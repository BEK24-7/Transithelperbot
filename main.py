import logging
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = "7570226433:AAEbkJnyfjU5RQhDDmNdw0hdaPbdV4AJzYY"

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    button = [[KeyboardButton("Yordam kerak"), KeyboardButton("Kontakt yuborish")]]
    markup = ReplyKeyboardMarkup(button, resize_keyboard=True)

    await update.message.reply_text(
        f"Salom, {user.first_name}! Men sizga tranzit yuklar bo'yicha yordam bera olaman. Quyidagi tugmalardan foydalaning:", 
        reply_markup=markup
    )

    await context.bot.send_message(
        chat_id=user.id,
        text=f"Sizning Telegram ID'ingiz: {user.id}"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    text = update.message.text

    if text == "Yordam kerak":
        await update.message.reply_text("Iltimos, savolingizni yozib yuboring. Admin siz bilan tez orada bog‘lanadi.")
    elif text == "Kontakt yuborish":
        await update.message.reply_text("Iltimos, telefon raqamingizni yozib yuboring.")
    else:
        await context.bot.send_message(
            chat_id=user.id,
            text=f"Biz sizning xabaringizni qabul qildik. Tez orada javob beramiz!"
        )

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
