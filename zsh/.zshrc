export ZSH="/home/r-handke/.oh-my-zsh"

ZSH_THEME="powerlevel10k/powerlevel10k"

plugins=(git zsh-syntax-highlighting vi-mode)

source $ZSH/oh-my-zsh.sh

if [ "$TMUX" = "" ]; then tty-clock -c -C 6 -D; fi
if [ "$TMUX" = "" ]; then tmux; fi


path+=(/snap/bin)

# FZF
FD_OPTIONS="--follow --exclude .git --exclude node_modules"
export FZF_DEFAULT_OPTS=" \
  --no-mouse \
  --height 50% \
  --reverse \
  --multi \
  --inline-info \
  --bind='ctrl-y:execute-silent(echo {+} | xclip -i -sel c -f | xclip -i -sel p)'"
export FZF_DEFAULT_COMMAND="git ls-files --cached --others --exclude-standard | fdfind --type f --type 1 ${FD_OPTIONS}"
export FZF_ALT_C_OPTS="--preview 'tree --dirsfirst {}' --preview-window=right:50% --height=75%"
export FZF_CTRL_T_OPTS=" \
  --preview='[[ \$(file --mime {}) =~ binary ]] && echo {} is a binary file || (bat ---style=numbers --color=always {} || cat {}) 2> /dev/null | head -300' \
  --preview-window='right:50%'"
export FZF_CTRL_T_COMMAND="fdfind --type f ${FD_OPTIONS}"
export FZF_ALT_C_COMMAND="fdfind --type d ${FD_OPTIONS}"

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

path+=("${HOME}/.config/composer/vendor/bin")
path+=("${HOME}/.local/bin")
export PATH

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh
