import discord
import cogs
from templatebot import Bot
from discord import AllowedMentions, Activity, Game
from os import environ as env
from dotenv import load_dotenv


bot = Bot(
    name="TemplateBot",
    command_prefix="t!",
    allowed_mentions=AllowedMentions(
     everyone=False, roles=False, users=True),
    activity=Game("h"),
)

bot.VERSION = "1.0.0"
for i in cogs.default:
  bot.load_extension(f"cogs.{i}")
bot.run(env.get("TOKEN", None))