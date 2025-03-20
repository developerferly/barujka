import telebot
import time
import re

TOKEN = "7884258399:AAEjJYL3eAvnTBkl-VQy_4ABr139IYBFqL0"
bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

#
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
        bot.reply_to(message, welcome_text)

#/rules
cooldowns = {}
COOLDOWN_TIME = 5

@bot.message_handler(commands=['rules'])
def send_rules(message):
    user_id = message.from_user.id
    current_time = time.time()

    if user_id in cooldowns and current_time - cooldowns[user_id] < COOLDOWN_TIME:
        return

    cooldowns[user_id] = time.time()

    rules_text = (
        "⬇ *CHAT FOR COMMUNICATION / RESSELLING* | *ЧАТ ДЛЯ ОБЩЕНИЯ / ПЕРЕПРОДАЖ* ⬇\n\n"
        "🔗  [t.me/barujka_chat](t.me/barujka_chat)\n"
        "🔗  [t.me/barujka_chat](t.me/barujka_chat)\n"
        "🔗  [t.me/barujka_chat](t.me/barujka_chat)\n\n"
        "⬆ *CHAT FOR COMMUNICATION / RESSELLING* | *ЧАТ ДЛЯ ОБЩЕНИЯ / ПЕРЕПРОДАЖ* ⬆\n\n"
        "🧛‍♂️ RULES | ПРАВИЛА ЛУЧШЕГО ЧАТА\n\n"
        "✅ *1.* Запрещено многочисленные оскорбления, провокации и любые другие способы нарушения адекватного общения. - мут/пред (в зависимости от ситуации) \n\n"
        "✅ *2.* Запрещено обсуждение наркотиков, терроризма, призывы к суициду/причинения вреда самому себе, а также демонстрация и публикация материалов с запрещённой символикой, сексуальным или другим неподобающим контентом - пред на 7д, после бан\n\n"
        "✅ *3.* Спам, спам командами, флуд, реклама, пересыл соо с ТГК (без ведома админов) - пред, после бан\n\n"
        "✅ *4.* Запрещено разжигание национальной розни, любые формы дискриминации, сексизм, а также враждебное отношение к религиозным группам и людям с ограниченными возможностями - мут\n\n"
        "✅ *5.* Запрещены твинки (вторые аккаунты), если до этого ваш аккаунт был в блокировке в чате - бан твинка\n\n"
        "✅ *6.* Постинг своих вещей с указанием канала запрещён. (Бесплатная реклама каналов отсутствует) - пред, после бан\n\n"
        "@barujka  @barujka  @barujka  @barujka  @barujka  @barujka"
    )
    bot.send_message(message.chat.id, rules_text, parse_mode="Markdown")

#/dm
@bot.message_handler(commands=['dm'])
def send_dm(message):
    user_id = message.from_user.id
    current_time = time.time()

    if user_id in cooldowns and current_time - cooldowns[user_id] < COOLDOWN_TIME:
        return  # Просто игнорируем команду, не отправляя ничего

    cooldowns[user_id] = time.time()

    dm_text = (
        "🛒 Если у вас есть вопросы или вы хотите сделать покупку, напишите мне в дм.\n\n"
        "⬇ MY DIRECT MESSAGE | МОЙ ДМ ⬇\n\n"
        "@barujka\n"
        "@barujka\n"
        "@barujka\n\n"
        "⬆ MY DIRECT MESSAGE | МОЙ ДМ ⬆\n\n"
    )
    bot.send_message(message.chat.id, dm_text, parse_mode="Markdown")

#/ban
authorized_users = [5209450978, 6668382884, -1002066320402]

def escape_markdown(text):
    return re.sub(r'([_*`\[\]()~>#+\-=|{}.!])', r'\\\1', text)

@bot.message_handler(commands=['ban'])
def ban_user(message):
    if message.from_user.id in authorized_users:
        if message.reply_to_message:
            user_to_ban = message.reply_to_message.from_user.id
            user_to_ban_username = message.reply_to_message.from_user.username

            try:
                # Баним пользователя
                bot.kick_chat_member(message.chat.id, user_to_ban)

                escaped_username = escape_markdown(user_to_ban_username)
                escaped_user_id = escape_markdown(str(user_to_ban))

                sent_message = bot.send_message(
                    message.chat.id,
                    f"Пользователь: @{escaped_username} |\nID `{escaped_user_id}`, был *заблокирован*.",
                    parse_mode="Markdown"
                )
            except Exception as e:
                # Обработка ошибки
                error_message = bot.send_message(message.chat.id, f"")
                time.sleep(3)
                # Удаляем сообщение с ошибкой
                bot.delete_message(message.chat.id, message.message_id)
                bot.delete_message(message.chat.id, error_message.message_id)
        else:
            sent_message = bot.send_message(
                message.chat.id,
                "Ответьте на сообщение *пользователя*,\nкоторого желаете забанить.",
                parse_mode="Markdown"
            )
            time.sleep(5)
            # Удаляем сообщение с инструкцией
            bot.delete_message(message.chat.id, message.message_id)
            bot.delete_message(message.chat.id, sent_message.message_id)
    else:
        error_message = "❌ Команда доступна только для владельца чата."
        sent_message = bot.send_message(message.chat.id, error_message)
        time.sleep(3)
        # Удаляем сообщение с ошибкой
        bot.delete_message(message.chat.id, message.message_id)
        bot.delete_message(message.chat.id, sent_message.message_id)

#
allowed_users = [5209450978, 6668382884, -1002066320402]

#/unban
@bot.message_handler(commands=['unban'])
def unban(message):
    if message.from_user.id in allowed_users:
        try:
            user_id = int(message.text.split()[1])
            user_name = bot.get_chat_member(message.chat.id, user_id).user.username
            bot.unban_chat_member(message.chat.id, user_id)
            bot.send_message(
                message.chat.id,
                f"Пользователь: @[{user_name}](tg://user?id={user_id}), был\n*разблокирован*.",
                parse_mode="Markdown")
            time.sleep(3)
            bot.delete_message(message.chat.id, message.message_id)
        except Exception as e:
            bot.send_message(message.chat.id, f"❌ Обязательно введите ID пользователя.")

        except (IndexError, ValueError):
            error_msg = bot.send_message(message.chat.id, "❌ Не правильный ID пользователя.")
            time.sleep(3)
            bot.delete_message(message.chat.id, error_msg.message_id)
            time.sleep(3)
            bot.delete_message(message.chat.id, message.message_id)
    else:
        error_message = "❌ Команда доступна только для владельца чата."
        sent_message = bot.send_message(message.chat.id, error_message)
        time.sleep(3)
        bot.delete_message(message.chat.id, message.message_id)
        bot.delete_message(message.chat.id, sent_message.message_id)

bot.polling(none_stop=True)
