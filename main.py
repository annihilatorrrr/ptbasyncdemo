from os import environ

from pyrogram import Client
from pyrogram.filters import command, channel
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, Defaults

defaults = Defaults(block=False)
TOKEN = environ.get("TOKEN")
pbot = Client(
    "ptbasyncdemo",
    api_id=6,
    api_hash="",
    bot_token=TOKEN,
)


async def start(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("PTB OP!")
    return


@pbot.on_message(command("start") & ~channel)
async def startp(_: pbot, m: Message):
    await m.reply_text("PYRO OP!")
    return


async def startpyro(_: Application):
    await pbot.start()
    print("PYROGRAM: Started!")
    return


builder = (Application.builder().token(TOKEN).defaults(defaults).concurrent_updates(True).post_init(startpyro))
application = builder.build()
application.add_handler(CommandHandler("start", start))
print("PTB: Started!")
application.run_polling(close_loop=False)
pbot.stop()
print("Bye!")
