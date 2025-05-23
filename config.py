import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("20492653", ""))
API_HASH = getenv("085603f4b4ae5721c3eb967050b7c3b0", "")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("7072325009:AAF8Vy3Ub09mIL9fMTO8IDNpUMq6Z6R_T4o")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("mongodb+srv://VeraoXMusic:VeraoXMusic@cluster0.lao28.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 600))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = int(getenv("1002570887006", None))

# Get this value from @BRANDRD_ROBOT on Telegram by /id
OWNER_ID = int(getenv("7795369685", ""))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/WCGKING/BRANDEDKING",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/phonkrayupdates")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/phonkray")

# Set it in True if you want to leave your assistant after a certain amount of time. [Set time via AUTO_LEAVE_ASSISTANT_TIME]
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", None)

# Time after which you're assistant account will leave chats automatically.
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)  # Remember to give value in Seconds

# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", 700))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", 700))

# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @BRANDEDSTRINGSESSION_BOT on Telegram
STRING1 = getenv("BQE4sW0AuD_yHtNk9ltEB1avnLgnYgWPLxRrxtTzyAHmDpWR0PQmqWbhklgTlJ-7XbEvskIMDYAcYjfhw-Xa2m4nm4SLiopkNbVf5kpblaOZFMn5RpRU9ZNNC8Z1ZFF9PegYuhqQcQiESulTPnSShiU3a_2_mtQs9voEEgNrTYpz8hujBa5kRodHoR-zwr5w485uyX7OcldHATKgwgCFzCvzAPGL-_iBlEoFYpUHz4QPuJdl4iQ35K491XG-oyXDmG_8SOX4C8umvzWN113BVRo16pierLavFmPvkl8TLKncZjyE2Q5AxEp_AJfBeNl4PQyVpuJ56F9YlhxtHQau7PZxFTxTkwAAAAHQo-bVAA", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/23d891bcb4bf014452cbe-ec1e6e0da9f6a730d5.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/aab653db92b77492b99f0-7a5f4b44a0514f8d14.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
