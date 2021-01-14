# Just copy this file to config.py and change it to your info.
from pyrogram import filters
from helpers import get_banned_users

# Get these two from https://my.telegram.org
API_ID = 1667813
API_HASH = "1f6921c27bf6cd01aba471a14ff33bcb"

# Get this from @Botfather
TOKEN = "1514565679:AAHDWubNCdFiDZ-XTXaIy0NXpBozH95kMTM"

# The IDs of the users which can stream, skip, pause and change volume
SUDO_USERS = [
1004538768,
1327934109
]

# A group ID to send messages to when a song starts playing
# Example group ID: -1001402753006
LOG_GROUP = None  # Just keep it like this if you are not going to use one

# Choose the preferred language for your bot. If English leave as it is, or change to the code of any supported language.
LANG = "en"

# Max video duration allowed for downloads in minutes
DUR_LIMIT = 5

# Remove downloaded files after playing
REMOVE_AFTER_PLAYING = False

# Show a small credit for @su_Bots in the start message
CREDIT = False

# No need to touch the following.
SUDO_FILTER = filters.user(SUDO_USERS)
BANNED = filters.user(get_banned_users())
