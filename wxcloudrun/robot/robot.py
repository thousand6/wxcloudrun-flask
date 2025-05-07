from ..werobot.robot import WeRoBot
from ..dao.mapper import get_content

robot = WeRoBot()

@robot.text
def hello_world(message):
    return get_content(message.content)
