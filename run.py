import pymysql


def check(user, passwd, host, run_type, port, dbname, sql_file):
	run_type = "check"
	sql_response = inception

def execute(user, passwd, host, run_type, port, dbname, sql_file):
	run_type = "execute"

def inception_run(user, passwd, host, run_type, port, dbname, sql_file):
    with open(sql_file, 'rb') as file:
        sql = file.read().decode('utf-8')
    inception_sql='/*--user={};--password={};--host={};--enable-{};--port={};*/\
    inception_magic_start;\
    use {};\
    {}\
    inception_magic_commit;'.format(user, passwd, host, run_type, port, dbname, sql)
        conn=pymysql.connect(host=inception_ip,user='root',passwd='', db='',port=6669)
        cur=conn.cursor()
        cur.execute(inception_sql)
        result=cur.fetchall()
        sql_response = result[0]
        print(sql_response)
        cur.close()
        conn.close()

	return sql_response
