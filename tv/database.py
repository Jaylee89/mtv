import sqlite3

class DB:
    table_name: str

    def __init__(self, table_name = 'tv'):
        self.table_name = table_name

    def start(self):
        self.conn = sqlite3.connect(f'{self.table_name}.db')
        self.cursor = self.conn.cursor()
 
    def init_table(self):
        self.start()
        self.__creat_table()
        self.close()

    def __creat_table(self):
        '''
        id:           index of data row
        name:         data name
        url:          data url
        category:     data category
        http_code:    data http code
        ipv4:         data ipv4: 1, ipv6: 0, n/a: 9
        valid:        data url valid: 11, invalid: 10, n/a: 9
        '''
        try:
            sql = f'''
            CREATE TABLE IF NOT EXISTS `{self.table_name}`(
               `id` INTEGER PRIMARY KEY AUTOINCREMENT,
               `name` VARCHAR(30) NOT NULL,
               `url` VARCHAR(500) NOT NULL,
               `category` VARCHAR(20),
               `http_code` INTEGER UNSIGNED,
               `ipv4` INTEGER UNSIGNED,
               `valid` INTEGER UNSIGNED,
               `updated_date` TIMESTAMP
            );
            '''
            self.cursor.execute(sql)
            return 1
        except Exception as e:
            print('>> Creat Error:', e)
            return 0
 
    def insert(self, data: tuple):
        try:
            sql = f'''
            INSERT INTO {self.table_name} (name, url, category, http_code, ipv4, valid, updated_date)
            VALUES (?, ?, ?, ?, ?, ?);
           '''
            self.start()
            self.cursor.execute(sql, data) # (name, url, category, http_code, ipv4, valid, updated_date)
            self.conn.commit()
            self.close()
            return 1
        except Exception as e:
            print('>> insert Error:', e)
            return 0
        
    def insert_many(self, data: list):
        try:
            sql = f'''
            INSERT INTO {self.table_name} (name, url, category, http_code, ipv4, valid, updated_date)
            VALUES
            (?, ?, ?, ?, ?, ?);
           '''
            self.start()
            self.cursor.executemany(sql, data)
            self.conn.commit()
            self.close()
            return 1
        except Exception as e:
            print('>> insert Error:', e)
            return 0
 
    def select_by(self, field: str):
        self.start()
        self.cursor.execute(f'''SELECT * from {self.table_name} WHERE category=(?) or name=(?) or http_code=(?) or ipv4=(?) or valid=(?);''', (field))
        res = self.cursor.fetchall()
        self.close()
        return res
 
    def close(self):
        self.cursor.close()
        self.conn.close()
 
    def SelectALL(self):
        self.start()
        sql = f"SELECT * from {self.table_name};"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        self.close()
        return res