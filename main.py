from os import environ
from asyncio import get_event_loop, sleep
from subprocess import PIPE, Popen

from telegram import Message, Update
from telegram.ext import Application, CommandHandler, ContextTypes, Defaults

defaults = Defaults(block=False)


async def start(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("PTB OP!")
    # check aliveness!
    return


async def sleeper(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    a = await update.effective_message.reply_text("Starting ...")
    await sleep(10)
    await a.edit_text("Done!")
    # this will work!
    return


async def sleeper2(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    a = await update.effective_message.reply_text("Starting non sync work ...")
    process = Popen("sleep 10", stdout=PIPE, stderr=PIPE, shell=True)
    stdout, stderr = process.communicate()
    stdout = stdout.decode()
    stderr = stderr.decode()
    await a.edit_text("Done!")
    # this will stop everything! so what should we do ?
    return


application = Application.builder().token(environ.get("TOKEN")).defaults(defaults).concurrent_updates(True).build()
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("work", sleeper))
application.add_handler(CommandHandler("work1", sleeper2))
print("Bot started")
application.run_polling()
print("Bye")
