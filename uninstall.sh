#!/bin/bash
if [ -d "$HOME/.eksiautoentry" ]; then
  rm -rf "$HOME/.eksiautoentry"
fi

search_string="0 * * * * python $HOME/.eksiautoentry/pp.py $HOME/.eksiautoentry/config.JSON >> $HOME/.eksiautoentry/generated.log"
crontab -l > tempcron
ctr=1
while IFS='' read -r line || [[ -n "$line" ]]; do
  if [ "$search_string" == "$line" ]; then
    sed -i.bak "${ctr}d" tempcron
  fi
  ((ctr++))
done < tempcron

crontab tempcron
rm tempcron
rm tempcron.bak

echo "DONE !"
