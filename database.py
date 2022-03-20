dimport pymysql


class Database:
    def connect(self):
        return pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='flask')
    
    
    def deletecom(self,id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM comparison  where id = %s", (id,))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()
        
    def readcomp(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM  comparison order by name asc")
            else:
                cursor.execute("SELECT * FROM comparison  where id = %s order by name asc", (id,))

            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()
    def insertDnaText(self,name,SeqA,SeqB,rep):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute("INSERT INTO comparison (name,SeqATextPath,SeqBTextPath,report) VALUES(%s, %s, %s, %s)", (name,SeqA,SeqB,rep,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()
 
    def readbio(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM  sequence order by name asc")
            else:
                cursor.execute("SELECT * FROM sequence  where id = %s order by name asc", (id,))

            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()
    
  
    def insertFasta(self,name,pathFasta,pathcsv):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO sequence (name,PathFasta,PathCSV) VALUES(%s, %s, %s)", (name,pathFasta,pathcsv,))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()
            
    def deleteb(self,id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM sequence  where id = %s", (id,))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()


    def read(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM customers  order by name asc")
            else:
                cursor.execute("SELECT * FROM customers  where id = %s order by name asc", (id,))

            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def insert(self,data,imagepath):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO customers (name,phone,address,path) VALUES(%s, %s, %s,%s)", (data['name'],data['phone'],data['address'],imagepath,))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

    def update(self, id, data):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE customers  set name = %s, phone = %s, address = %s where id = %s", (data['name'],data['phone'],data['address'],id,))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

    def delete(self, id):
        
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute("DELETE FROM customers  where id = %s", (id,))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()




    