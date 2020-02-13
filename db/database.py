import sqlite3


def create_database(db_path):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    create_user_table = '{}{}{}'.format(
                        'CREATE TABLE IF NOT EXISTS',
                        ' user(id INTEGER PRIMARY KEY,',
                        ' username text NOT NULL, password text NOT NULL);'
                        )

    cursor.execute(create_user_table)

    create_history_table = '{}{}{}{}{}{}'.format(
                          'CREATE TABLE IF NOT EXISTS',
                          ' purchase_history(id INTEGER PRIMARY KEY,',
                          ' product text, user_id INTEGER NOT NULL,',
                          ' product_id INTEGER NOT NULL,',
                          ' FOREIGN KEY (user_id) REFERENCES user(id),',
                          ' FOREIGN KEY (product_id) REFERENCES store(id));'
                          )
    cursor.execute(create_history_table)

    create_store_table = '{}{}{}'.format(
                         'CREATE TABLE IF NOT EXISTS',
                         ' store(id INTEGER PRIMARY KEY,',
                         ' product text, price FLOAT);'
                         )
    cursor.execute(create_store_table)

    # Add by Aaron.Z
    create_store_table = '{}{}{}{}{}{}{}{}{}'.format(
                         'CREATE TABLE az_example_01(',
                         ' id INTEGER PRIMARY KEY,',
                         ' date TEXT,',
                         ' time TEXT,',
                         ' people TEXT,',
                         ' firstname TEXT,',
                         ' lastname TEXT,',
                         ' telnumber TEXT,',
                         ' created_datetime TIMESTAMP DEFAULT (datetime(CURRENT_TIMESTAMP,"localtime")));'
                         )
    cursor.execute(create_store_table)
    cursor.execute('INSERT INTO az_example_01 (date, time, people, firstname, lastname, telnumber) VALUES(datetime("now", "localtime"),datetime("now", "localtime"), 3, "中村", "健一", "09091041234");')

    cursor.execute('INSERT OR REPLACE INTO user VALUES(1, "test_1", "qwert");')
    cursor.execute(
        'INSERT OR REPLACE INTO user VALUES(2, "test_2", "qwaszx");')
    cursor.execute(
        'INSERT OR REPLACE INTO user VALUES(3, "test_3", "zxasqw");')
    cursor.execute('INSERT OR REPLACE INTO user VALUES(4, "test_4", "asdfg");')
    cursor.execute(
        'INSERT OR REPLACE INTO user VALUES(5, "test_5", "qwerty");')

    cursor.execute('INSERT OR REPLACE INTO store VALUES(1, "car", 10999.99);')
    cursor.execute('INSERT OR REPLACE INTO store VALUES(2, "bike", 45.99);')
    cursor.execute(
        'INSERT OR REPLACE INTO store VALUES(3, "motorbike", 599.99);')
    cursor.execute(
        'INSERT OR REPLACE INTO store VALUES(4, "go-cart", 20050.99);')

    cursor.execute(
        'INSERT OR REPLACE INTO purchase_history VALUES(1, "car", 1, 1);')

    connection.commit()
    connection.close()

    print('Database successfully created and populated with data!')
