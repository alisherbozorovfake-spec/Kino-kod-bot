import telebot
from config import TOKEN, CHANNELS, MOVIE_CHANNEL, MOVIES

bot = telebot.TeleBot(8592895853:AAEg_fZI-PozBZT6av8fZMsxbgbOYwv94mA)

def check_sub(user_id):
    for ch in CHANNELS:
        try:
            status = bot.get_chat_member(ch, user_id).status
            if status not in ['member', 'administrator', 'creator']:
                return False
        except:
            return False
    return True

@bot.message_handler(commands=['start'])
def start(message):
    if not check_sub(message.from_user.id):
        text = "❌ Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:\n\n"
        for ch in CHANNELS:
            text += f"👉 {ch}\n"
        text += "\n✅ Obuna bo‘lgach, /start ni qayta bosing"
        bot.send_message(message.chat.id, text)
        return

    bot.send_message(
        message.chat.id,
        "🎬 Kino kodini yuboring:\n\nMasalan: 541"
    )

@bot.message_handler(func=lambda m: True)
def send_movie(message):
    if not check_sub(message.from_user.id):
        bot.send_message(message.chat.id, "❌ Avval kanallarga obuna bo‘ling")
        return

    code = message.text.strip()
    if code in MOVIES:
        post_id = MOVIES[code]
        bot.copy_message(
            chat_id=message.chat.id,
            from_chat_id=MOVIE_CHANNEL,
            message_id=post_id
        )
    else:
        bot.send_message(message.chat.id, "❌ Bunday kod topilmadi")

bot.infinity_polling()
