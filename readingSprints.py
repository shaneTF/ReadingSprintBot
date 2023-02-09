
import hikari, lightbulb
from dotenv import load_dotenv
from datetime import *
import os
import time

load_dotenv()
bot = lightbulb.BotApp(token=f"{os.getenv('api_key')}")


@bot.command
@lightbulb.option('pages', 'Number of pages you plan to read', required=False)
@lightbulb.option('time', 'Enter the amount of reading time.', choices=['5 mins', '10 mins', '20 mins', '30 mins', '60 mins', '2 hours'])
@lightbulb.command('sprint', 'Start a reading sprint.')
@lightbulb.implements(lightbulb.SlashCommand)
async def readSprint(ctx):

    embedmsg = hikari.Embed(color=(255, 0, 0))
    pageGoal = (ctx.options.pages if (ctx.options.pages != None and int(ctx.options.pages) > 0) else '0')

    global timerOn
    global sprintActive

    timerOn = True
    sprintActive = False

    setTimer = 0

    match ctx.options.time:
        
        case '5 mins':
            setTimer = 300
        case '10 mins':
            setTimer = 600
        case '20 mins':
            setTimer = 1200
        case '30 mins':
            setTimer = 1800
        case '60 mins':
            setTimer = 3600
        case '2 hours':
            setTimer = 7200

    embedmsg.add_field(name='*Sprint Start!*', value=f"Time: {(ctx.options.time if ctx.options.time != '2 hours' else '2 Hours')}. Page goal: {pageGoal}. Time will start in 30 seconds!")
    await ctx.respond(embedmsg)

    sprintActive = True

    time.sleep(30)
    
    while setTimer:
        setTimer -= 1
        mins, secs = divmod(setTimer, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        embedmsg.edit_field(0, '*Timer*', f"Time: {timer}. Page goal: {pageGoal}")
        await ctx.edit_last_response(embedmsg)
        time.sleep(1)
        if not timerOn:
            break
    
    if(timerOn):
        embedmsg.edit_field(0, '*Time Has Ended!*', 'Use /page count to enter your pages read.')
        await ctx.respond(embedmsg)

@bot.command
@lightbulb.command('cancel', 'Stops the timer!')
@lightbulb.implements(lightbulb.SlashCommand)
async def cancel(ctx):
    global timerOn
    timerOn = False

    embedmsg = hikari.Embed(color=(255, 0, 0))
    embedmsg.add_field(name='*Sprint Was Abandoned*', value='Use /sprint to start a new sprint.')
    await ctx.respond(embedmsg)

@bot.command
@lightbulb.command('join', 'Join the active sprint!')
@lightbulb.implements(lightbulb.SlashCommand)
async def join(ctx):

    await ctx.respond(ctx.author.mention)

bot.run()