from werobot.robot import WeRoBot

robot = WeRoBot()

@robot.text
def hello_world():
    return 'Hello World!'
