# setup git
alias gb="git branch"
alias gst="git status -uno"
alias gco="git checkout"
alias ga="git add"
alias gd="git diff"
alias gcmsg="git commit -m"
alias glog="git log --oneline --decorate"


# cleanup .DS_Store
alias ds="find . -type f -name '.DS_Store'"


# cleanup docker
alias dclean="docker ps -aq | xargs docker rm -f;docker images -q | xargs docker rmi"
