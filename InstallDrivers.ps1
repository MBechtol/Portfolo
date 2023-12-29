#get current location to save log file too
$location = Get-Location

#log Function
$Logfile= $location + "\Log.txt"

Start-Transcript -path $LogFile

#get file path from user
[string]$DriverFilePath = Read-Host "Enter file Path"

#list drivers

$InfList = Get-ChildItem "$DriverFilePath" -Recurse -Filter "*.inf" -ErrorAction SilentlyContinue | select -ExpandProperty PSChildName
[System.Collections.ArrayList]$InfListArray = @($InfList)
$InfListArrayCount = $InfListArray.count
Write-Host "`n`n$InfListArrayCount [.INF] files located within the '$DriverFilePath' directory:`n";$InfListArray;Write-Host "`n`n"
#WriteLog "`n`n$InfListArrayCount [.INF] files located within the '$DriverFilePath' directory:`n";$InfListArray;Write-Host "`n`n"

#install drivers
Get-ChildItem $DriverFilePath -Recurse -Filter "*.inf" | ForEach-Object { PNPUtil.exe /add-driver $_.FullName /install } 

Stop-Transcript

