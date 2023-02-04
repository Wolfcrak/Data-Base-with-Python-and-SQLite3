import sqlite3
conn = sqlite3.connect('example.db')

#This code is used to create the Data Base

def createDB():
     conn = sqlite3.connect("example.db")
     cursor = conn.cursor()
     cursor.execute(
          """CREATE TABLE example (
               nombre text,
               apellido text,
               edad interger"""
     )
     conn.commit()
     conn.close()

#This code is used to create a Table in the Data Base

def createTable():
     conn = sqlite3.connect('example.db')
     conn.commit()
     conn.close()

#This code is to add data in the table

def insertRow(nombre, apellido, edad):
     conn = sqlite3.connect('example.db')
     cursor = conn.cursor()
     instruccion = f"INSERT INTO example VALUES ('{nombre}', {apellido}, {edad})"
     cursor.execute(instruccion)
     conn.commit()
     conn.close() 

#This code is to give you the data

def readRows():
     conn = sqlite3.connect('example.db')
     cursor = conn.cursor()
     instruccion = f"SELECT * FROM example "
     cursor.execute(instruccion)
     datos = cursor.fetchall()
     conn.commit()
     conn.close()  
     print(datos)


#This code is to give you the data in the order you want removing and putting "DESC"

def readordered(field):
     conn = sqlite3.connect('example.db')
     cursor = conn.cursor()
     instruccion = f"SELECT * FROM example ORDERER BY {field} DESC"
     cursor.execute(instruccion)
     datos = cursor.fetchall()
     conn.commit()
     conn.close()  
     print(datos)

#this code is to run the functions 

if __name__ == "__main__":
    #put this code only once then yoy put "#" in the beggining
    createDB()
    createTable()
    
    #this code is to add Rows in the table
    insertRow("Josue", "Obando_Pimentel", 44)
    insertRow("Merary", "Chavarria_Monge", 39)
    insertRow("Joel", "Obando_Chavarria", 12) 
    insertRow("Lidny", "Obando_Chavarria", 9)

    #or you can put
    example = [
    ("Josue", "Obando_Pimentel", 44)
    ("Merary", "Chavarria_Monge", 39) 
    ("Joel", "Obando_Chavarria", 12)
    ("Lidny", "Obando_Chavarria", 9)
    ]

    #this code give you data
    readRows()

    #and this is to reed ordered the data
    readordered()