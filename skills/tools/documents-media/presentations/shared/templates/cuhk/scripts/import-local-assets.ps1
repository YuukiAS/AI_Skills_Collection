param(
  [string]$TemplateZip = "C:\Users\humc2\Downloads\CUHK Template.zip",
  [string]$Destination = ".\private-cuhk-assets"
)

New-Item -ItemType Directory -Force -Path $Destination | Out-Null
Expand-Archive -LiteralPath $TemplateZip -DestinationPath $Destination -Force
Write-Host "Imported local CUHK assets to $Destination. Do not commit them unless redistribution rights are confirmed."
