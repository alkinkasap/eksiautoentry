Supply the login(username,password), entry and baslik information and run
from the terminal. username should be the mail address and the password should be user-known password.

$python pp.py

Requires mechanize module (python 2.x)

To install--> $sudo pip install mechanize

If you would like to generate a cron job, you can run setup.sh from the terminal to set-up a cron job for each hour of each day.(The script will check every hour if an entry is deleted from a header.)

If you want to modify the configuration file, uninstall first, change the config file and finally install again.

To uninstall, just run the uninstall.sh

To bypass the captcha check, first log-in from your original browser. After logging in successfully the script will be able to log-in as well.
