# Setup fzf
# ---------
# Install via package manager

# Auto-completion
# ---------------
[[ $- == *i* ]] && source "${HOME}/.config/fzf/completion.zsh" 2> /dev/null

# Key bindings
# ------------
FD_OPTIONS="--exclude .git"
export FZF_DEFAULT_OPTS="--no-mouse --height 50% --multi --inline-info --layout=reverse"
export FZF_DEFAULT_COMMAND="rg --files"
export FZF_CTRL_T_OPTS="--preview 'bat {}'"
export FZF_CTRL_T_COMMAND="rg --files"
export FZF_ALT_C_OPTS="--preview 'tree -C {} | head -50'"
export FZF_ALT_C_COMMAND="fd --type d ${FD_OPTIONS}"

source "${HOME}/.config/fzf/key-bindings.zsh"
