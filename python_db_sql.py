
def insert_into_db(account_society_db_ins,account_name_db_ins,account_password_db_ins):
    import psycopg2
    from config import host, user, password, db_name, port
    from gui import account_society,account_password,account_name

    account_society_db = account_society
    account_name_db = account_name
    account_password_db = account_password

    try:
        connection = psycopg2.connect(
            host = host,
            user = user,
            password = password,
            database = db_name,
            port = port
        )
        connection.autocommit= True
        # cursor

        # создание таблицыa
        # with connection.cursor() as cursor:
        #     cursor.execute("""CREATE TABLE users(
        #                    id serial PRIMARY KEY,
        #                    account_society VARCHAR(65) NOT NULL,
        #                    account_name VARCHAR(65) NOT NULL,
        #                    account_password VARCHAR(65) NOT NULL
        #     );""")
        #     print("[INFO] create table succes")

        # ввод данных в sql таблицу

        with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO users(account_society,account_name,account_password)
                        VALUES(%s,%s,%s);""",(account_society_db_ins,account_name_db_ins,account_password_db_ins))


    except Exception as _ex:
        print("[INFO] FAIL", _ex)
    finally:
        if connection:
            connection.close()