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
    [string]$SkillRoot = ".\skills"
)

$initScript = "C:\Users\lattapon.kea\.codex\skills\.system\skill-creator\scripts\init_skill.py"
$validateScript = "C:\Users\lattapon.kea\.codex\skills\.system\skill-creator\scripts\quick_validate.py"

python $initScript $Name --path $SkillRoot --resources $Resources --interface "display_name=$DisplayName" --interface "short_description=$ShortDescription" --interface "default_prompt=$DefaultPrompt"
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

python $validateScript (Join-Path $SkillRoot $Name)
exit $LASTEXITCODE
