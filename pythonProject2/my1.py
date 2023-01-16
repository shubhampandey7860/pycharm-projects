import mysql.connector
def main():
    cn=mysql.connector.Connect(database='shubham',username='root',password='root')
    c=cn.cursor()
    cmd='insert into employee values("vivek",1004)'
    c.execute(cmd)
    print('data added succesfuly')
    k=c.rowcount
    print(k)
    cn.commit
main()
