#!/bin/sh
dir=$(dirname $0)
rm ~/.bashrc ~/.bash_profile ~/.bash_logout
for f in $(ls -1A $dir); do
  if [ ".git" != "$f" ]; then
    ln -s $dir/$f $HOME/
  fi
done
