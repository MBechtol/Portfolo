InstallDrivers script v1.1 
written by Matthew Bechtol and Dale Bivins 2023-12-18

to use:
. Copy script to you desktop
. Copy and extract driver folder to desktop
. Run powershell as admin.
. Change directory to location of script
. Enable running of scripts with "Set-ExecutionPolicy Bypass -scope Process -force" 
. Run script with ".\InstallDrivers.ps1"
. When prompted enter full file path of the driver folder you wish to install from. (example: "C:\Users\User\Desktop\Driversfolder")
. Upon completion a log file will be generated in the current location. to read file enter "Get-Content Log.txt"

	

Version revisions:
	2023-12-22: v1.1 added transcript function to the program.
	
