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
    bot.send_message(
        chat_id=message.chat.id,
        text=f"Assalomu alaykum! {message.from_user.full_name}"
    )


if __name__ == "__main__":
    print("Bot ishga tushdi")
    bot.infinity_polling()