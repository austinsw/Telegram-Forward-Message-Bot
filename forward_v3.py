# Logger 3.0
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, ConversationHandler)
import telegram
import logging

admins = [1231234567,1231234560]  # id or username
targets = [1239876543]  # id or username
targetGroup = "targetChannel"   ##### 1. username (case-sensitive) or id
receiver = -1002101555321       ##### 2. only id
telegram_token = "1234567890:BOttoKeN"   ##### 3. bot token

def listToFile(fileName, ls):
    with open(fileName, 'w') as filehandle:
        filehandle.writelines("%s," % data for data in ls)

def fileToList(fileName):
    with open(fileName, 'r') as filehandle:
        a = filehandle.read()
    a = a.split(',')
    a.pop()
    b = []
    for element in a:
        try:
            b.append(int(element))
        except:
            b.append(element)
    print(b)
    return b

targets = fileToList("targets.txt")
admins = fileToList("admins.txt")

def index(ID, L):
    try:
        return(L.index(ID))
    except:
        return -1

def addTarget(ID):
    pos = index(ID, targets)
    if pos != -1:
        print("user found")
        return pos
    else:
        targets.append(ID)
        listToFile("targets.txt", targets)
        return -1

updater = Updater(token=telegram_token, use_context=True);
dispatcher = updater.dispatcher;
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO);

def add(update, context):
    for admin in admins:
        if admin == update.effective_chat.id or admin == update.effective_chat.username:
            userIDs = context.args
            if len(userIDs) != 0:
                for userID in userIDs:
                    try:
                        userID = int(userID)
                    except:
                        pass
                    isInSystem = addTarget(userID)
                    if isInSystem == -1:
                        context.bot.send_message(chat_id=update.effective_chat.id, text=str(userID) + " added.")
                    else:
                        context.bot.send_message(chat_id=update.effective_chat.id,
                                                 text=str(userID) + " is already in system.")
                print(targets)
                return
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Plz put the username/ id you want to add after the command.")
            return
    context.bot.send_message(chat_id=update.effective_chat.id, text="Not authorized.")
    print("add, not authorized")
add_handler = CommandHandler('add', add)
dispatcher.add_handler(add_handler)

def rm(update, context):
    for admin in admins:
        if admin == update.effective_chat.id or admin == update.effective_chat.username:
            userIDs = context.args
            if len(userIDs) != 0:
                for userID in userIDs:
                    try:
                        userID = int(userID)
                    except:
                        pass
                    idx = index(userID, targets)
                    if idx != -1:
                        del targets[idx]
                        listToFile("targets.txt", targets)
                        context.bot.send_message(chat_id=update.effective_chat.id,
                                                 text=str(userID) + " deleted.")
                    else:
                        context.bot.send_message(chat_id=update.effective_chat.id,
                                                 text=str(userID) + " not found.")
                return
            context.bot.send_message(chat_id=update.effective_chat.id,
                                         text="Plz put the username/ id you want to remove after the command.")
            return
    context.bot.send_message(chat_id=update.effective_chat.id, text="Not authorized.")
    print("rm, not authorized")
rm_handler = CommandHandler('rm', rm)
dispatcher.add_handler(rm_handler)

def list(update, context):
    for admin in admins:
        if admin == update.effective_chat.id or admin == update.effective_chat.username:
            message = ""
            if len(targets) != 0:
                for target in targets:
                    message = message + str(target)
                    message = message + ' '
                message = message[:-1]
                context.bot.send_message(chat_id=update.effective_chat.id, text=message)
                return
            context.bot.send_message(chat_id=update.effective_chat.id, text="No user.")
            return
    context.bot.send_message(chat_id=update.effective_chat.id, text="Not authorized.")
    print("list, not authorized")
list_handler = CommandHandler('list', list)
dispatcher.add_handler(list_handler)

def delAll(update, context):
    for admin in admins:
        if admin == update.effective_chat.id or admin == update.effective_chat.username:
            targets.clear()
            listToFile("targets.txt", targets)
            context.bot.send_message(chat_id=update.effective_chat.id, text="Deleted all.")
            return
    context.bot.send_message(chat_id=update.effective_chat.id, text="Not authorized.")
    print("delAll, not authorized")
delAll_handler = CommandHandler('delAll', delAll)
dispatcher.add_handler(delAll_handler)

def help(update, context):
    for admin in admins:
        if admin == update.effective_chat.id or admin == update.effective_chat.username:
            message = "/add {id/usernames} \n/rm {id/usernames} \n/list \n/delAll"
            context.bot.send_message(chat_id=update.effective_chat.id, text=message)
            return
    #context.bot.send_message(chat_id=update.effective_chat.id, text="You are not authorized.")
    print("help, not authorized")
help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

def mesgs_hand(update, context):
    if targetGroup == update.effective_chat.id or targetGroup == update.effective_chat.username:
        for target in targets:
            if target == update.effective_user.id or target == update.effective_user.username:
                context.bot.forward_message(chat_id=receiver,
                                            from_chat_id=update.effective_chat.id,
                                            message_id=update.message.message_id)
                return
messages_handler = MessageHandler(Filters.update, mesgs_hand)
dispatcher.add_handler(messages_handler)

def bot():
    updater.start_polling();

if __name__ == "__main__":
    bot();
