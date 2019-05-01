import pymysql

def get_userpwd():
    db=pymysql.connect(
        host='localhost',
        user='root',
        password='Achencan123',
        db='test',
        port=3306
    )
    cur=db.cursor()
    try:
        cur.execute("select * from usr")
        results=cur.fetchall()
    except Exception as e:
        raise e

    finally:
        return results
        db.close()
