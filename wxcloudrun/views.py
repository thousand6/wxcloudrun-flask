from flask import render_template
from run import app


@app.route('/')
def index():
    """
    :return: 返回index页面
    """
    return render_template('index.html')
