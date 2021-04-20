import mysql.connector as connector

class CRUD:

    def __init__(self):
        print("Hello we are going to perform CURD Operations") 
        self.con = connector.connect(host='localhost',port='3306',user='root',password='Khan98!!!!',database='pythondb')    #established connection between your database  
        print(self.con)  
          # Create Query
        query = 'create table students(studentId int primary key, studentName varchar(200),phone varchar(12))'

        cur = self.con.cursor() # cursor() method create a cursor object 

        cur.execute(query)  # Execute Query

        print("Created....")

    # insert 
    def insert(self,studentId, studentName, phone):
        query = "insert into students(studentId,studentName,phone) values ({},'{}','{}')".format(studentId,studentName,phone)
        print(query)
        cur = self.con.cursor() # cursor() method create a cursor object 
        cur.execute(query)
        self.con.commit()   # Commit is used for your changes in the database and rollback used for if any error   
        print("Data inserted on DB Successfully...")

    # Select
    def select(self):
        query = "select *from students"
        cur = self.con.cursor() # cursor() method create a cursor object 
        cur.execute(query)
        for row in cur:
            print("studentId : ",row[0])
            print("studentName : ",row[1])
            print("Phone : ",row[2])

    # Delete Query
    def delete(self,studentId):
        query = "delete from students where studentId = {}".format(studentId)
        print(query)
        c = self.con.cursor()   # cursor() method create a cursor object 
        c.execute(query)
        self.con.commit()   # Commit is used for your changes in the database and rollback used for if any error   
        print("Deleted Successfully....")

    # Update Query
    def update(self,studentId,newName,newPhone):
        query = "update students set studentName = '{}', phone = '{}' where studentId = {}".format(newName,newPhone,studentId)
        print(query)
        c = self.con.cursor()   # cursor() method create a cursor object 
        c.execute(query)
        self.con.commit()   # # Commit is used for your changes in the database and rollback used for if any error   
        print("Updated Successfully...")

# main function
if __name__ == '__main__':
    operations = CRUD()
    operations.insert(21,"sahib","86685558393")
    operations.insert(204,"khan","45721578")
    operations.insert(80,"krit","9528461254")
    operations.select()
    operations.delete(21)
    operations.select()
    operations.update(205,"SHK","5784578457")
    operations.select()