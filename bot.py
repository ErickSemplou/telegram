import os
import telebot

BOT_TOKEN = "7905878460:AAFMs94DlUaDhRRr8XEPn-UMxFrOow72xIw"
GROUP_CHAT_ID = -1002466933691

bot = telebot.TeleBot(BOT_TOKEN)

PETITIONS = [
    "1. 🇺🇦 Роман Кінаш 🔥🔥🔥\nhttps://petition.president.gov.ua/petition/245246",
    "2. 🇺🇦 Антон Листопад\nhttps://petition.president.gov.ua/petition/245654",
    "3. 🇺🇦 Василь Клекач\nhttps://petition.president.gov.ua/petition/244660",
    "4. 🇺🇦 Олег Гнед\nhttps://petition.president.gov.ua/petition/244852",
    "5. 🇺🇦 Юрій Бузіков 🔥🔥🔥\nhttps://petition.president.gov.ua/petition/244036",
    "6. 🇺🇦 Богдан Танасюк 🔥🔥🔥\nhttps://petition.president.gov.ua/petition/243292",
    "7. 🇺🇦 Руслан Валько 🔥🔥🔥\nhttps://petition.president.gov.ua/petition/244108",
    "8. 🇺🇦 Юрій Чмут 🔥🔥🔥\nhttps://petition.president.gov.ua/petition/243630"
]

@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привіт! Ось список петицій, які потрібно підписати:")
    for p in PETITIONS:
        bot.send_message(message.chat.id, p)
    bot.send_message(message.chat.id, "Після того, як підпишеш усі петиції, напиши: ✅ Я підписав")

@bot.message_handler(func=lambda message: "✅" in message.text or "підписав" in message.text.lower())
def accept_signature(message):
    bot.reply_to(message, "Дякуємо! Тепер ти можеш додати свою петицію. Надішли посилання:")

@bot.message_handler(func=lambda message: "http" in message.text and "petition" in message.text)
def forward_petition(message):
    bot.send_message(GROUP_CHAT_ID, f"👤 Користувач @{message.from_user.username or message.from_user.first_name} додав петицію:{message.text}")
    bot.reply_to(message, "✅ Дякуємо! Петицію надіслано в групу.")

bot.infinity_polling()
