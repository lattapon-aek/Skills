param(
    [Parameter(Mandatory = $true)]
    [string]$Name,

    [Parameter(Mandatory = $true)]
    [string]$DisplayName,

    [Parameter(Mandatory = $true)]
    [string]$ShortDescription,

    [Parameter(Mandatory = $true)]
    [string]$DefaultPrompt,

    [string]$Resources = "references",
    [string]$SkillRoot = ".\suites\software-engineering\skills"
)

$codexHome = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME '.codex' }
$initScript = Join-Path $codexHome 'skills\.system\skill-creator\scripts\init_skill.py'
$validateScript = Join-Path $codexHome 'skills\.system\skill-creator\scripts\quick_validate.py'

if (-not (Test-Path $initScript)) {
    Write-Error "skill-creator toolkit not found at $codexHome; set CODEX_HOME to override"
    exit 1
}

python $initScript $Name --path $SkillRoot --resources $Resources --interface "display_name=$DisplayName" --interface "short_description=$ShortDescription" --interface "default_prompt=$DefaultPrompt"
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

python $validateScript (Join-Path $SkillRoot $Name)
exit $LASTEXITCODE
