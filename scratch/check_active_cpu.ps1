$samples = Get-Counter '\Process(*)\% Processor Time'
$active = $samples.CounterSamples | Where-Object { $_.InstanceName -notmatch '^_Total$|^Idle$' -and $_.CookedValue -gt 1 } | Sort-Object CookedValue -Descending
$active | Select-Object -First 10 InstanceName, @{Name="CPU_Percent";Expression={[math]::Round($_.CookedValue, 1)}} | Format-Table -AutoSize
