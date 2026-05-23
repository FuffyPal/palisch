import sys
import os
import subprocess
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Bot configuration
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.command(name="palc")
async def palc(ctx, *, text: str):
    """
    Converts the given text using the Palisch converter.
    Usage: !palc <text>
    """
    try:
        # Run the converter script as a subprocess
        command = [sys.executable, "main.py", "-t", text]

        process = subprocess.run(
            command,
            capture_output=True,
            text=True,
            encoding='utf-8'  # Important for Turkish characters
        )

        # Get the output from the terminal
        output = process.stdout.strip()

        if output:
            await ctx.send(f"**Cuteee lang~ :3 **{output}")
        else:
            # If there's an error, check stderr
            error = process.stderr.strip()
            await ctx.send(f"An error occurred: {error}")

    except Exception as e:
        await ctx.send(f"System error: {e}")


@bot.slash_command(name="palc", description="Converts the given text using the Palisch converter.")
async def palc_slash(ctx: discord.ApplicationContext, text: str):
    """
    Converts the given text using the Palisch converter.
    Usage: /palc <text>
    """
    try:
        await ctx.defer()
        # Run the converter script as a subprocess
        command = [sys.executable, "main.py", "-t", text]

        process = subprocess.run(
            command,
            capture_output=True,
            text=True,
            encoding='utf-8'  # Important for Turkish characters
        )

        # Get the output from the terminal
        output = process.stdout.strip()

        if output:
            await ctx.respond(f"**Cuteee lang~ :3 **{output}")
        else:
            # If there's an error, check stderr
            error = process.stderr.strip()
            await ctx.respond(f"An error occurred: {error}")

    except Exception as e:
        try:
            await ctx.respond(f"System error: {e}")
        except Exception:
            pass


if __name__ == "__main__":
    if TOKEN:
        bot.run(TOKEN)
    else:
        print("Error: DISCORD_TOKEN not found in .env file.")
