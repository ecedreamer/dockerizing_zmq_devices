import logging
import sys
import pathlib


CURRENT_PATH = pathlib.Path(__file__).parent.parent.resolve()

LOG_FILE_PATH = CURRENT_PATH / "logs/streamer.log"


logging.basicConfig(filename=LOG_FILE_PATH,
                    format='%(asctime)s %(message)s',
                    filemode='a')
 
logger = logging.getLogger()
logger.setLevel(logging.INFO)