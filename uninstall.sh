#!/bin/bash
if [ -d "$HOME/.eksiautoentry" ]; then
  rm -rf "$HOME/.eksiautoentry"
fi
echo "Make sure to remove the cron job that is entered with the setup string."
echo "The string combination is --> 0 * * * * python $HOME/.eksiautoentry/pp.py"
