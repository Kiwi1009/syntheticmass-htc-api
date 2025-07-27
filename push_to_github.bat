@echo off
echo ========================================
echo HTC API - Push to Personal GitHub
echo ========================================
echo.

echo Please enter your GitHub username:
set /p github_username=

echo.
echo Adding personal remote repository...
git remote add personal https://github.com/%github_username%/htc-api.git

echo.
echo Pushing to your personal GitHub repository...
git push personal master

echo.
echo Done! Your HTC API is now available at:
echo https://github.com/%github_username%/htc-api
echo.
pause 