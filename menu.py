from telebot.types import ReplyKeyboardMarkup, KeyboardButton


data = {
    "kategoriyalar": [
        {
            "Milliy taomlar": [
                ["Osh", 17000],
                ["Norin", 35000],
                ["Sho'rva", 20000],

            ],
            "Fast-Food": [
                ["Gamburger", 25000],
                ["Lavash", 40000]
            ],
            "Ichimliklar": [
                ["Pepsi 1L", 12000],
                ["Fanta 1.5L", 15000]
            ]
        }
    ]
}


def main_menu_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for i in data["kategoriyalar"][0]:
        btn = KeyboardButton(text=i)
        kb.row(btn)
    return kb


def show_category_kb(category_name):
    items = data["kategoriyalar"][0][category_name]
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for i in items:
        btn = KeyboardButton(f"{i[0]} - {i[1]} so'm")
        kb.add(btn)

    back_btn = KeyboardButton("Orqaga⬅️")
    kb.add(back_btn)
    return kb