from tkinter.constants import COMMAND

import telebot
import time

TOKEN = "7884258399:AAEjJYL3eAvnTBkl-VQy_4ABr139IYBFqL0"
bot = telebot.TeleBot(TOKEN, parse_mode="HTML")


#WELCOME_CHAT_BARUJKA
@bot.message_handler(content_types=['new_chat_members'])
def welcome_new_member(message):
    for new_member in message.new_chat_members:
        # Получаем username или first_name участника
        user_mention = f"@{new_member.username}" if new_member.username else f"<b>{new_member.first_name}</b>"

        # Приветственное сообщение с тегом и ссылкой
        welcome_text = (
            f"👋 Приветствуем, {user_mention}! Ознакомьтесь с правилами, чтобы избежать недоразумений.\n\n"
            f"Нажмите на <a href='https://t.me/+qZuZbxptYWkwY2Yy'>ссылку</a>, чтобы перейти в телеграмм канал <a href='https://t.me/+qZuZbxptYWkwY2Yy'>Хижины барыжки</a>!\n\n"
        )

        # rеплей на сообщение о вступлении с тегом и ссылкой
        bot.reply_to(message, welcome_text)


#/rules
cooldowns = {}

#кулдаун
COOLDOWN_TIME = 5

@bot.message_handler(commands=['rules'])
def send_rules(message):
    user_id = message.from_user.id
    current_time = time.time()

    if user_id in cooldowns and current_time - cooldowns[user_id] < COOLDOWN_TIME:
        return

    cooldowns[user_id] = time.time()

#сообщение
    rules_text = (
        "⬇ *CHAT FOR COMMUNICATION / RESSELLING* | *ЧАТ ДЛЯ ОБЩЕНИЯ / ПЕРЕПРОДАЖ* ⬇\n\n"
        "🔗 [t.me/barujka_chat](t.me/barujka_chat)\n"
        "🔗 [t.me/barujka_chat](t.me/barujka_chat)\n"
        "🔗 [t.me/barujka_chat](t.me/barujka_chat)\n\n"
        "⬆ *CHAT FOR COMMUNICATION / RESSELLING* | *ЧАТ ДЛЯ ОБЩЕНИЯ / ПЕРЕПРОДАЖ* ⬆\n\n"
        "🧛‍♂️ *RULES | ПРАВИЛА ЛУЧШЕГО ЧАТА*\n\n"
        "✅ *1.* Запрещено многочисленные оскорбления, провокации и любые другие способы нарушения адекватного общения. - мут/пред (в зависимости от ситуации) \n\n"
        "✅ *2.* Запрещено обсуждение наркотиков, терроризма, призывы к суициду/причинения вреда самому себе, а также демонстрация и публикация материалов с запрещённой символикой, сексуальным или другим неподобающим контентом - пред на 7д, после бан\n\n"
        "✅ *3.* Спам, спам командами, флуд, реклама, пересыл соо с ТГК (без ведома админов) - пред, после бан\n\n"
        "✅ *4.* Запрещено разжигание национальной розни, любые формы дискриминации, сексизм, а также враждебное отношение к религиозным группам и людям с ограниченными возможностями - мут\n\n"
        "✅ *5.* Запрещены твинки (вторые аккаунты), если до этого ваш аккаунт был в блокировке в чате - бан твинка\n\n"
        "✅ *6.* Постинг своих вещей с указанием канала запрещён. (Бесплатная реклама каналов отсутствует) - пред, после бан"
    )
    bot.send_message(message.chat.id, rules_text, parse_mode="Markdown")

#команда /дм
@bot.message_handler(commands=['dm'])
def send_dm(message):
    user_id = message.from_user.id
    current_time = time.time()

    if user_id in cooldowns and current_time - cooldowns[user_id] < COOLDOWN_TIME:
        return  # Просто игнорируем команду, не отправляя ничего

    cooldowns[user_id] = time.time()

#сообщение
    dm_text = (
        "🛒 Если у вас есть вопросы или вы хотите сделать покупку, напишите мне в дм.\n\n"
        "⬇ MY DIRECT MESSAGE | МОЙ ДМ ⬇\n\n"
        "@barujka\n"
        "@barujka\n"
        "@barujka\n\n"
        "⬆ MY DIRECT MESSAGE | МОЙ ДМ ⬆\n\n"
    )
    bot.send_message(message.chat.id, dm_text, parse_mode="Markdown")


bot.polling(none_stop=True)
