from telebot import TeleBot
from telebot import types
from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN", None)

if not BOT_TOKEN:
    raise ValueError("BOT token sozlanmagan")

bot = TeleBot(token=BOT_TOKEN)

@bot.message_handler(commands=["start"])
def start_handler(message: types.Message):
    inline_menu = types.InlineKeyboardMarkup()
    inline_menu.add(
        types.InlineKeyboardButton("USD", callback_data="select_usd"),
        types.InlineKeyboardButton("RUB", callback_data="select_rub"),
    )

    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)

    menu.row(
        types.KeyboardButton("USD"),
        types.KeyboardButton("RUB")
    )


    bot.send_message(
        chat_id=message.chat.id,
        text=f"Assalomu alaykum! {message.from_user.full_name}",
        reply_markup=inline_menu
    )


@bot.message_handler(func=lambda message: message.text == "USD")
def usd_handler(message: types.Message):
    bot.send_message(message.chat.id, "1$ = 11800 so'm")


@bot.message_handler(func=lambda message: message.text == "RUB")
def rub_handler(message: types.Message):
    bot.send_message(message.chat.id, "1 rubl = 160 so'm")



if __name__ == "__main__":
    print("Bot ishga tushdi")
    bot.infinity_polling()