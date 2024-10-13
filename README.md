# TwitchPlayPokemon
First install librairie from the [requirement.txt](requirement.txt) with the command bellow:
```bash
pip install -r requirement.txt --break-system-packages
```
After you need to make a **.env** file at the root of the reposiroty. The **.env** file look like:
```env
TWITCH_TOKEN=oauth:exampletoken123456
TWITCH_NICKNAME=mytwitchbot
TWITCH_CHANNEL=mytwitchchannel
```
Before execute the code please be sure you have the good keymap configuration on your emulator:
```python
key_mapping = {
    "up": 'up',
    "down": 'down',
    "left": 'left',
    "right": 'right',
    "a": 'a',
    "b": 'b',
    "y": 'y',
    "x": 'x',
    "l": 'l',
    "r": 'r',
    "start": 'enter',
    "select": 'backspace'
}
```
After you only need to execute the [main.py](main.py) program with the command:
```bash
python main.py
```