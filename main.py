import discord
from discord.ext import commands
import joblib

model = joblib.load('Testament_Classifier.pkl')
vectorizer = joblib.load('TC_Vectorizer.pkl')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!",intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Logged in as {bot.user}')

@bot.command()
async def classify(ctx, *, verse: str = None):
    # Check if user provided a verse
    if not verse or verse.strip() == "":
        await ctx.send("⚠️ Please provide a verse to classify. Usage: `!classify <verse>`")
        return

    try:
        result = model.predict(vectorizer.transform([verse]))[0]
        prediction = "New Testament" if result == "NT" else "Old Testament"
        await ctx.send(f"Verse: '{verse}'\nPrediction: {prediction}")
    except Exception as e:
        # Catch unexpected errors
        await ctx.send(f"❌ An error occurred while classifying the verse.\nError: {e}")

bot.run("MTQwNjI0NjYxMjYyNzYxOTkwMg.GNi7Gm.LdTGdqNN4-DpEZca1Bf1GMziuHs65G3jhs_720")