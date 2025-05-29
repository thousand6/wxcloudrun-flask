import pymysql
from datetime import datetime


mysql_config = {
    'host': '10.12.109.184',
    'port': 3306,
    'user': 'root',
    'password': '123!@#qwe',
    'db': 'duty',
    'autocommit': True,
    'cursorclass': pymysql.cursors.DictCursor
}

sql = '''select name, duties, key_points, finished, unfinished, assessment from employee_duties where number=%s'''

def get_content(number):
    with pymysql.connect(**mysql_config) as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (number))
            if result := cursor.fetchone():
                date = datetime.now()
                month = date.month
                day = date.day
                return f"{result['name']}，你好，本月你应完成的安全履职事项为：\n{result['duties']}\n\n截止到{month}月{day}日，仍需完成的安全履职事项为：\n{result['unfinished']}\n\n截止目前，本月安全履职评价为：“{result['assessment']}”。"
    return None