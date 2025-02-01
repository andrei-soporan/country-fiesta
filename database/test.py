import getpass
import oracledb

usr = 'nds_reference'
connString = '192.168.1.115/and'
pwd = getpass.getpass(f'Enter password for user{usr}@{connString}:')

with oracledb.connect(user=usr, password=pwd, dsn=connString) as connection:
    with connection.cursor() as cursor:
        sql = """select * from dtUser"""
        for r in cursor.execute(sql):
            print(r)
            
