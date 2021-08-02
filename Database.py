import pymysql


def database_conn():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password="Root12!@",
        db='GoogleNews',
    )
    db_name = "GoogleNews"
    cur = conn.cursor()
    # sqlStatement = "CREATE DATABASE "+db_name
    # cur.execute(sqlStatement)
    Sqltable = "CREATE TABLE if not exists "+db_name+"(`id` INT AUTO_INCREMENT PRIMARY KEY," \
                                                     "`title` VARCHAR(255) CHARACTER SET utf8," \
                                                     "`media` VARCHAR(255) CHARACTER SET utf8," \
                                                     "`published_date` VARCHAR(14) CHARACTER SET utf8," \
                                                     "`description` text(1089) CHARACTER SET utf8," \
                                                     "`link` VARCHAR(255) CHARACTER SET utf8," \
                                                     "`img` VARCHAR(255) CHARACTER SET utf8," \
                                                     "`created_at` DATETIME)"
    cur.execute(Sqltable)
    # db = "INSERT INTO" + db_table + "VALUES('"title"'+'"desc"')"

    delete_query = "DELETE FROM GoogleNews WHERE link = 'DummyLink' and img = 'DummyImg'"
    with conn.cursor() as cursor:
        cursor.execute(delete_query)
        conn.commit()


database_conn()

