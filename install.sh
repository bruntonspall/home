#!/bin/sh
dir=$(dirname $0)
rm ~/.bashrc ~/.bash_profile ~/.bash_logout
for f in .bashrc .bash_profile .bash_logout bin share etc var .muttrc 
do
    ln -s $dir/$f $HOME/
done
cd $dir
git submodule update --init
ln -s etc/dotvim ~/.vim
etc/dotvim/install.sh
