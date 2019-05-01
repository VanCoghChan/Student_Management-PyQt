import pymysql

def read_db():
    data=[]
    try:
        db=pymysql.connect(
            host='localhost',
            user='root',
            password='Achencan123',
            db='test',
            port=3306
        )
        cur=db.cursor()
        cur.execute('select * from stu_info')
        data=cur.fetchall()
    except Exception as e:
        print(e)
        db.rollback()
    finally:
        db.close()
        return data
        
    
    