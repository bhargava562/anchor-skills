<#
.SYNOPSIS
    Synchronizes skill-shelf skills to standard AI agent directories on Windows.

.DESCRIPTION
    Symlinks, junctions, or copies all skills from skills/* to the global skill
    discovery directories of supported AI agents:
      - Antigravity / Gemini: ~/.gemini/skills/
      - Claude Code:          ~/.claude/skills/
      - Codex / OpenCode:     ~/.codex/skills/
      - Hermes Agent:         ~/.hermes/skills/

.PARAMETER Mode
    Sync method to use:
      - 'Auto' (default): Attempts directory Junction first (fast, zero disk duplication, no elevation required), falling back to Copy if unavailable.
      - 'Junction': Forces NTFS Directory Junctions.
      - 'Symlink': Creates directory Symbolic Links (requires Developer Mode or Administrator privileges).
      - 'Copy': Performs a full file copy.

.PARAMETER TargetAgent
    Optional filter for a specific agent: 'gemini', 'claude', 'codex', 'hermes', or 'all' (default).

.PARAMETER Force
    Overwrites/replaces existing targets without prompting.

.EXAMPLE
    .\scripts\sync.ps1
    Synchronizes all skills using Auto mode (Junction with Copy fallback).

.EXAMPLE
    .\scripts\sync.ps1 -Mode Copy -Force
    Forces a fresh copy of all skills to agent directories.
#>

[CmdletBinding()]
param(
    [ValidateSet('Auto', 'Junction', 'Symlink', 'Copy')]
    [string]$Mode = 'Auto',

    [ValidateSet('all', 'gemini', 'claude', 'codex', 'hermes')]
    [string]$TargetAgent = 'all',

    [switch]$Force = $true
)

$ErrorActionPreference = 'Stop'

# Determine source skills directory
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RepoRoot = Split-Path -Parent $ScriptDir
$SkillsDir = Join-Path $RepoRoot "skills"

if (-not (Test-Path -LiteralPath $SkillsDir -PathType Container)) {
    Write-Error "Source skills directory not found: $SkillsDir"
    exit 1
}

# Determine User Home directory
$UserHome = if ($env:USERPROFILE) { $env:USERPROFILE } else { [Environment]::GetFolderPath('UserProfile') }

# Define standard target discovery roots
$AgentTargets = [ordered]@{
    "gemini" = Join-Path $UserHome ".gemini\skills"
    "claude" = Join-Path $UserHome ".claude\skills"
    "codex"  = Join-Path $UserHome ".codex\skills"
    "hermes" = Join-Path $UserHome ".hermes\skills"
}

# Filter targets if requested
$ActiveTargets = @{}
if ($TargetAgent -eq 'all') {
    $ActiveTargets = $AgentTargets
} else {
    $ActiveTargets[$TargetAgent] = $AgentTargets[$TargetAgent]
}

# Discover all valid skill directories (must contain SKILL.md)
$SkillFolders = Get-ChildItem -LiteralPath $SkillsDir -Directory | Where-Object {
    Test-Path -LiteralPath (Join-Path $_.FullName "SKILL.md")
}

if (-not $SkillFolders) {
    Write-Warning "No valid skills with SKILL.md found in $SkillsDir"
    exit 0
}

Write-Host ("=" * 70) -ForegroundColor Cyan
Write-Host "SKILL-SHELF ENVIRONMENT SYNCHRONIZER (Windows)" -ForegroundColor Cyan
Write-Host "Source: $SkillsDir"
Write-Host "Mode:   $Mode"
Write-Host ("=" * 70) -ForegroundColor Cyan

function Sync-SkillFolder {
    param(
        [System.IO.DirectoryInfo]$SourceDir,
        [string]$TargetParentDir,
        [string]$PreferredMode
    )

    $SkillName = $SourceDir.Name
    $DestinationPath = Join-Path $TargetParentDir $SkillName

    # Ensure parent directory exists
    if (-not (Test-Path -LiteralPath $TargetParentDir)) {
        [void](New-Item -ItemType Directory -Path $TargetParentDir -Force)
    }

    # Handle existing destination
    if (Test-Path -LiteralPath $DestinationPath) {
        $Item = Get-Item -LiteralPath $DestinationPath -Force
        $isReparse = [bool]($Item.Attributes -band [System.IO.FileAttributes]::ReparsePoint)

        if ($isReparse) {
            # Safely remove existing junction / symlink
            cmd /c "rmdir `"$DestinationPath`"" 2>$null
            if (Test-Path -LiteralPath $DestinationPath) {
                Remove-Item -LiteralPath $DestinationPath -Force -Recurse
            }
        } else {
            Remove-Item -LiteralPath $DestinationPath -Force -Recurse
        }
    }

    $MethodUsed = ""

    if ($PreferredMode -eq 'Copy') {
        Copy-Item -LiteralPath $SourceDir.FullName -Destination $DestinationPath -Recurse -Force
        $MethodUsed = "Copy"
    }
    elseif ($PreferredMode -eq 'Symlink') {
        New-Item -ItemType SymbolicLink -Path $DestinationPath -Target $SourceDir.FullName -Force | Out-Null
        $MethodUsed = "SymbolicLink"
    }
    elseif ($PreferredMode -eq 'Junction') {
        New-Item -ItemType Junction -Path $DestinationPath -Target $SourceDir.FullName -Force | Out-Null
        $MethodUsed = "Junction"
    }
    else { # Auto: Try Junction -> Symlink -> Copy
        try {
            New-Item -ItemType Junction -Path $DestinationPath -Target $SourceDir.FullName -Force | Out-Null
            $MethodUsed = "Junction"
        }
        catch {
            try {
                New-Item -ItemType SymbolicLink -Path $DestinationPath -Target $SourceDir.FullName -Force | Out-Null
                $MethodUsed = "SymbolicLink"
            }
            catch {
                Copy-Item -LiteralPath $SourceDir.FullName -Destination $DestinationPath -Recurse -Force
                $MethodUsed = "Copy (Fallback)"
            }
        }
    }

    return $MethodUsed
}

$SuccessCount = 0
$TotalOperations = $ActiveTargets.Count * $SkillFolders.Count

foreach ($AgentKey in $ActiveTargets.Keys) {
    $TargetRoot = $ActiveTargets[$AgentKey]
    Write-Host "`nTarget [$AgentKey]: $TargetRoot" -ForegroundColor Yellow

    foreach ($Folder in $SkillFolders) {
        try {
            $Used = Sync-SkillFolder -SourceDir $Folder -TargetParentDir $TargetRoot -PreferredMode $Mode
            Write-Host "  [OK] $($Folder.Name) -> $Used" -ForegroundColor Green
            $SuccessCount++
        }
        catch {
            Write-Host "  [FAIL] $($Folder.Name): $_" -ForegroundColor Red
        }
    }
}

Write-Host ""
Write-Host ("-" * 70) -ForegroundColor Cyan
Write-Host "Synchronization complete: $SuccessCount/$TotalOperations operations succeeded." -ForegroundColor Cyan

exit 0
