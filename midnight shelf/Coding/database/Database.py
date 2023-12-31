import pyodbc as db
#import numpy

conn = db.connect('Driver={SQL Server};'
                                'Server=DESKTOP-SCROTBM\TEW_SQLEXPRESS;'
                                'Database=Midnight_shelf;'
                                'trust_connection=yes')
cursor = conn.cursor()

class sign_in:
    semail = ""
    spassword = ""
    susername = ""
    sphone = 0
    saddress = ""
    styp = ""
    sbirthdate = ""

    def __init__(self,email,password,username,phone,address,typ,birthdate):
        sign_in.semail = email
        sign_in.spassword = password
        sign_in.susername = username
        sign_in.sphone = int(phone)
        sign_in.saddress = address
        sign_in.styp = typ
        sign_in.sbirthdate = birthdate

    def registration(self):
        cursor.execute("select * from user_data where email={}".format(sign_in.semail))
        temp = cursor.fetchall()
        if (len(temp) != 0):
            return -1  #error means email already exists
        cursor.execute("select * from user_data where username={}".format(sign_in.susername))
        temp = cursor.fetchall()
        if (len(temp) != 0):
            return -2  #error means username already exists
        query = """INSERT INTO user_data (ID, Username, email, pass, phone, addr, typ, birthdate)VALUES ((SELECT COALESCE(MAX(ID) + 1, 0) FROM user_data),?, ?, ?, ?, ?, ?, ?)"""
        values = (sign_in.susername,sign_in.semail,sign_in.spassword,sign_in.sphone,sign_in.saddress,sign_in.styp,sign_in.sbirthdate)
        cursor.execute(query, values)
        conn.commit()
        return 0



class login:
    db_email = ""
    db_password = ""
    def __init__(self,email,password):
        self.email = email
        self.password = password
        login.db_email = self.email
        login.db_password = self.password

    def check_login(self):
        cursor.execute("select * from user_data where email={} and pass={}".format(login.db_email,login.db_password))
        temp = cursor.fetchall()
        if(len(temp)==0):
            return 0
        else:
            row = cursor.fetchone()
            return row[0]

def main():
    email = "minamalak3dds@gmail.com"
    password = 'asd'
    username = 'sonic'
    phone = 000
    address = 'abc'
    type = 'M'
    birth = '2023-05-10'
    #cursor.execute("insert into user_data (ID,Username , email,pass,phone,addr,typ,birthdate)values ((SELECT ISNULL(MAX(ID)+1,0) FROM  user_data),'miallmnlak','minamalak4dds@gmail.com','asd',21445,'asfcasvwabves','M','1990-05-15');")
    #conn.commit()

    obj = sign_in(email,password,username,phone,address,type,birth)
    obj.registration()
main()