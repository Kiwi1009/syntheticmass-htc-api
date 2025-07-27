Write-Host "========================================" -ForegroundColor Green
Write-Host "HTC API - Push to Personal GitHub" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""

$github_username = Read-Host "Please enter your GitHub username"

Write-Host ""
Write-Host "Adding personal remote repository..." -ForegroundColor Yellow
git remote add personal "https://github.com/$github_username/htc-api.git"

Write-Host ""
Write-Host "Pushing to your personal GitHub repository..." -ForegroundColor Yellow
git push personal master

Write-Host ""
Write-Host "Done! Your HTC API is now available at:" -ForegroundColor Green
Write-Host "https://github.com/$github_username/htc-api" -ForegroundColor Cyan
Write-Host ""
Read-Host "Press Enter to continue" 