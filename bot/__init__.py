import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("API_ID", "31462135"))
    API_HASH = os.environ.get("API_HASH", "b1842df444fcd7e211f428d5578c04c0")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8604733307:AAFFTpGNGuSmJM30llIl3TtEWJtx3rBLCjI")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Fastosavebot")
    #AUTH_USER = int(os.environ.get("AUTH_USER", 5071059420))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]
