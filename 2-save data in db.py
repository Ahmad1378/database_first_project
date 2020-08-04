import re
import mysql.connector

def isemail(input):

    """check whether input email is valid or not"""

    first_slice = re.findall( r"(^.*)@" , input )
    second_slice = re.findall( r"@(.*)\." , input)
    third_slice = re.findall( r"\.(.*)" , input )

    if len(first_slice) == 0 or len(second_slice) == 0 or len(third_slice) == 0 :
        return False
    elif len (re.findall( r"\d" , second_slice[0] )) != 0 or len (re.findall( r"\d" , third_slice[0] )) != 0 :
        return False
    elif len (re.findall( r"(\s)" , input )) != 0:
        return False
    else:
        return True


input_username = str( input("enter your email address as your username :") )
input_password = str( input("enter your password :") )

#create a connection ro database
cnx = mysql.connector.connect( user = 'root' , password = 'ahmad2233912' , 
                                    host = '127.0.0.1' , database = 'mydatabase')

cursor = cnx.cursor()

while isemail (input_username) == False :
    print ("The username is not valid please enter a valid email . The correct pattern is expression@string.string . Please try again .")
    input_username = str( input("enter your email address as your username :") )
    input_password = str( input("enter your password :") )

query = 'INSERT INTO email VALUES (%s , %s);'
values = (input_username,input_password)

cursor.execute(query,values)
cnx.commit()
print ("Thanks its done .")

cnx.close()
