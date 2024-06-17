# Create the project directory structure
$directories = "client", "server", "client\resources", "client\resources\icons", "client\resources\styles", "server\modules"
foreach ($directory in $directories) {
    if (!(Test-Path $directory)) {
        New-Item -ItemType Directory -Path $directory
    }
}

# Create the required files
$files = "client\main.py", "client\requirements.txt", "client\startup.ps1", "server\app.py", "server\requirements.txt", "server\startup.ps1", "server\modules\__init__.py", "server\modules\routes.py", "server\modules\utils.py", "README.md"
foreach ($file in $files) {
    if (!(Test-Path $file)) {
        New-Item -ItemType File -Path $file
    }
}

# Create virtual environments
if (!(Test-Path "client_venv")) {
    python -m venv client_venv
}
if (!(Test-Path "server_venv")) {
    python -m venv server_venv
}

# Activate client virtual environment and install requirements
if (Test-Path "client\requirements.txt") {
    .\client_venv\Scripts\Activate.ps1
    pip install -r client\requirements.txt
    deactivate
}

# Activate server virtual environment and install requirements
if (Test-Path "server\requirements.txt") {
    .\server_venv\Scripts\Activate.ps1
    pip install -r server\requirements.txt
    deactivate
}

Write-Host "Setup complete. Use the following commands to run the server and client:"
Write-Host ".\server_venv\Scripts\Activate.ps1; python server\app.py"
Write-Host ".\client_venv\Scripts\Activate.ps1; python client\main.py"