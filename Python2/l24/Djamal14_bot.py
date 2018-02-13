import telebot

TOKEN = "482065065:AAEfH4lf9Tcea8LdpiPlSRHMofZsQKiSC7Q"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands = ['start'])
@bot.message_handler(commands = ['commands'])
@bot.message_handler(commands = ['info_bot'])

def answer(message):
	if message.text == "/start":
		bot.send_message(message.chat.id, "Привет! Ты начал разговор с ботом, напиши ему что-то!")
	if message.text == "/commands":
		bot.send_message(message.chat.id, "/start, /commands, /info_bot")

@bot.message_handler(func = lambda message: True)

def say_smth(message):
	if message.text == "Привет":
		bot.send_message(message.chat.id, "Дратути")
	elif message.text == "Ты человек?":
		bot.reply_to(message, "Я робот!!!")
	elif message.text == "Как дела?":
		bot.reply_to(message, "Отлично!!")
	elif message.text == "Что делаешь?":
		bot.reply_to(message, "С тобой разговариваю!")
	elif message.text == "Ты робот?":
		bot.reply_to(message, "Нет я многофункциональная машина!")
	elif message.text == "Пока":
		bot.reply_to(message, "Пока! Шутка!")
	elif message.text == "Ты тупой?":
		bot.reply_to(message, "Но уж поумнее тебя!!!!")
	elif message.text == "Как тебя зовут?":
		bot.reply_to(message, "Pask")
	elif message.text == "Почему тебя зовут Pask?":
		bot.reply_to(message, "Pask - от слова паскаль, если ты знаешь физику, то ты знаешь.")
	elif message.text == "Кто твой создатель?":
		bot.reply_to(message, "Djamal")
	elif message.text == "Дурак":
		bot.reply_to(message, "Мне же обидно, хватит! :(")
	elif message.text == "Дибил":
		bot.reply_to(message, "Хватит осёл вонючий!!!!")
	else:
		bot.send_message(message.chat.id, "Я не понимаю что ты говоришь! Или в моей базе данных нет данного слова! ((((")

if __name__ == "__main__":
	bot.polling()