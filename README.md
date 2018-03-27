Supply the login(username,password), entry and baslik information and run
from the terminal. username should be the mail address and the password should be user-known password.

$python pp.py config.JSON

Requires mechanize module (python 2.x)

To install--> ./setup.sh

If you run setup.sh from the terminal you would set-up a cron job for each hour of each day.(The script will check every hour if an entry is deleted from a header.)

If you want to modify the configuration file, uninstall first, change the config file and finally install again.

To uninstall--> ./uninstall.sh

To bypass the captcha check, first log-in from your original browser. After logging in successfully the script will be able to log-in as well.
