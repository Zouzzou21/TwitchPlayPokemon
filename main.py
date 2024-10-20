import os
from dotenv import load_dotenv
from twitchio.ext import commands
from pynput.keyboard import Key, Controller
import time

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Récupérer les informations sensibles depuis les variables d'environnement
TWITCH_TOKEN = os.getenv('TWITCH_TOKEN')
TWITCH_NICKNAME = os.getenv('TWITCH_NICKNAME')
TWITCH_CHANNEL = os.getenv('TWITCH_CHANNEL')

# Bot Twitch
class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token=TWITCH_TOKEN, prefix='!', initial_channels=[TWITCH_CHANNEL])

    async def event_ready(self):
        print(f'Bot is ready and logged in as | {self.nick}')

    async def event_message(self, message):
        if message.author.name.lower() == self.nick.lower():
            return

        print(f'{message.author.name}: {message.content}')
        await self.handle_commands(message)

        handle_pokemon_command(message.content)

# Fonction pour traiter les commandes du chat
def handle_pokemon_command(command):
    valid_commands = ["up", "down", "left", "right", "a", "b", "y", "x", "l", "r", "start", "select"]
    if command.lower() in valid_commands:
        inject_command_into_game(command.lower())

keyboard = Controller()

def inject_command_into_game(command):
    key_mapping = {
        "up": Key.up,
        "down": Key.down,
        "left": Key.left,
        "right": Key.right,
        "a": 'a',  # Assurez-vous que cela correspond aux touches de votre émulateur
        "b": 'b',
        "y": 'y',
        "x": 'x',
        "l": 'l',
        "r": 'r',
        "start": Key.enter,
        "select": Key.backspace
    }

    if command in key_mapping:
        key = key_mapping[command]
        keyboard.press(key)
        time.sleep(0.2)  # Pour s'assurer que la touche est enregistrée
        keyboard.release(key)

bot = Bot()
bot.run()
