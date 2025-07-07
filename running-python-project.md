# Installing pyenv
```
git clone https://github.com/pyenv/pyenv.git ~/.local/src
```

## Exporting pyenv path as environment variable
Add this line to your .bashrc if you use bash or .zshenv if you use zsh
```
export PYENV_ROOT="$HOME/.local/src/pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)
```

# Installing and switching to different python version
Listing all available python versions
```
pyenv install -l
```
Listing all installed python versions
```
pyenv versions
```
Installing
```
pyenv install <version>
```
Switching
```
pyenv global <version>
```
Checking globally activated python version
```
python --version
```

# Creating virtual environment 
Cd to your python project directory
```
python3 -m venv .venv
```
You can specify any kind of name in case of .venv

# Activating virtual environment 
```
source .venv/bin/activate
```
For deactivating virtual environment use
```
deactivate
```
# For upgrading to latest pip version
```
python<version> -m pip install --upgrade pip
```

# Installing Dependencies of your python project
```
pip install -r requirements.txt
```

# Creating requirements.txt file
```
pip freeze > requirements.txt
```
