import pyodbc as db
from PIL import Image
#import numpy

conn = db.connect('Driver={SQL Server};'
                                'Server=DESKTOP-SCROTBM\TEW_SQLEXPRESS;'
                                'Database=Midnight_shelf;'
                                'trust_connection=yes')
cursor = conn.cursor()

description = """
Rowan
I'm in the business of creating fairy tales.
Theme parks. Production companies. Five-star hotels.
Everything could be all mine if I renovated Dreamland.
My initial idea of hiring Zahra was good in theory, but then I kissed her.
Things spiraled out of control once I texted her using an alias.
By the time I realized where I went wrong, it was too late.
People like me don't get happy endings.
Not when we're destined to ruin them.

Zahra
After submitting a drunk proposal criticizing Dreamland's most expensive ride, I should have been fired.
Instead, Rowan Kane offered me a dream job.
The catch? I had to work for the most difficult boss I'd ever met.
Rowan was rude and completely off-limits, but my heart didn't care.
At least not until I discovered his secret.
It was time to teach the billionaire that money couldn't fix everything.
Especially not us."""


class sign_in:
    semail = ""
    spassword = ""
    susername = ""
    sphone = 0
    saddress = ""
    styp = ""
    sbirthdate = ""

    def __init__(self,email,password,username,phone,address,typ,birthdate,role):
        sign_in.semail = email
        sign_in.spassword = password
        sign_in.susername = username
        sign_in.sphone = int(phone)
        sign_in.saddress = address
        sign_in.styp = typ
        sign_in.sbirthdate = birthdate
        self.role = role

    def registration(self):
        cursor.execute("select * from user_data where email='{}'".format(sign_in.semail))
        temp = cursor.fetchall()
        if (len(temp) != 0):
            return -1  #error means email already exists
        cursor.execute("select * from user_data where username='{}'".format(sign_in.susername))
        temp = cursor.fetchall()
        if (len(temp) != 0):
            return -2  #error means username already exists
        query = """INSERT INTO user_data (ID, Username, email, pass, phone, addr, typ, birthdate, role)VALUES ((SELECT COALESCE(MAX(ID) + 1, 0) FROM user_data),?, ?, ?, ?, ?, ?, ?, ?)"""
        values = (sign_in.susername,sign_in.semail,sign_in.spassword,sign_in.sphone,sign_in.saddress,sign_in.styp,sign_in.sbirthdate,self.role)
        cursor.execute(query, values)
        conn.commit()
        return 0



class login:
    db_email = ""
    db_password = ""
    def __init__(self,email,password,role):
        self.email = email
        self.password = password
        self.role = role
        login.db_email = self.email
        login.db_password = self.password

    def check_login(self):
        select_query = f"select * from user_data where email = ? and pass = ? and role = ?"
        values = (self.email,self.password,self.role)
        cursor.execute(select_query, values)
        temp = cursor.fetchall()
        if(len(temp)==0):
            return 0
        else:
            return temp[0][0]

def add_photo(bname,bauthor,bdescription,bimage,bprice):
    I_Path = bimage.replace('\\','/')
    x = bdescription.replace("'","''")
    bdescription = x
    with open(I_Path, 'rb') as file:
        image_data = file.read()
    file.close()
    insert_query = f"Insert into Books (ID, Name,Author, description, ImageData,price) values ((select COALESCE (max(id)+1,1 ) from Books ),?,?,?,?,? )"
    values = (bname,bauthor,bdescription,image_data,bprice)
    cursor.execute(insert_query, values)
    conn.commit()

#add_photo()

def get_photo(ID):
    select_query = f" select * from Books where ID = ? ;"
    values = (ID)
    cursor.execute(select_query, values)
    temp = cursor.fetchall()
    print(temp[0][4])
    return temp[0][4]

def user_library(user_ID):
    select_query = f"select Book_ID from Library where User_ID = ? and (state = 1 or state = 2)"
    values = (user_ID)
    cursor.execute(select_query, values)
    temp = cursor.fetchall()
    #print(temp[0][0])
    ans=[]
    for i in enumerate(temp):
        select_query = f"Select * from Books where ID = ?"
        values = (i[1][0])
        cursor.execute(select_query, values)
        tempp = cursor.fetchall()
        ans.append(tempp)
    #x=ans[2][0]
    #print(x[0])
    return ans

def user_favourite(user_ID):
    select_query = f"select Book_ID from Library where User_ID = ? and state = 2"
    values = (user_ID)
    cursor.execute(select_query, values)
    temp = cursor.fetchall()
    #print(temp[0][0])
    ans=[]
    for i in enumerate(temp):
        select_query = f"Select * from Books where ID = ?"
        values = (i[1][0])
        cursor.execute(select_query, values)
        tempp = cursor.fetchall()
        ans.append(tempp)
    #x=ans[2][0]
    #print(x[0])
    return ans

