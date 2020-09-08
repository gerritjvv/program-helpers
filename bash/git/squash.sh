#!/usr/bin/env bash

# rebase branch
# use rebase 3
function rebase() {
  I=$1
  git reset --soft HEAD~$I
  echo "do a git commit and git push --force"
}


function count_commits() {
  MASTER="$1"
  BRANCH="$2"
  git rev-list --left-right --count "$MASTER"..."$BRANCH"
}


# count the number of commits from when the branch was created from master
count_commits master `git branch --show-current`