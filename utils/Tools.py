import json, sys, os
from discord.ext import commands
from core import Context
import aiohttp



def DotEnv(query: str):
  return os.getenv(query)

def getConfig(guildID):
    with open("config.json", "r") as config:
        data = json.load(config)
    if str(guildID) not in data["guilds"]:
        defaultConfig = {
            "antiSpam": False,
            "antiLink": False,
            "whitelisted": [], 
            "punishment": "ban",
            "prefix": "@"
        }
        updateConfig(guildID, defaultConfig)
        return defaultConfig
    return data["guilds"][str(guildID)]


def updateConfig(guildID, data):
    with open("config.json", "r") as config:
        config = json.load(config)
    config["guilds"][str(guildID)] = data
    newdata = json.dumps(config, indent=4, ensure_ascii=False)
    with open("config.json", "w") as config:
        config.write(newdata)


def add_user_to_blacklist(user_id: int) -> None:
    with open("blacklist.json", "r") as file:
        file_data = json.load(file)
        if str(user_id) in file_data["ids"]:
            return

        file_data["ids"].append(str(user_id))
    with open("blacklist.json", "w") as file:
        json.dump(file_data, file, indent=4)


def remove_user_from_blacklist(user_id: int) -> None:
    with open("blacklist.json", "r") as file:
        file_data = json.load(file)
        file_data["ids"].remove(str(user_id))
    with open("blacklist.json", "w") as file:
        json.dump(file_data, file, indent=4)


def update_vanity(guild, code):
    with open('vanity.json', 'r') as vanity:
        vanity = json.load(vanity)
    vanity[str(guild)] = str(code)
    new = json.dumps(vanity, indent=4, ensure_ascii=False)
    with open('vanity.json', 'w') as vanity:
        vanity.write(new)


def blacklist_check():
    def predicate(ctx):
        with open("blacklist.json") as f:
            data = json.load(f)
            if str(ctx.author.id) in data["ids"]:
                return False
            return True

    return commands.check(predicate)


def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)




def getbadges(userid):
  with open("badges.json", "r") as f:
    data = json.load(f)
  if str(userid) not in data:
    default = []
    makebadges(userid, default)
    return default
  return data[str(userid)]

def makebadges(userid, data):
  with open("badges.json", "r") as f:
    badges = json.load(f)
  badges[str(userid)] = data
  new = json.dumps(badges, indent=4, ensure_ascii=False)
  with open("badges.json", "w") as w:
    w.write(new)




def getanti(guildid):
    with open("anti.json", "r") as config:
        data = json.load(config)
    if str(guildid) not in data["guilds"]:
        default = "off"
        updateanti(guildid, default)
        return default
    return data["guilds"][str(guildid)]

def updateanti(guildid, data):
    with open("anti.json", "r") as config:
        config = json.load(config)
    config["guilds"][str(guildid)] = data
    newdata = json.dumps(config, indent=4, ensure_ascii=False)
    with open("anti.json", "w") as config:
        config.write(newdata)