def user_wishlist(user_ID):
    select_query = f"select Book_ID from Library where User_ID = ? and state = 3"
    values = (user_ID)
    cursor.execute(select_query, values)
    temp = cursor.fetchall()
    #print(temp[0][0])
    ans=[]
    for i in enumerate(temp):
        select_query = f"Select * from Books where ID = ?"
        values = (i[1][0])
        cursor.execute(select_query, values)
        tempp = cursor.fetchall()
        ans.append(tempp)
    #x=ans[2][0]
    #print(x[0])
    return ans



def add_to_favourite(user_id,book_id):
    query = f"select state from library where user_id = ? and book_id = ?"
    values = (user_id,book_id)
    cursor.execute(query,values)
    temp = cursor.fetchall()
    print(temp[0][0])
    if temp[0][0] == 2:
        select_query = f"UPDATE library SET state = 1 WHERE user_id= ? and book_id= ? ;"
        values = (user_id,book_id)
        cursor.execute(select_query, values)
        conn.commit()
    elif temp[0][0] == 1:
        select_query = f"UPDATE library SET state = 2 WHERE user_id= ? and book_id= ? ;"
        values = (user_id,book_id)
        cursor.execute(select_query, values)
        conn.commit()

def check_state(user_id,book_id):
    query = f"select state from library where user_id = ? and book_id = ?"
    values = (user_id, book_id)
    cursor.execute(query, values)
    temp = cursor.fetchall()
    return temp[0][0]


def delete_from_library(user_id,book_id):
    select_query = f"DELETE FROM library WHERE user_id = ? and book_id = ? ;"
    values = (user_id, book_id)
    cursor.execute(select_query, values)
    conn.commit()

def search_wishlist(user_id,word):
    word += '%'
    Query = """select Book_id from library where (state = 3) and User_id = ? """
    values = (user_id)
    cursor.execute(Query,values)
    temp = cursor.fetchall()
    #print(len(temp))
    ans = []
    for i in enumerate(temp):
        select_query = f"Select * from Books where (Name like ?) and ID = ?"
        #print(i[0])
        values = (word,i[1][0])
        cursor.execute(select_query, values)
        tempp = cursor.fetchall()

        if (len(tempp) == 0):
            pass
        else:
            #print(tempp[0][0])
            ans.append(tempp)
    #x=ans[3][4]
    #print(x)
    return ans

def search_favourite(user_id,word):
    word += '%'
    Query = """select Book_id from library where (state = 2) and User_id = ? """
    values = (user_id)
    cursor.execute(Query,values)
    temp = cursor.fetchall()
    #print(len(temp))
    ans = []
    for i in enumerate(temp):
        select_query = f"Select * from Books where (Name like ?) and ID = ?"
        ##print(i[1])
        values = (word,i[1][0])
        cursor.execute(select_query, values)
        tempp = cursor.fetchall()

        if (len(tempp) == 0):
            pass
        else:
            #print(tempp[0][0])
            ans.append(tempp)
    #x=ans[1]
    #print(x)
    return ans

def add_to_wishlist(user_id,book_id):
    query = f"insert into library (user_id,book_id,state) values (?,?,3)"
    values = (user_id,book_id)
    cursor.execute(query,values)
    conn.commit()

def search_library(user_id,word):
    word += '%'
    Query = """select Book_id from library where (state = 1 or state = 2) and User_id = ? """
    values = (user_id)
    cursor.execute(Query,values)
    temp = cursor.fetchall()
    #print(len(temp))
    ans = []
    for i in enumerate(temp):
        select_query = f"Select * from Books where (Name like ?) and ID = ?"
        #print(i[0])
        values = (word,i[1][0])
        cursor.execute(select_query, values)
        tempp = cursor.fetchall()

        if (len(tempp) == 0):
            pass
        else:
            #print(tempp[0][0])
            ans.append(tempp)
    #x=ans[3][4]
    #print(x)
    return ans

def search_user_store(user_id,word):
    word+='%'
    Query = """select * from Books where ( ID not in (select Book_id from library where user_id = ?) ) and (Name like ?)"""
    values = (user_id,word)
    cursor.execute(Query, values)
    temp = cursor.fetchall()
    return temp

def wish(user_id):
    Query = """select * from Books where ID not in (select Book_id from library where user_id = ?)"""
    values = (user_id)
    cursor.execute(Query,values)
    temp = cursor.fetchall()
    return temp

def store_books():
    Query = """select * from Books"""
    values = ()
    cursor.execute(Query, values)
    temp = cursor.fetchall()
    print(temp[6][1])
    return temp

def search_store(user_id,word):
    word += '%'
    Query = f"Select * from Books where (Name like ?)"
    values = (word)
    cursor.execute(Query,values)
    temp = cursor.fetchall()
    return temp


"""
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
"""
