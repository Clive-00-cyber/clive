@echo off
echo Installation des dependances pour le generateur de tableaux...
echo.

:: Verifier si Python est installe
python --version >nul 2>&1
if errorlevel 1 (
    echo ERREUR: Python n'est pas installe ou n'est pas dans le PATH.
    echo Veuillez installer Python depuis https://www.python.org/downloads/
    pause
    exit /b 1
)

:: Installer les dependances
echo Installation de PyInstaller...
pip install pyinstaller

echo Installation de ReportLab...
pip install reportlab

echo Installation de Pillow...
pip install pillow

echo.
echo Toutes les dependances sont installees!
echo.
echo Pour creer l'executable, executez:
echo pyinstaller --onefile --windowed --name "GenerateurTableauxNoms" main.py
echo.
pause
