# Zouzzou21/TwitchPlayPokemon

This project allows Twitch viewers to control a Pokémon game running on a DeSmuME emulator by entering commands in the Twitch chat.

## Setup Instructions

### 1. Install Required Libraries
First, install the necessary libraries from the `requirements.txt` file by running the following command:

```bash
pip install -r requirements.txt --break-system-packages
```

### 2. Create a `.env` File
Next, create a `.env` file at the root of the repository. This file should contain your Twitch credentials, structured like this:

```env
TWITCH_TOKEN=oauth:exampletoken123456
TWITCH_NICKNAME=mytwitchbot
TWITCH_CHANNEL=mytwitchchannel
```

Make sure to replace the values with your actual Twitch bot information.

### 3. Configure Emulator Keymap
Before running the code, ensure that your emulator's key mappings match the following configuration:

```python
key_mapping = {
    "up": 'up',
    "down": 'down',
    "left": 'left',
    "right": 'right',
    "a": 'a',  # Adjust to match your emulator's settings
    "b": 'b',
    "y": 'y',
    "x": 'x',
    "l": 'l',
    "r": 'r',
    "start": 'enter',
    "select": 'backspace'
}
```

You can usually check and update your key mappings in the emulator’s settings under `Config > Control Config`.

### 4. Run the Program
Once the setup is complete, you can run the bot by executing the `main.py` script:

```bash
python main.py
```