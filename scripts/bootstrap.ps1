$ErrorActionPreference = 'Stop'

$venvPath = Join-Path $PSScriptRoot '..\.venv'
$envFile = Join-Path $PSScriptRoot '..\.env'
$envExample = Join-Path $PSScriptRoot '..\.env.example'
$templatesDir = Join-Path $PSScriptRoot '..\src\prompts\templates'
$promptsDir = Join-Path $PSScriptRoot '..\src\prompts'

if (-not (Test-Path $venvPath)) {
    python -m venv $venvPath
}

& (Join-Path $venvPath 'Scripts\Activate.ps1')

pip install -r (Join-Path $PSScriptRoot '..\requirements.txt')

if (-not (Test-Path $envFile)) {
    Copy-Item $envExample $envFile
    Write-Host 'Created .env from .env.example. Please add your keys.'
}

if (Test-Path $templatesDir) {
    Get-ChildItem -Path $templatesDir -Filter *.py | ForEach-Object {
        $target = Join-Path $promptsDir $_.Name
        if (-not (Test-Path $target)) {
            Copy-Item $_.FullName $target
        }
    }
}

Write-Host 'Run: langgraph dev --allow-blocking'
