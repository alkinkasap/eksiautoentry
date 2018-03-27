#!/bin/bash

pip -V >> /dev/null 2>&1
if (( $? == 127 ));then
  sudo apt-get update && sudo apt-get -y upgrade
  sudo apt-get install python-pip
fi

python -c "import mechanize" >> /dev/null 2>&1

if (( $? == 1 ));then
  sudo pip install --upgrade pip
  sudo pip install mechanize
fi

if [ ! -d "$HOME/.eksiautoentry" ]; then
  mkdir "$HOME/.eksiautoentry"
fi
cp "config.JSON" "$HOME/.eksiautoentry"
cp "pp.py" "$HOME/.eksiautoentry"

cat <(crontab -l) <(echo "0 * * * * python $HOME/.eksiautoentry/pp.py $HOME/.eksiautoentry/config.JSON >> $HOME/.eksiautoentry/generated.log")  | crontab -

echo "Installed under folder --> $HOME/.eksiautoentry"
echo "DONE !"
