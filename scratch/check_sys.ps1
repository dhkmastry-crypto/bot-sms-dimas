$cpu = Get-CimInstance Win32_Processor | Measure-Object -Property LoadPercentage -Average | Select-Object -ExpandProperty Average
Write-Host "CPU Load Average: $cpu %"

$os = Get-CimInstance Win32_OperatingSystem
$totalRamGB = [math]::Round($os.TotalVisibleMemorySize / 1MB, 2)
$freeRamGB = [math]::Round($os.FreePhysicalMemory / 1MB, 2)
$usedRamGB = [math]::Round(($os.TotalVisibleMemorySize - $os.FreePhysicalMemory) / 1MB, 2)

Write-Host "Total RAM: $totalRamGB GB"
Write-Host "Used RAM:  $usedRamGB GB"
Write-Host "Free RAM:  $freeRamGB GB"

$edgeProcs = Get-Process -Name msedge -ErrorAction SilentlyContinue
$edgeCount = if ($edgeProcs) { $edgeProcs.Count } else { 0 }
$edgeRamGB = if ($edgeProcs) { [math]::Round(($edgeProcs | Measure-Object WorkingSet64 -Sum).Sum / 1GB, 2) } else { 0 }

Write-Host "Edge Processes: $edgeCount | Total RAM: $edgeRamGB GB"

$pyProcs = Get-Process -Name python -ErrorAction SilentlyContinue
$pyCount = if ($pyProcs) { $pyProcs.Count } else { 0 }
$pyRamGB = if ($pyProcs) { [math]::Round(($pyProcs | Measure-Object WorkingSet64 -Sum).Sum / 1GB, 2) } else { 0 }

Write-Host "Python Processes: $pyCount | Total RAM: $pyRamGB GB"
