'''
基本逻辑是上传sql内容，然后结合数据库连接信息重组sql，通过inception检查，然后存储到sqlrecord表，返回一个uuid
然后通过uuid触发sql执行
这里只写了点主要的内容，其他内容可以自行完善
'''
import pymysql
'''
DatabaseConnInfo存储要操作的数据库连接信息
'''
from models import DatabaseConnInfo


def get_inception_sql(sql, env, dbname, sql_type):
    try:
        if env in ['dev', 'test', 'demo']:
            conn_data = DatabaseConnInfo.objects.get(conn_name=env)
        else:
            conn_data = DatabaseConnInfo.objects.get(conn_name=dbname)
        user = conn_data.username
        password = conn_data.password
        host = conn_data.host
        port = conn_data.port
        inception_sql = '/*--user={};--password={};--host={};--enable-{};--port={};*/\
            inception_magic_start;\
            use {};\
            {}\
            inception_magic_commit;'.format(user, password, host, sql_type, port, dbname, sql)
        return inception_sql
    except DatabaseConnInfo.DoesNotExist as e:
        print(e)
        return None


def check(sql, env, dbname):
    sql_type = "check"
    inception_sql = get_inception_sql(sql, env, dbname,sql_type)
    data = {}
    conn = pymysql.connect(host=inception_host, user='root', passwd='', db='', port=6669)
    cur = conn.cursor()
    try:
        cur.execute(inception_sql)
        results = cur.fetchall()
        print(results)
        data['error_msg'] = ''
        data['error_sql'] = ''
        for result in results:
            if result[2] != 0:
                data['error_msg'] = result[4]
                data['error_sql'] = result[5]
        cur.close()
        conn.close()
	return data

def execute(uuid):
	run_type = "execute"
	inception_sql = get_inception_sql(sql_content, env, dbname, sql_type)
	conn = pymysql.connect(host=inception_host, user='root', passwd='', db='', port=6669)
    	cur = conn.cursor()
	cur.execute(inception_sql)
	results = cur.fetchall()
	
	return results

	


