import werobot

robot = werobot.WeRoBot()

@robot.text
def hello_world():
    return 'Hello World!'
