import logging
import os


LOG_PATH = os.getenv("LOG_PATH", "logs/shortener.log")

logger = logging.getLogger("shortener")
logger.setLevel(logging.INFO)

if os.path.dirname(LOG_PATH):
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

fh = logging.FileHandler(LOG_PATH)
fh.setFormatter(logging.Formatter("%(asctime)s %(levelname)s: %(message)s"))
logger.addHandler(fh)

ch = logging.StreamHandler()
ch.setFormatter(logging.Formatter("%(asctime)s %(levelname)s: %(message)s"))
logger.addHandler(ch)
