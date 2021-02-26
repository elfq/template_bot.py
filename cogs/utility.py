import discord
from discord.ext import commands

class Utility(commands.Cog):
  """ Uility-related commands """
  def __init__(self, bot):
    self.bot = bot

  

def setup(bot):
  bot.add_cog(Utility(bot))