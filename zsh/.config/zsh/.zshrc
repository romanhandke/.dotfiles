if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

export ZSH="${HOME}/.config/oh-my-zsh"
export BAT_CONFIG_PATH="${HOME}/.config/bat/batrc"
export XDG_CONFIG_HOME="${HOME}/.config"
export HISTFILE="${HOME}/.local/hist/history"

export NVM_DIR="${HOME}/.config/nvm"
export NVM_BIN="${HOME}/.config/nvm/bin"
export NVM_DIR="${HOME}/.config/nvm"
[ -s "${NVM_DIR}/nvm.sh" ] && \. "${NVM_DIR}/nvm.sh"
[ -s "${NVM_DIR}/bash_completion" ] && \. "${NVM_DIR}/bash_completion"

ZSH_THEME="powerlevel10k/powerlevel10k"
ZSH_HIGHLIGHT_HIGHLIGHTERS=(main brackets pattern cursor)

typeset -A ZSH_HIGHLIGHT_STYLES
ZSH_HIGHLIGHT_STYLES[command]='fg=blue,bold'
ZSH_HIGHLIGHT_STYLES[alias]='fg=blue,bold'
ZSH_HIGHLIGHT_STYLES[builtin]='fg=blue,bold'

DISABLE_AUTO_TITLE="true"
# ENABLE_CORRECTION="true"
COMPLETION_WAITING_DOTS="true"

plugins=(git composer vi-mode zsh-syntax-highlighting tmux)
ZSH_TMUX_AUTOSTART="true"
ZSH_TMUX_CONFIG="${HOME}/.config/tmux/tmux.conf"

source $ZSH/oh-my-zsh.sh

alias zshconfig="vim ${HOME}/.config/zsh/.zshrc"
alias qtileconfig="vim ${HOME}/.config/qtile/config.py"
alias qtileautostart="vim ${HOME}/.config/qtile/autostart.sh"
alias fzfconfig="vim ${HOME}/.config/fzf/fzf.zsh"
alias alacrittyconfig="vim ${HOME}/.config/alacritty/alacritty.yml"
alias gb="${HOME}/.dotfiles/scripts/branch-select.sh"

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
# [[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
[[ ! -f ~/.config/zsh/.p10k.zsh ]] || source ~/.config/zsh/.p10k.zsh

[ -f "${HOME}/.config/fzf/fzf.zsh" ] && source "${HOME}/.config/fzf/fzf.zsh"
