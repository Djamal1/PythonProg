import telebot

TOKEN = "482065065:AAEfH4lf9Tcea8LdpiPlSRHMofZsQKiSC7Q"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(regexp = "ЛОЛ")
def checker (message):
	bot.send_message(message.chat.id, "STPU")

our_kb = telebot.types.ReplyKeyboardMarkup()
our_kb.row("1 + 1 = ?", "LOL")
our_kb.row("0", "+", "-")

@bot.message_handler(commands = ['start'])
def start_kb(message):
	bot.send_message(message.chat.id, "Помидорки вкусняя!", reply_markup = our_kb)


if __name__ == "__main__":
	bot.polling()