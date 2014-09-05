#!/usr/bin/env sh

git clone https://github.com/rgrannell1/git-join
cd git-join
echo alias git-join=\'$(pwd -P)/lib/git-join.sh\' >> ~/.bashrc && . ~/.bashrc
