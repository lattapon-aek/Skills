param(
    [string]$Destination = (Join-Path $HOME '.codex\skills')
)

$ErrorActionPreference = 'Stop'

$repoRoot = Split-Path -Parent $PSScriptRoot
$skills = @(
    @{
        Name = 'software-engineering-core'
        Path = Join-Path $repoRoot 'suites/software-engineering/skills/software-engineering-core'
    },
    @{
        Name = 'change-review'
        Path = Join-Path $repoRoot 'suites/software-engineering/skills/change-review'
    },
    @{
        Name = 'verification-hazards'
        Path = Join-Path $repoRoot 'suites/software-engineering/skills/verification-hazards'
    }
)

New-Item -ItemType Directory -Force -Path $Destination | Out-Null

foreach ($skill in $skills) {
    $target = Join-Path $Destination $skill.Name

    if (Test-Path $target) {
        Write-Host "skipped $($skill.Name): target already exists at $target"
        continue
    }

    New-Item -ItemType Junction -Path $target -Target $skill.Path | Out-Null
    Write-Host "linked $($skill.Name) -> $($skill.Path)"
}
