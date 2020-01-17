from commands import *

async def callCommands(eventObject):
    #minor event checks for further specification, meant to avoid an endless elif sequence
    if eventObject["messageText"] == "/start" or eventObject["messageText"] == "/help" or eventObject["messageText"] == "/stop":
        await baseCommands(eventObject)
    elif eventObject["messageText"] == "a" or eventObject["messageText"] == "b" or eventObject["messageText"] == "c":
        await alphabetCommands(eventObject)

async def baseCommands(eventObject):
    if eventObject["messageText"] == "/start":
        await start.command(eventObject)
    elif eventObject["messageText"] == "/help":
        await helpCommand.command(eventObject)
    elif eventObject["messageText"] == "/stop":
        await stop.command(eventObject)

async def alphabetCommands(eventObject):
    if eventObject["messageText"] == "/a":
        await a.command(eventObject)