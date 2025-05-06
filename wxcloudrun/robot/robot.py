from ..werobot.robot import WeRoBot

robot = WeRoBot()

@robot.text
def hello_world(message):
    return message.content[::-1]
