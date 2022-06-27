from api import bot, os, time


@bot.message_handler(commands=['start'])
def welcome(messange):
    file = open('welcom.webp', 'rb')
    bot.send_sticker(messange.chat.id, file)
    bot.send_message(messange.chat.id, "Привет дорогой ты мой ")


@bot.message_handler(commands=['test'])
def file_file_ids(message):
    for file in os.listdir('misic/'):
        if file.split('.')[-1] == 'ogg':
            f = open('music/' + file, 'rb')
            msg = bot.send_voice((message.chat.id, f, None))
            bot.send_message(message.chat.id, msg.voice.file_id, reply_to_message_id=msg.message_id)
        time.sleep(3)


bot.polling(none_stop=True)  # код для того что бы запустить сам бот
