import sqlite3

class SQLighter:
     def __init__(self,database_file):
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()

     def subscriber_exests(self,user_id):
              with self.connection:
                   result = self.cursor.execute("SELECT * FROM `subscrip` WHERE `user_id` = ?", (user_id,)).fetchall()
                   return bool(len(result))
     def group_exests(self,user_id):
              with self.connection:
                   result = self.cursor.execute("SELECT `group` FROM `subscrip` WHERE `user_id` = ?", (user_id,))
                   return result.fetchone()
     def get_document(self,user_id):
           with self.connection:
                 result = self.cursor.execute("SELECT `file_name`, `group` FROM `filedoc` WHERE `user_id` = ?",(user_id,)) 
                 return result.fetchone() 
     def get_document2(self,user_id):
           with self.connection:
                 result = self.cursor.execute("SELECT `file_name`, `group` FROM `filedoc2` WHERE `user_id` = ?",(user_id,)) 
                 return result.fetchone()   
     def get_document3(self,user_id):
           with self.connection:
                 result = self.cursor.execute("SELECT `file_name`, `group` FROM `filedoc3` WHERE `user_id` = ?",(user_id,)) 
                 return result.fetchone()   
     def get_document4(self,user_id):
           with self.connection:
                 result = self.cursor.execute("SELECT `file_name`, `group` FROM `filedoc4` WHERE `user_id` = ?",(user_id,)) 
                 return result.fetchone()                     
     def add_document(self,user_id,file_name,file_id,group):
           with self.connection:
                 return self.cursor.execute("INSERT INTO `filedoc` (`user_id`,`file_name`,`file_id`,`group`) VALUES(?,?,?,?)",(user_id,file_name,file_id,group))
     def add_document2(self,user_id,file_name,file_id,group):
           with self.connection:
                 return self.cursor.execute("INSERT INTO `filedoc2` (`user_id`,`file_name`,`file_id`,`group`) VALUES(?,?,?,?)",(user_id,file_name,file_id,group)) 
     def add_document3(self,user_id,file_name,file_id,group):
           with self.connection:
                 return self.cursor.execute("INSERT INTO `filedoc3` (`user_id`,`file_name`,`file_id`,`group`) VALUES(?,?,?,?)",(user_id,file_name,file_id,group)) 
     def add_document4(self,user_id,file_name,file_id,group):
           with self.connection:
                 return self.cursor.execute("INSERT INTO `filedoc4` (`user_id`,`file_name`,`file_id`,`group`) VALUES(?,?,?,?)",(user_id,file_name,file_id,group))                                                 
     def add_subscriber(self,user_id,group):
         with self.connection:
              return self.cursor.execute("INSERT INTO 'subscrip' (`user_id`,`group`) VALUES(?,?)",(user_id,group))     
     def close(self):
          self.connection.close()