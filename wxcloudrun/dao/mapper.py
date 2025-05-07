import pymysql


mysql_config = {
    'host': '10.12.109.183',
    'port': 3306,
    'user': 'root',
    'password': '123!@#qwe',
    'db': 'duty',
    'autocommit': True,
    'cursorclass': pymysql.cursors.DictCursor
}

cursor = pymysql.connect(**mysql_config).cursor()

sql = '''select name, finished, unfinished, assessment from employee_duties where number=%s'''

def get_content(number):
    cursor.execute(sql, (number))
    if result := cursor.fetchone():
        return f'{result['name']}, 你好，本月你已经完成的安全履职事项“{result['finished']}”，还有“{result['unfinished']}未完成履职”，截止目前，本月安全履职评价为“{result['sssessment']}”'
    return '未查找到履职信息，请检查员工编号'