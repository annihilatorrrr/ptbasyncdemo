from uvloop import install

install()
from telegram import Update
from pyrogram import Client, filters, idle
from pyrogram.types import Message
from telegram.ext import Application, CommandHandler, ContextTypes


pbot = Client(
    "testbot",
    api_id=6,
    api_hash="eb06d4abfb49dc3eeb1aeb98ae0f581e",
    bot_token="1809261258:AAHusgeYUgAcW6F1poVEscUD55Ty4_EULA0", # will be revoked!
)


@pbot.on_message(filters.command("start"))
async def starth(_: pbot, m: Message):
  await m.reply_text("Pyro")
  return


async def start(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html("PTB")
    return


application = Application.builder().token("TOKEN").build()
application.add_handler(CommandHandler("start", start))
pbot.start()
application.run_polling()
idle()