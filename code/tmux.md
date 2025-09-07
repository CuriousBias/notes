# Tmux

### Purpose
- Terminal tool to manage multiple command line sessions.
- Great for remote execution as session stays alive if disconnected.

### Install

1. macOs: `brew install tmux`
2. Ubuntu: `apt install tmux`

## Use

### Modes
- Copy mode (to scroll): `ctrl + b, [`

### Sessions

- List sessions: `tmux ls`
- Start a new session: `tmux new -s kiz1`
- End session: `tmux kill-session -t kiz1`
- End all: `tmux kill-session -a`, ctrl + b, s

- Attach to session: `tmux a -t kiz1`
- Detach from current session: ctrl + b, d

### Windows
Each session can hold multiple windows
Variables maintained in different windows?

- Create window: `ctrl + b, c`
- List windows: `ctrl + b, w`

### Panes
Visual split of a window

- Split vertically: `ctrl + b, %`
- Split horizontally: `ctrl + b, "`
- Navigate panes: `ctrl + b, each arrow key`
- Close current pane: `ctrl + b, x`

### Misc

- Disable mouse scroll history: `tmux set -g mouse on`

### .tmux.conf
- Setup a tmux config file. 
- This file needs to be on the ssh server with the tmux session.
- Copy tmux.conf to host: `scp .tmux.conf kiz@cloud:~/` or `scp .tmux.conf oisl@otac-node-13:~/`

```
# Enable mouse mode
set -g mouse on

# Modern copy mode settings
bind-key -T copy-mode-vi v send-keys -X begin-selection
bind-key -T copy-mode-vi y send-keys -X copy-selection-and-cancel
bind-key -T copy-mode-vi y send-keys -X copy-pipe-and-cancel "pbcopy"  # for macOS

# For better system clipboard integration
set -g set-clipboard on
```
