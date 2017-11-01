#!/bin/bash
if [ ! -d "$HOME/.eksiautoentry" ]; then
  mkdir "$HOME/.eksiautoentry"
fi
cp "config.JSON" "$HOME/.eksiautoentry"
cp "pp.py" "$HOME/.eksiautoentry"

cat <(crontab -l) <(echo "0 * * * * python $HOME/.eksiautoentry/pp.py") | crontab -

echo "Installed under folder --> $HOME/.eksiautoentry"
echo "DONE !"
