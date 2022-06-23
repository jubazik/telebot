from api import bot

@bot.message_handler(commands=['start'])
def welcom(message):
    sri = open('welcom.webp', 'rb')
    bot.send_sticker(message.chat.id, sri)

    bot.send_message(message.chat.id,
                     "Ты уверен что хочешь сюда? \n я бот созданный чтобы быть подоподным кроликом", parse_mode='html')


@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, message.text)
