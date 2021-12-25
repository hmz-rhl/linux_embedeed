#!/bin/bash
#echo ${1##*.}
rm $HOME/projet4/img*
wget -c $1 -O img -P $HOME/projet4/script/
#.${1##*.}
