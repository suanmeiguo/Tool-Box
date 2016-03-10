# setup git
alias gb="git branch"
alias gst="git status -uno"
alias gco="git checkout"
alias ga="git add"
alias gd="git diff"
alias gcmsg="git commit -m"
alias glog="git log --oneline --decorate"


# setup virtual environment
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh


# JAVA
export JAVA_HOME="$(/usr/libexec/java_home -v 1.8)"


# AWS
export AWS_ACCESS_KEY_ID=<key>
export AWS_SECRET_ACCESS_KEY=<secret>
export AWS_DEFAULT_REGION=<region>


# python3
alias python=python3


# cleanup .DS_Store
alias ds="find . -type f -name '.DS_Store'"


# cleanup docker
alias dclean="docker ps -aq | xargs docker rm -f;docker images -q | xargs docker rmi"


