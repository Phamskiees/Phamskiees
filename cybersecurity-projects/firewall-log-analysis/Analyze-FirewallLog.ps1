[CmdletBinding()]
param(
    [Parameter(Mandatory)]
    [string]$Path,

    [Parameter(Mandatory)]
    [string]$OutputDirectory
)

$ErrorActionPreference = 'Stop'

if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
    throw "Firewall log not found: $Path"
}

$lines = Get-Content -LiteralPath $Path
$fieldsLine = $lines | Where-Object { $_ -like '#Fields:*' } | Select-Object -Last 1
if (-not $fieldsLine) {
    throw 'The log does not contain a #Fields header.'
}

$fields = ($fieldsLine -replace '^#Fields:\s*', '') -split '\s+'
$events = foreach ($line in $lines) {
    if ([string]::IsNullOrWhiteSpace($line) -or $line.StartsWith('#')) {
        continue
    }

    $values = $line -split '\s+'
    if ($values.Count -ne $fields.Count) {
        Write-Warning "Skipping malformed log line: $line"
        continue
    }

    $record = [ordered]@{}
    for ($index = 0; $index -lt $fields.Count; $index++) {
        $record[$fields[$index]] = $values[$index]
    }
    [pscustomobject]$record
}

New-Item -ItemType Directory -Path $OutputDirectory -Force | Out-Null
$eventsPath = Join-Path $OutputDirectory 'events.csv'
$summaryPath = Join-Path $OutputDirectory 'summary.json'
$events | Export-Csv -LiteralPath $eventsPath -NoTypeInformation

function Convert-Group {
    param([object[]]$Groups)
    @($Groups | ForEach-Object {
        [ordered]@{
            value = $_.Name
            count = $_.Count
        }
    })
}

$summary = [ordered]@{
    source_file = Split-Path -Leaf $Path
    generated_at = (Get-Date).ToString('o')
    total_events = @($events).Count
    by_action = Convert-Group (@($events | Group-Object action | Sort-Object Count -Descending))
    by_protocol = Convert-Group (@($events | Group-Object protocol | Sort-Object Count -Descending))
    top_sources = Convert-Group (@($events | Group-Object src-ip | Sort-Object Count -Descending | Select-Object -First 10))
    top_destination_ports = Convert-Group (@($events | Group-Object dst-port | Sort-Object Count -Descending | Select-Object -First 10))
}

$summary | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath $summaryPath -Encoding utf8

Write-Host "Parsed events: $(@($events).Count)"
Write-Host "Events CSV: $eventsPath"
Write-Host "Summary JSON: $summaryPath"
