@echo off
echo Cleaning up...
rd /s /q node_modules
del /f /q package-lock.json
del /f /q .next

echo Installing dependencies...
npm install

echo Building the project...
npm run build

echo Starting development server...
npm run dev
