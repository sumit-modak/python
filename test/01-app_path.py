import os
import sys

if getattr(sys, 'frozen', False):
    currentFilePath = os.path.dirname(sys.executable)
else:
    currentFilePath = os.path.dirname(os.path.abspath(__file__))

print(currentFilePath)

fileName = os.path.basename(sys.argv[0])
filePath = os.path.join(currentFilePath, fileName)

print(fileName)
print(filePath)

startupFolderPath = os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
startupFilePath = os.path.join(startupFolderPath, fileName)

print(startupFolderPath)
print(startupFilePath)
