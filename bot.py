import telebot
import requests

# ====== ضع مفاتيحك هنا ======
TELEGRAM_TOKEN = "8728705076:AAE9j2SRgf9y5pWjIuQ2-IEVcAwpsOyLV0g"
OPENROUTER_API_KEY = "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"
# ============================

bot = telebot.TeleBot(TELEGRAM_TOKEN)

def ask_ai(user_message):

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openrouter/free",
        "messages": [
            {
                "role": "system",
                "content": "أنت مساعد ذكي عربي، تتكلم كل اللهجات العربية، ترد بأسلوب طبيعي بشري، مختصر ومفهوم."
            },
            {
                "role": "user",
                "content": user_message
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return "حصل خطأ في الاتصال بالذكاء الاصطناعي."

@bot.message_handler(func=lambda message: True)
def chat(message):
    try:
        reply = ask_ai(message.text)
        bot.reply_to(message, reply)
    except Exception as e:
        bot.reply_to(message, "صار خطأ 😅 جرب مرة ثانية.")

print("Bot is running...")
bot.infinity_polling(none_stop=True)
