# def avg(mmm,aa):
#     average=sum(mmm)/aa
#     print(f"Average mark: {average}")   
#     print("Overall Grade: ",end='') 
#     if(average>=90):
#         print("O")
#     elif(average>=80):
#         print("A")
#     elif(average>=70):
#         print("B")
#     else:
#         print("U")

import mysql.connector


db_con = mysql.connector.connect(
    host="192.168.1.211",
    database="CMMS",
    user="cmms",
    password="Rax@123"
)

cursor = db_con.cursor()

# now you can run queries in the 'office' database
cursor.execute("SELECT AtmLocation, Alertname FROM AtmAlert WHERE Atmid = 6424")
result = cursor.fetchall()
print(result)

db_con.close()


# import pyodbc

# server = '127.0.0.1'       
# database = 'office'        
# username = 'root'           
# password = 'Kavinjude@2004'

# conn_str = (
#     'DRIVER={SQL Server};'
#     f'SERVER={server};'
#     f'DATABASE={database};'
#     f'UID={username};'
#     f'PWD={password}'
# )
# conn = pyodbc.connect(conn_str)
# print("Connection Successful!")
# cursor = conn.cursor()
# cursor.execute("SELECT * FROM Employees WHERE EmployeeID=101")
# result=cursor.fetchall()
# print(result)