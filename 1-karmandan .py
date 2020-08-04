import mysql.connector

#connecting to database 
cnx = mysql.connector.connect( user = 'root' , password = '' , host = '127.0.0.1' , database ='mydatabase')

#define a cursor
cursor = cnx.cursor()

query = "SELECT * FROM karmandan;"
cursor.execute(query)

karmandan_list = []

karmandan = cursor.fetchall()

#add database data to a list
for x in karmandan:
    karmandan_list.append(x)

#sort commands
for i in range( len(karmandan_list) ) :

    for j in range( i+1 , len(karmandan_list) ) : 

        if karmandan_list[i][2] > karmandan_list[j][2] :
            pass

        if karmandan_list[i][2] == karmandan_list[j][2] :
            
            if karmandan_list[i][1] > karmandan_list[j][1] :
                karmandan_list[i] , karmandan_list[j] = karmandan_list[j] , karmandan_list[i]

        if karmandan_list[i][2] < karmandan_list[j][2] :
            karmandan_list[i] , karmandan_list[j] = karmandan_list[j] , karmandan_list[i] 


for i in range ( len (karmandan_list) ) :
    print(karmandan_list[i][0],karmandan_list[i][2],karmandan_list[i][1])