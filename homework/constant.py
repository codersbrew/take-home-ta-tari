import logging
import os

BASE_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        os.path.pardir
    )
)

ROTATIONS_FILE = BASE_PATH + "/data/rotations.csv"
SPOTS_FILE = BASE_PATH + "/data/spots.csv"

DATE_FMT = "%m/%d/%Y"
TIME_FMT = "%I:%M %p"

# Logging Config, could be done in an ini
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# create single instance to use
logger = logging.getLogger()
