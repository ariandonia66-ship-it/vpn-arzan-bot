import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🛒 سفارش VPN", callback_data="order")],
        [InlineKeyboardButton("💰 قیمت‌ها", callback_data="prices")],
        [InlineKeyboardButton("📞 پشتیبانی", url="https://t.me/ariandonia3017")]
    ]
    await update.message.reply_text(
        "سلام! 👋 به VPN ARZAN خوش آمدی.\n\nاز منوی زیر انتخاب کن:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "order":
        text = "برای سفارش و اطلاع از فعال بودن سرویس، با پشتیبانی پیام بده:\n@ariandonia3017"
    elif query.data == "prices":
        text = "قیمت‌ها و مدت اشتراک را از پشتیبانی بپرس:\n@ariandonia3017"
    else:
        text = "برای راهنمایی به @ariandonia3017 پیام بده."

    await query.message.reply_text(text)

def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN تنظیم نشده است.")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))
    app.run_polling()

if __name__ == "__main__":
    main()
