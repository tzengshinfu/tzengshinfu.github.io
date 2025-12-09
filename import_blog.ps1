Set-Location -Path 'R:\tzengshinfu.github.io'

# Directories
$postsDir = Join-Path $PWD '_posts'
$destBase = Join-Path $PWD 'source\_posts'
$noTitleDir = Join-Path $destBase 'no_title'

# Ensure directories exist
if (-not (Test-Path $postsDir)) { New-Item -ItemType Directory -Path $postsDir | Out-Null }
if (-not (Test-Path $destBase)) { New-Item -ItemType Directory -Path $destBase | Out-Null }
if (-not (Test-Path $noTitleDir)) { New-Item -ItemType Directory -Path $noTitleDir | Out-Null }

$errors = @()
$jekyllImportCmd = Get-Command 'jekyll-import' -ErrorAction Stop
$jekyllImportExe = $jekyllImportCmd.Name
$jekyllImportArgsBase = @('rss')
$escapeUrlForCmd = $false

if ($jekyllImportCmd.Source -like '*.bat') {
    $rubyDir = Split-Path $jekyllImportCmd.Source -Parent
    $rubyExe = Join-Path $rubyDir 'ruby.exe'
    $rubyScript = Join-Path $rubyDir 'jekyll-import'
    if ((Test-Path $rubyExe -PathType Leaf) -and (Test-Path $rubyScript -PathType Leaf)) {
        $jekyllImportExe = $rubyExe
        $jekyllImportArgsBase = @($rubyScript) + $jekyllImportArgsBase
    } else {
        $escapeUrlForCmd = $true
    }
}

for ($i = 1; $i -le 270; $i++) {
    Write-Output "=== Index $i ==="
    $src = "https://tzengshinfu.blogspot.com/feeds/posts/default?alt=rss&start-index=$i&max-results=1"
    $sourceArg = if ($escapeUrlForCmd) { $src -replace '&', '^&' } else { $src }
    $commandArgs = $jekyllImportArgsBase + @('--source', $sourceArg, '--extract_tags', 'category')

    Write-Output "Running jekyll-import for index $i"
    try {
        & $jekyllImportExe @commandArgs 2>&1 | Write-Output
    } catch {
        Write-Output "Import command failed for index $i ($_)"
    }

    # brief pause to allow file write
    Start-Sleep -Milliseconds 500

    $newFiles = @(Get-ChildItem -Path $postsDir -File -Name -ErrorAction SilentlyContinue)
    if ($newFiles.Count -eq 0) {
        Write-Output "NO FILE for index $i"
        $errors += $i
        continue
    }

    foreach ($f in $newFiles) {
        $pattern = '^\d{4}-\d{2}-\d{2}-(?<title>.+)\.html$'
        if ($f -match $pattern -and ($Matches['title'].Trim() -ne '')) { $destDir = $destBase } else { $destDir = $noTitleDir }
        $srcPath = Join-Path $postsDir $f
        $dstPath = Join-Path $destDir $f
        try {
            if (Test-Path $dstPath) {
                $base = [System.IO.Path]::GetFileNameWithoutExtension($f)
                $ext = [System.IO.Path]::GetExtension($f)
                $chars = 48..57 + 65..90 + 97..122
                do {
                    $rand = -join (1..6 | ForEach-Object { [char](Get-Random -InputObject $chars) })
                    $newName = "$base-$rand$ext"
                    $dstPath = Join-Path $destDir $newName
                } while (Test-Path $dstPath)
                $f = (Split-Path $dstPath -Leaf)
            }
            Move-Item -Path $srcPath -Destination $dstPath
            Write-Output "Moved $f -> $destDir"
        } catch {
            Write-Output "Failed to move $f for index $i ($_)"
            $errors += $i
        }
    }
}

Write-Output '--- DONE ---'
if ($errors.Count -gt 0) { Write-Output "Errors (no file generated) for indices: $($errors -join ', ')" } else { Write-Output "All imports produced files and were moved." }
