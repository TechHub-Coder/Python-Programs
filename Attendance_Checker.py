import sqlite3

#Entering the attendance list obtained from Meet

def list_Entry(list,db_file):
    
    conn=sqlite3.connect(db_file)
    cur=conn.cursor()

#Reading the names from the text file entered

    file_data = [i.strip('\n').split(',') for i in open(list)]
    tempData = [[str(a), *b] for a, *b in file_data] 
    print(tempData)
    attendanceList=[]
    for i in tempData:
        for j in i:
                 attendanceList.append(j)
                 print(j)
                 
#Checking database to find absentees names

    cur.execute("DROP TABLE IF EXISTS attendee_List")
    cur.execute("CREATE TABLE attendee_List (stud_name text)")
    query= "INSERT INTO attendee_List(stud_Name) VALUES(?);"
    for row in attendanceList:
        cur.execute(query, [row])
    conn.commit()
    
    cur.execute("SELECT stud_Name FROM attendee_List")

#Main function

def main():
    db_file = input("Enter the DataBase name: \n")
    list = input("Enter the List obtained from Meet: \n")
    conn = sqlite3.connect(db_file)         
    cur = conn.cursor()
    list_Entry(list,db_file)

    print("\n===========================\n");
    print("Absentees of A Batch:\n")
    cur.execute("SELECT name FROM a_batch EXCEPT SELECT stud_Name FROM attendee_List ")
    rows=cur.fetchall()
    for row in rows:
        print(row)
    print("\n---------------------------\n");
    
    print("Absentees of B Batch:\n")
    cur.execute("SELECT name FROM b_batch EXCEPT SELECT stud_Name FROM attendee_List ")
    rows=cur.fetchall()
    for row in rows:
        print(row)
    print("\n---------------------------\n");

    print("Unidentified Attendees:\n")
    cur.execute("SELECT stud_Name FROM attendee_List EXCEPT SELECT name FROM (SELECT name FROM a_batch UNION SELECT name FROM b_batch)")
    rows=cur.fetchall()
    for row in rows:
        print(row)
    print("\n===========================\n");
if __name__ == '__main__':
    
    main()