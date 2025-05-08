import telebot
import time
import re

TOKEN = "7884258399:AAEjJYL3eAvnTBkl-VQy_4ABr139IYBFqL0"
bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

#
@bot.message_handler(content_types=['new_chat_members'])
def welcome_new_member(message):
    for new_member in message.new_chat_members:
        user_mention = f"@{new_member.username}" if new_member.username else f"<b>{new_member.first_name}</b>"

        welcome_text = (
            f"👋 Приветствуем, {user_mention}! Ознакомьтесь с правилами, чтобы избежать недоразумений.\n\n"
            f"<b>НОВЫЙ ТГК ХИЖИНЫ БАРЫЖКИ!</b>\n\n"
            f"БАРЫЖКА ОТКРЫЛ НОВЫЙ ТГК ТАК КАК ПРОШЛЫЙ СНЕСЛИ, БУДЕТ МНОЖЕСТВО ИНТЕРЕСНЫХ ВЕЩЕЙ!\n\n"
            f"<a href='https://t.me/+BqTQRpuGjTQ4Y2Uy'>ТОЛЬКО ГОДНЫЕ АЙТЕМЫ И ЧЕСТНЫЙ РЕСЕЙЛ</a>"
        )
        bot.reply_to(message, welcome_text, parse_mode='HTML')


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
        return

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

#/info
@bot.message_handler(commands=['info'])
def send_info(message):
    user_id = message.from_user.id
    current_time = time.time()

    if user_id in cooldowns and current_time - cooldowns[user_id] < COOLDOWN_TIME:
        return

    cooldowns[user_id] = time.time()

    info_text = (
        "ИНФОРМАЦИОННЫЙ БЛОК / INFORMATION BLOCK\n\n"
        "*⬇ СОЦИАЛЬНЫЕ СЕТИ / SOCIAL MEDIA⬇*\n\n"
        "📎  ТЕЛЕГРАМ КАНАЛ / TELEGRAM CHANNEL:  \n"
        "       [https://t.me/+BqTQRpuGjTQ4Y2Uy](https://t.me/+BqTQRpuGjTQ4Y2Uy)\n\n"
        "📎  НОВОСТИ БАРЫЖКИ / BARUJKA NEWS: \n"
        "       [@barujka_news](https://t.me/barujka_news)\n\n"
        "📎  ИНСТАГРАМ / INSTAGRAM: \n"
        "       [barujka.store](https://www.instagram.com/barujka.store)\n\n"
        "📎  ТИК ТОК / TIKTOK: \n"
        "       [@barujka](https://www.tiktok.com/@barujka.store)\n\n\n"
        "*⬆ СОЦИАЛЬНЫЕ СЕТИ / SOCIAL MEDIA⬆*\n\n\n"
        "*⬇ КОМАНДНОЕ МЕНЮ / COMMAND MENU⬇*\n\n"
        "/info - Отображает основную информацию и полезные ссылки.\n"
        "/dm - Если у вас есть вопросы или вы хотите сделать покупку, напишите мне в дм.\n\n"
        "*⬆ КОМАНДНОЕ МЕНЮ / COMMAND MENU⬆*\n\n\n"
        "*Оригинальные* брендовые вещи (NEW & Б/У)\n"
        "Вся продукция проверяется *лично*\n"
        "Мы *не* размещаем реплики или *запрещённый* контент\n"
        "👉 *ЛИЧНОЕ СООБЩЕНИЕ / DIRECT MESSAGE*: @barujka"
    )

    bot.send_message(message.chat.id, info_text, parse_mode="Markdown")

    time.sleep(10)
    bot.delete_message(message.chat.id, message.message_id)

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

#autoedeleted
FORBIDDEN_WORDS = ["PRICE", "pRice", "pRICe", "pRICE", "pRice", "prIce", "priCe", "pricE", "PRice", "PRIce", "PRICe", "price"]

# ID
ALLOWED_CHANNEL_IDS = [-1001696392169, -1002168291561, -1002327413167, -1002656374686]

@bot.message_handler(content_types=["text", "photo", "video", "document", "audio", "voice", "video_note"])
def handle_forwarded_message(message):
    if message.forward_from_chat and message.forward_from_chat.type in ["channel", "supergroup"]:
        print(f"ID пересланного канала: {message.forward_from_chat.id}")

        if message.forward_from_chat.id in ALLOWED_CHANNEL_IDS:
            print(f"Сообщение из канала {message.forward_from_chat.id} не будет удалено")
            return

        if message.text:
            if any(word in message.text for word in FORBIDDEN_WORDS):
                try:
                    bot.delete_message(message.chat.id, message.message_id)
                except Exception as e:
                    print(f"Ошибка при удалении сообщения с текстом: {e}")

        elif (message.photo or message.video or message.document or message.audio) and \
                (message.text is None or any(word in message.text for word in FORBIDDEN_WORDS)):
            try:
                bot.delete_message(message.chat.id, message.message_id)
            except Exception as e:
                print(f"Ошибка при удалении сообщения с медиа: {e}")

    else:
        pass

bot.remove_webhook()
bot.polling(none_stop=True)