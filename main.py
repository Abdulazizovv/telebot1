from telebot import TeleBot
from telebot import types
from environs import Env
from datetime import datetime
from menu import main_menu_kb, data, show_category_kb

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN", None)



if not BOT_TOKEN:
    raise ValueError("BOT token sozlanmagan")

bot = TeleBot(token=BOT_TOKEN)

@bot.message_handler(commands=["start"])
def start_handler(message: types.Message):
    today = datetime.now().date().strftime("%d-%m-%Y")

    greeting_text = f"""
Assalomu alaykum! Oshxonamizga xush kelibsiz!
Bugun {today}.
Menyu bilan tanishing👇
    """

    bot.send_message(
        chat_id=message.chat.id,
        text=greeting_text,
        reply_markup=main_menu_kb()
    )



@bot.message_handler(func = lambda message: message.text in data["kategoriyalar"][0])
def get_category(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text=f"{message.text} kategoriyasidagi taomlar:",
        reply_markup=show_category_kb(message.text)
    )




if __name__ == "__main__":
    print("Bot ishga tushdi")
    bot.infinity_polling()