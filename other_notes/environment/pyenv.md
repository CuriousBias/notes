# PyEnv
- Change global or project python versions
- No need to load python into shell

## Function
1. pyenv intercepts python commands using shim executables in `PATH`
2. pyenv then determines specified python version
3. pyenv hands commands to said specified python version

### PATH insert
- pyenv inserts directory of shims at beginning of `PATH`.
- This ensures system checks with pyenv before searching remaining directories for python installations.

### Shims
- Lightweight exeuctables to pass python commands to pyenv
Process (example with `pip` command)
1. Seeach `PATH` for executable file named `pip`
2. Find pyenv shim named `pip` at beginning of path.
3. Run shim called `pip`

### Python version selection
When executing shim, pyenv determines python version from 4 sources (in this order)
1. `PYENV_VERSION` environment variable if set. Set by `pyenv shell` in current shell session.
2. Application specific `.python-version`. Set current direcotry file with `pyenv local`
3. The first `.python-version` file found by searching each parent directory.
4. The global `$(pyenv root)/version` file. Set by `pyenv global`

### Installation location
Each python version is installed into own directory under `$(pyenv root)/versions`
Example (3 versions installed)
- `$(pyenv root)/versions/2.7.8`
- `$(pyenv root)/versions/3.8.10`
- `$(pyenv root)/versions/3.10.12`


## Installation

### MacOS
Use brew
```
brew update
brew install pyenv
```

### Linux
` curl https://pyenv.run | bash`

## Setup Shell Environment
This ensures pyenv will function correctly in your shell.
Place following commands in approriate shell source file.

### MacOS
For Zsh
```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```

## Install python build dependencies

### MacOS
1. Install XCode Command Line Tools (if not already done) `xcode-select --install`
2. Install dependencies via brew `brew install openssl readline sqlite3 xz zlib tcl-tk`

## Maintenance

### Uninstall
To remove individual python versions 
1. Run `pyenv uninstall <version>`
2. Remove specific directory Ex: $(pyenv root)/versions/3.8.10 with `rm -rf`
3. If installed with brew: `brew uninstall pyenv`

### Upgrading
1. If installed with brew: `brew upgrade pyenv`
