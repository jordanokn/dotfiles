# OrbStack integration (оставлено, если нужно)
source ~/.orbstack/shell/init.zsh 2>/dev/null || :

# Инициализация Homebrew
eval "$(/opt/homebrew/bin/brew shellenv)"

# Настройка pyenv
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"

# Настройка autojump (если установлен)
if [[ -s "$(brew --prefix autojump)/etc/profile.d/autojump.sh" ]]; then
  source "$(brew --prefix autojump)/etc/profile.d/autojump.sh"
fi

export PATH="/opt/homebrew/opt/qt@5/bin:$PATH"

alias git-clean-branches='git branch | grep -v "^*" | xargs git branch -D'

plugins=(git)
ZSH_THEME="robbyrussell" 

act() {
    eval "$(poetry env activate)"
}

p() {
    local script="$1"
    if [[ "$script" != *.py ]]; then
        script="${script}.py"
    fi

    python3 "$script" "${@:2}"
}


## завершение всех рабочий програм
alias kall='python3 /Users/georgeknyazyan/Documents/customScripts/kill.py'

pipe(){
    local scripts="$1"
    python3 /Users/georgeknyazyan/Documents/customScripts/reduce_utils.py "$scripts"
}

nowork(){
    pipe "kill,open_friends"
}

alias mycom='/Users/georgeknyazyan/Documents/customScripts/workflow_git.sh'

