# UninstallApplications.ps1 - Generated by Blackbox.ai

# List of applications to uninstall
$applications = @(
    "Google.Chrome",
    "Mozilla.Firefox",
    "Notepad++.Notepad++"
)

# Loop through each application and uninstall it
foreach ($app in $applications) {
    Write-Host "Uninstalling $app..."
    winget uninstall --id $app --silent --accept-source-agreements --accept-package-agreements
    if ($LASTEXITCODE -eq 0) {
        Write-Host "$app uninstalled successfully."
    } else {
        Write-Host "Failed to uninstall $app."
    }
}
