# Telegram Forward Message Bot
A Telegram bot for forwarding specific users' messages to a desginated channel, made in 2021

## Run
The code is run on Python 3. If Python 3 is not your default interpreter (say Python 2.7), you will probably need `pip3 install`, and `python3` command to install the packages and run the .py file.

`python forward_v3.py` to run the file: It was originally created on PyCharm, but can be put on a virtual machine, say Google Cloud for 24/7 usesage.

## forward_v3.py

Although `admins` and `targets` variables are pre-defined in the code, the admins and targets details are actually stored in ***admins.txt*** and ***targets.txt***. If you wish to add or remove admins, make the changes on ***admins.txt***. Although you can make the changes on ***targets.txt*** manually as well, it is not advised as you can change the target details through Telegram...(see below)

### Set up the basics:
In the code...
- `targetGroup` Insert the group to monitor: id or username (case-sensitive)
- `receiver` Insert the group for receiving messages: only id
- `telegram_token` Insert the bot token

### Commands in Telegram
For ease of use, Telegram is used as an interface to interact with the code, by sending commands to the bot. And only the admins registered in ***admins.txt*** can use these commands:
- `/add {id/usernames}` Adding new people to ***targets.txt***. When adding multiple targets, a space bar ` ` between targets will do, e.g. `/add Amy123 123124534 Peter321`. 
- `/rm {id/usernames}` Removing that usersname (id) from ***targets.txt***.
- `/list` Listing our every target's usersname (id)
- `/delAll` Erase everything on ***targets.txt***. Would recommend using the `/list` to keep a back up of the personnels first.
- `/help` Listing out the above 4 commands

Telegram user / group chat id can be checked by Nicegram or by other means.

## forward_v1.py

It is the version 1 of the code, uses the telethon package. If the package is not already installed, run the code to install the package: `pip install telethon`

API_ID and API_HASH values can be retrieved from https://my.telegram.org.
