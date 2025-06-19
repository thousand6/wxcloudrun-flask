from ..werobot.robot import WeRoBot
from ..dao.mapper import get_content
from loguru import logger
import time

robot = WeRoBot()

@robot.text
def get_duties(message):
    try:
        return get_content(message.content)
    except:
        logger.exception('')
        time.sleep(1.5)
        return get_content(message.content)

