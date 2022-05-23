# Sublime Text

```% brew install --cask sublime-text```

Command palette: "command" + "shift" + "p"

## Setup package control
1. Install "Package Control"
    - Command palette: "Install package control"
2. Install Packages
    - Command palette: "Install package: <package>"
        - Git
        - SublimeLinter
        - SublimeLinter-pycodestyle
        - SublimeLinter-pylint


## Settings
1. Settings
Command palette -> Preferences: Settings
```json
{
	"theme": "Default Dark.sublime-theme",
	"ignored_packages":
	[
		"Vintage",
	],
}
```

2. SublimeLinter Settings
Command palette -> Preferences: SublimeLinter Settings
```json
{
    "linters": {
        "pycodestyle": {
            "max-line-length": 100
        }
    }
}
```
