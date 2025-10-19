@echo off
title Construction de l'executable - Generateur de Tableaux de Noms
echo Construction de l'application executable...
echo.

:: Creer un environnement propre
if exist "dist" rmdir /s /q dist
if exist "build" rmdir /s /q build

:: Construire l'executable
pyinstaller --onefile --windowed --name "GenerateurTableauxNoms" --icon=icon.ico main.py

if errorlevel 1 (
    echo.
    echo ERREUR lors de la construction!
    pause
    exit /b 1
)

echo.
echo ✅ Construction terminee avec succes!
echo.
echo L'executable se trouve dans le dossier: dist\GenerateurTableauxNoms.exe
echo.
echo Vous pouvez maintenant copier cet executable sur un autre ordinateur.
echo.
pause