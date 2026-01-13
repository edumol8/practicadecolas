Write-Host "Creando entorno virtual..." -ForegroundColor Green
python -m venv generico_envrabbitmq

Write-Host "Activando entorno virtual..." -ForegroundColor Yellow
& .\generico_envrabbitmq\Scripts\Activate.ps1

Write-Host "Instalando pika..." -ForegroundColor Cyan
pip install pika

Write-Host "Entorno virtual creado y pika instalado!" -ForegroundColor Green
Write-Host "Entorno activado: $(Get-Location)" -ForegroundColor Magenta
pause