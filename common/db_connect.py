import pymysql




class Dbcon():
    def __init__(self, database, args):
        self.db = pymysql.connect(cursorclass=pymysql.cursors.DictCursor, database=database, **args)
        self.cul = self.db.cursor()

    def select(self, sql):
        self.cul.execute(sql)
        data = self.cul.fetchall(sql)

    def excute(self, sql):
        try:
            self.cul.execute(sql)
            self.db.commit()
        except:
            self.cul.scroll()
            self.cul.close()

    def dbclose(self):
        self.db.close()
