import hikari, lightbulb
from dotenv import load_dotenv
from datetime import *
import os

load_dotenv()
bot = lightbulb.BotApp(token=f"{os.getenv('api_key')}")


@bot.command
@lightbulb.option('pages', 'Number of pages you plan to read', required=False)
@lightbulb.option('time', 'Enter the amount of reading time.')
@lightbulb.command('sprint', 'Start a reading sprint.')
@lightbulb.implements(lightbulb.SlashCommand)
async def readSprint(ctx):
    await ctx.respond('This is the time: ' + ctx.options.time + '. This is your page goal: ' + ctx.options.pagegoal)

bot.run()