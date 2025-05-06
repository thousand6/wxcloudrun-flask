from flask import Flask
import config
from .robot.robot import robot
from werobot.contrib.flask import make_view

# 初始化web应用
app = Flask(__name__, instance_relative_config=True)
app.config['DEBUG'] = config.DEBUG

# 加载控制器
from wxcloudrun import views

# 加载配置
app.config.from_object('config')

app.add_url_rule(rule='/wx/api',        # WeRoBot 挂载地址
                 endpoint='werobot',    # Flask 的 endpoint
                 view_func=make_view(robot),
                 methods=['GET', 'POST'])
