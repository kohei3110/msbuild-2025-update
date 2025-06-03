# Run this script first to set up the environment for Azure DevOps Extension development.
# It installs the required ps_modules, sets up the task paths, and builds the front-end for AIAgentReport.
# It also updates the version in vss-extension.json and creates a production version of the file.
$scriptsFolder = Split-Path -Path $MyInvocation.MyCommand.Path -Parent
. $scriptsFolder\set-variables.ps1

New-Item -Path $prodExtensionDir -ItemType Directory -Force | Out-Null
Push-Location -Path $repoRoot

try {
    Write-Host "Building AIAgentReport web UI..."
    $reportPath = Join-Path -Path $repoRoot -ChildPath "tasks/AIAgentReport"
    Push-Location -Path $reportPath
    try {
        npm ci
        npm run build
        Write-Host "AIAgentReport build completed successfully" -ForegroundColor Green
    }
    catch {
        Write-Error "Error building AIAgentReport: $_"
        exit 1
    }
    finally {
        # Always return to the previous directory even if there are errors
        Pop-Location
    }

    # Import the utilities module with shared functions
    $utilsPath = Join-Path -Path $repoRoot -ChildPath "scripts/utilities.ps1"
    . $utilsPath

    # Update version in vss-extension.json
    Write-Host "Updating version in vss-extension.json..."
    $vssExtensionPath = Join-Path -Path $repoRoot -ChildPath "vss-extension.json"
    $vssExtensionProdPath = Join-Path -Path $prodExtensionDir -ChildPath "vss-extension.json"

    $vssExtension = Get-Content -Path $vssExtensionPath -Raw | ConvertFrom-Json
    $currentVersion = $vssExtension.version
    $vssExtension.version = Update-VersionNumber -CurrentVersion $currentVersion

    $vssExtension | ConvertTo-Json -Depth 10 | Set-Content -Path $vssExtensionProdPath
    Write-Host "Version updated successfully in vss-extension.json for prod" -ForegroundColor Green

    # Copy files defined in vss-extension.json using the utility function
    $copySuccess = Copy-FilesFromVssExtension -SourceRootPath $repoRoot -DestinationRootPath $prodExtensionDir -VssExtensionObject $vssExtension
    if (-not $copySuccess) {
        Write-Error "Failed to copy files defined in vss-extension.json 'files' section or section not found"
        exit 1
    }
    Write-Host "Copied supporting files for extension" -ForegroundColor Green

    Write-Host "Setting up VstsTaskSdk module..."

    # Use the download-vstsTaskSdk.ps1 
    & (Join-Path -Path $scriptsFolder -ChildPath "download-vstsTaskSdk.ps1")
    if ($LASTEXITCODE -ne 0) {
        Write-Error "Failed to download VstsTaskSdk module"
        exit 1
    }
    Write-Host "VstsTaskSdk module downloaded successfully" -ForegroundColor Green

    $commonLatestTask = Join-Path -Path $repoRoot -ChildPath "tasks/AIAgentEvaluation"
    $filesToCopyInLatest = @(
        "task.json",
        "run.ps1",
        "check-python.ps1"
    )
    foreach ($file in $filesToCopyInLatest) {
        $sourcePath = Join-Path -Path $commonLatestTask -ChildPath $file
        $destPath = Join-Path -Path $prodExtensionDir -ChildPath "tasks/AIAgentEvaluation/$latestVersion/$file"
        $removePath = Join-Path -Path $prodExtensionDir -ChildPath "tasks/AIAgentEvaluation/$file"
        Copy-Item -Path $sourcePath -Destination $destPath -Force
        Remove-Item -Path $removePath -Force -ErrorAction SilentlyContinue
        Write-Host "Copied $file to $destPath" -ForegroundColor Green
    }

    # add action.py, analysis and pyproject.toml to the production v1 directory
    . $scriptsFolder/download-previousVersions.ps1

    # Add action.py, analysis and pyproject.toml to the production latest(v2) directory
    $filesToCopy = @(
        "action.py",
        "pyproject.toml"
    )
    $foldersToCopy = @(
        "analysis"
    )
    foreach ($file in $filesToCopy) {
        $sourcePath = Join-Path -Path $repoRoot -ChildPath $file
        $destPath = Join-Path -Path $prodExtensionDir -ChildPath "tasks/AIAgentEvaluation/$latestVersion/$file"
        Copy-Item -Path $sourcePath -Destination $destPath -Force
    }
    foreach ($folder in $foldersToCopy) {
        $sourcePath = Join-Path -Path $repoRoot -ChildPath $folder
        $destPath = Join-Path -Path $prodExtensionDir -ChildPath "tasks/AIAgentEvaluation/$latestVersion/$folder"
        Copy-Directory -SourceDir $sourcePath -DestinationDir $destPath
    }


    $validate = Check-CriticalFiles -OutputDir $prodExtensionDir -IsDevExtension $false
    if (-not $validate) {
        Write-Error "Critical files check failed for production extension"
        exit 1
    }
    Write-Host "Critical files check passed for production extension" -ForegroundColor Green
}
finally {
    # Return to the original directory
    Pop-Location
}