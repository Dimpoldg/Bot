import os
import time
import threading
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# 🔑 Telegram Bot Token (Render ENV se aayega)
TOKEN = os.getenv("TOKEN")

# 📌 Apna Group ID yaha set karo
CHAT_ID = -1001234567890

# 🧠 Quiz List (tum yaha apne questions add kar sakte ho)
quiz_list = [
    "❓ Q1: India capital?\nA. Mumbai\nB. Delhi\nC. Kolkata\nD. Chennai",
    "❓ Q2: 2 + 2 = ?\nA. 3\nB. 4\nC. 5\nD. 6",
    "❓ Q3: Assam capital?\nA. Guwahati\nB. Dispur\nC. Jorhat\nD. Dibrugarh"
]

running = False


# 🚀 START AUTO QUIZ
def start_quiz(update: Update, context: CallbackContext):
    global running
    running = True

    update.message.reply_text("✅ Auto Quiz Started!")

    def quiz_loop():
        i = 0
        while running:
            context.bot.send_message(chat_id=CHAT_ID, text=quiz_list[i])
            i = (i + 1) % len(quiz_list)
            time.sleep(30)  # ⏱ 30 sec gap

    threading.Thread(target=quiz_loop).start()


# ⛔ STOP QUIZ
def stop_quiz(update: Update, context: CallbackContext):
    global running
    running = False
    update.message.reply_text("⛔ Auto Quiz Stopped!")


# 📌 START COMMAND
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "👋 Welcome to Auto Quiz Bot!\n\n"
        "/startquiz - Start quiz\n"
        "/stopquiz - Stop quiz"
    )


# 🚀 MAIN FUNCTION
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("startquiz", start_quiz))
    dp.add_handler(CommandHandler("stopquiz", stop_quiz))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
