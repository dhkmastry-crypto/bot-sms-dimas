$t = (Get-Counter '\Processor(_Total)\% Processor Time').CounterSamples.CookedValue
$cores = (Get-CimInstance Win32_Processor | Measure-Object -Property NumberOfLogicalProcessors -Sum).Sum
Write-Host "Total CPU across all cores: $([math]::Round($t, 1))%"
Write-Host "Total Logical Cores: $cores"
