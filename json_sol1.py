# Backend_developer_assignment

con=sqlite3.connect('emp.db')   #establishing connection to the database
if __name__=="__main__": #executing the db_create.py only when the database is not present
    cursor.execute('''CREATE TABLE EMPLOYEES(
                emp_id INTEGER NOT NULL,
                emp_name TEXT NOT NULL,
                manager_name TEXT )''')
    con.commit()

def update(a,b,c):  #fuction to update the database, a=emp_id, b=emp_name, c= manager_name
    con = sqlite3.connect('emp.db')
    flag=0
    ceo_flag=0  #to check if only one CEO is given in the database
    cur = con.execute("select * from Employees")
    i=()
    for i in cur:
        if i[2]=="":
            ceo_flag+=1
            break
        if a==i[0] or b==i[1]: #to check if an employee data is already in the database
            flag=1
            break
    if flag==1:
        print("Employee details already exist!")
        print(*i)   #printing employee details of the the existing employee for cross reference
    elif ceo_flag==1:
        print("CEO already exists in the records!")
        print(*i)   #printing the existing CEO details in the database for cross reference
    else:
        s="INSERT INTO EMPLOYEES Values ({},'{}','{}')"
        con.execute(s.format(a,b,c))
        con.commit()
    con.close()


def display():  #printing the database is json string form
    con = sqlite3.connect('emp.db')
    l=[]
    cur=con.execute("select * from Employees")
    for i in cur:
        dict1 = {}
        dict1["emp_id"]=i[0]
        dict1["emp_name"]=i[1]
        dict1["manager_name"]=i[2]
        l.append(dict1)
    s=json.dumps(l,indent=2)
    print(s)
    con.close()

def delete(a):  #delete by employee id
    con = sqlite3.connect('emp.db')
    if a=="*": #use star to delete every entry in the table
        con.execute("delete from EMPLOYEES")
        con.commit()
    else:
        s="delete from EMPLOYEES where emp_id={}"
        con.execute(s.format(a))
        con.commit()
    display()

con.close()


