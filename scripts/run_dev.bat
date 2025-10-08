@echo off
setlocal enableextensions
pushd %~dp0\..

echo Starting HarshaOS backend...
start "HarshaOS Backend" cmd /k "python backend\main.py"

echo Starting HarshaOS UI...
pushd ui
if not exist node_modules (
  echo Installing UI dependencies...
  call npm install
)
call npm start
popd

popd
endlocal
