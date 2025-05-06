# -*- coding: utf-8 -*-

from flask import request, make_response

import html


def make_view(robot):
    """
    为一个 BaseRoBot 生成 Flask view。

    Usage ::

        from werobot import WeRoBot

        robot = WeRoBot(token='token')


        @robot.handler
        def hello(message):
            return 'Hello World!'

        from flask import Flask
        from werobot.contrib.flask import make_view

        app = Flask(__name__)
        app.add_url_rule(rule='/robot/', # WeRoBot 的绑定地址
                        endpoint='werobot', # Flask 的 endpoint
                        view_func=make_view(robot),
                        methods=['GET', 'POST'])

    :param robot: 一个 BaseRoBot 实例
    :return: 一个标准的 Flask view
    """
    def werobot_view():
        if 'CheckContainerPath' in request.data:
            return ''
        message = robot.parse_message(
            request.data
        )
        response = make_response(robot.get_reply(message))
        response.headers['content_type'] = 'application/xml'
        return response

    return werobot_view
