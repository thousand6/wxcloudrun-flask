import werobot

robot = werobot.WeRoBot(token='jb9EQDxQ17zDiVaOj1iSedx6sgCLppV0')

@robot.text
def hello_world():
    return 'Hello World!'
