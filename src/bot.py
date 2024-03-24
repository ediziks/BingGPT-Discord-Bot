#!/usr/bin/env python3
import os
import sys
import json
from discord import app_commands
import discord
from dotenv import load_dotenv
import logging
from sydney import SydneyClient

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ImageGen import ImageGenAsync


load_dotenv(".env")
TOKEN = os.getenv("BOT_TOKEN")
SERVER_ID = os.getenv("SERVER_ID")
MY_GUILD = discord.Object(id=SERVER_ID)

log = logging.getLogger("discord.bot")


class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)


@client.event
async def on_ready():
    log.info(f"Logged in as {client.user} (ID: {client.user.id})")
    log.info("------")


sydney = SydneyClient(style="creative")


@client.tree.command()
async def ask(interaction: discord.Interaction, prompt: str):
    """Ask BingGPT a question"""
    await interaction.response.defer(thinking=True)
    try:
        async with SydneyClient() as sydney:
            res = await sydney.ask(prompt=prompt, citations=True, search=True)
        log.info(f"Response received: {res}")
    except Exception as e:
        log.warning(e)
        await interaction.followup.send(
            "Error: " + str(e) + "\nTry again or check if your prompt is appropriate."
        )

    if len(prompt) < 1900:
        prompt = "`" + "Prompt: " + prompt + "`"
        await interaction.followup.send(prompt, suppress_embeds=True)
    else:
        prompt_first = "`" + "Prompt: " + prompt[:1900] + "`"
        await interaction.followup.send(prompt_first, suppress_embeds=True)
        prompt_rest = prompt[1900:]
        while len(prompt_rest) > 1900:
            prompt_rest_text = "`" + prompt_rest[:1900] + "`"
            await interaction.channel.send(prompt_rest_text, suppress_embeds=True)
            prompt_rest = prompt_rest[1900:]
        prompt_rest_text = "`" + prompt_rest + "`"
        await interaction.channel.send(prompt_rest_text, suppress_embeds=True)

    if len(res) < 1900:
        await interaction.channel.send(res, suppress_embeds=True)
    else:
        while len(res) > 1900:
            res_text = res[:1900]
            await interaction.channel.send(res_text, suppress_embeds=True)
            res = res[1900:]
        await interaction.channel.send(res, suppress_embeds=True)


@client.tree.command()
async def imagine(interaction: discord.Interaction, prompt: str):
    """Ask BingGPT to imagine visuals"""
    await interaction.response.defer(thinking=True)
    with open("cookies.json", encoding="utf-8") as file:
        cookie_json = json.load(file)
        for cookie in cookie_json:
            if cookie.get("name") == "_U":
                auth_cookie = cookie.get("value")
                break
    try:
        images = await ImageGenAsync(auth_cookie=auth_cookie).get_images(prompt=prompt)
        len_images = len(images)
        if len_images == 0:
            await interaction.followup.send("No images generated. Try again.")
            log.warning("No images generated. Try again.")
        elif len_images == 1:
            image_1 = images[0]
            embed1 = discord.Embed(url="https://tse4.mm.bing.net/")
            embed1.set_image(url=image_1)
            await interaction.followup.send(
                "`" + "Prompt: " + prompt + "`\n", embeds=[embed1]
            )
            log.info("Image generated.")
        elif len_images == 2:
            image_1, image_2 = images
            embed1 = discord.Embed(url="https://tse4.mm.bing.net/")
            embed2 = discord.Embed(url="https://tse4.mm.bing.net/")
            embed1.set_image(url=image_1)
            embed2.set_image(url=image_2)
            await interaction.followup.send(
                "`" + "Prompt: " + prompt + "`\n", embeds=[embed1, embed2]
            )
            log.info("Images generated.")
        elif len_images == 3:
            image_1, image_2, image_3 = images
            embed1 = discord.Embed(url="https://tse4.mm.bing.net/")
            embed2 = discord.Embed(url="https://tse4.mm.bing.net/")
            embed3 = discord.Embed(url="https://tse4.mm.bing.net/")
            embed1.set_image(url=image_1)
            embed2.set_image(url=image_2)
            embed3.set_image(url=image_3)
            await interaction.followup.send(
                "`" + "Prompt: " + prompt + "`\n", embeds=[embed1, embed2, embed3]
            )
            log.info("Images generated.")
        elif len_images == 4:
            image_1, image_2, image_3, image_4 = images
            embed1 = discord.Embed(url="https://tse4.mm.bing.net/")
            embed2 = discord.Embed(url="https://tse4.mm.bing.net/")
            embed3 = discord.Embed(url="https://tse4.mm.bing.net/")
            embed4 = discord.Embed(url="https://tse4.mm.bing.net/")
            embed1.set_image(url=image_1)
            embed2.set_image(url=image_2)
            embed3.set_image(url=image_3)
            embed4.set_image(url=image_4)
            await interaction.followup.send(
                "`" + "Prompt: " + prompt + "`\n",
                embeds=[embed1, embed2, embed3, embed4],
            )
            log.info("Images generated.")

    except Exception as e:
        log.warning(e)
        await interaction.followup.send(
            "Error: " + str(e) + "\nTry again or check if your prompt is appropriate."
        )


@ask.error
async def ask_error(interaction: discord.Interaction, error):
    log.warning(error)
    await interaction.response.send_message(
        "Error: "
        + str(error)
        + "\nTry resetting the conversation with `/reset` command."
    )


@imagine.error
async def imagine_error(interaction: discord.Interaction, error):
    log.warning(error)
    await interaction.response.send_message(
        "Error: " + str(error) + "\nTry again or check if your prompt is appropriate."
    )


@client.tree.command()
async def reset(interaction: discord.Interaction):
    """Reset the conversation"""
    async with SydneyClient() as sydney:
        # Conversation
        await sydney.reset_conversation(style="balanced")
    await interaction.response.send_message("Conversation has been reset")


client.run(TOKEN)
