# .dotfiles

A repository for dotfiles that can be managed with GNU stow.

# Installation

clone this repository

# Usage

```bash
cd .dotfiles
stow -nvSt ~ *
```

The 'n' flag set stow to simulation mode (while 'v' is for 'verbose'). That way changes will not be applied but rather shown in stdout.
The 't' flat specifies the target directory and needs an argument (in this case '~' for the home directory of the current user)
The '\*' is a shorthand for all and could be replaced with a space separated list of directories in this repository
If the suggested changes are acceptable:

```bash
stow -vSt ~ *
```
