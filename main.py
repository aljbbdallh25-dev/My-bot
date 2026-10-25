import os
import telebot

BOT_TOKEN = os.environ.get("BOT_TOKEN")
WALLET = "TDUdh4awmPgcvYRBaxZUEemnCm8fKstZmX"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, "Bot is working ✅\nSend amount like: 100")

@bot.message_handler(func=lambda m: True)
def all_msg(m):
    try:
        amount = float(m.text)
        total = amount * 1.03
        bot.send_message(m.chat.id, f"Amount: {amount}\nTotal: {total:.2f}\nSend to TRC20:\n{WALLET}")
    except:
        bot.send_message(m.chat.id, "Send number only, ex: 100")

bot.infinity_polling()
