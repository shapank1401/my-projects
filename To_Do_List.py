import sqlite3
import time

def create_table():
    conn=sqlite3.connect("tasks.db")
    cursor=conn.cursor()
    cursor.execute(""" Create Table IF NOT EXISTS tasks(
                    id Integer PRIMARY KEY AUTOINCREMENT,
                    task TEXT NOT NULL,
                    status TEXT NOT NULL DEFAULT 'Pending'
                    )""")

    conn.commit()
    conn.close()


def add_task(task):
    create_table()
    conn=sqlite3.connect("tasks.db")
    cursor=conn.cursor()
    cursor.execute("INSERT INTO tasks (task) VALUES (?)",(task,))
    conn.commit()
    conn.close()
    print("\nTask added successfully!\n")
    

def view_task():
    create_table()
    conn=sqlite3.connect("tasks.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * from tasks")
    tasks=cursor.fetchall()
    conn.close()
    if tasks:
        print("\nYour To-Do List :")
        for task in tasks:
            print(f"ID: {task[0]} | Task : {task[1]} | Status : {task[2]}")
            
    else:
        print("\nNo tasks found!")
    print("\n")

def delete_task(task_id):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id from tasks")
    ids=cursor.fetchall()
    id_list = [row[0] for row in ids]

    if int(task_id) in id_list:
        cursor=conn.cursor()
        cursor.execute("DELETE from tasks WHERE id=?",(task_id,))
        conn.commit()
        conn.close()
        print("\nTask deleted successfully!\n")
    else:
        print("\nNo data found. Please enter correct ID.\n")
   # seq()
   
   
    
#def seq():
    #conn=sqlite3.connect("tasks.db")
    #cursor=conn.cursor()
   # cursor.execute("ALTER TABLE tasks AUTO_INCREMENT = 1")
   # conn.commit()
   # conn.close()
    
def drop_task():
    conn=sqlite3.connect("tasks.db")
    cursor=conn.cursor()
    cursor.execute("DROP TABLE tasks")
    conn.commit()
    conn.close()
    print("\nContents from Table removed successfully!\n")
    
def update_task(task_id):
    
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id from tasks")
    ids=cursor.fetchall()
    id_list = [row[0] for row in ids]

    if int(task_id) in id_list:
        cursor=conn.cursor()
        cursor.execute("UPDATE tasks SET status='Completed' WHERE id=?",(task_id,))
        conn.commit()
        conn.close()
        print("\nTask Marked as Completed successfully!\n")
    else:
        print("\nNo data found. Please enter correct ID.\n")
    
def todo():
    create_table()
    while True:
        print("""To-Do List App
        Enter 1 to ADD Task.
        Enter 2 to VIEW ALL Tasks.
        Enter 3 to DELETE ANY Task.
        Enter 4 to UPDATE Task as COMPLETED.
        Enter 5 to Clear Table.
        Enter 6 to EXIT
        """)
        choice=input("\nPlease select an option : ")
        
        if choice == "1":
            task=input("\nEnter Task : ")
            add_task(task)
        elif choice == "2":
            view_task()
        elif choice == "3":
            ID=input("\nEnter the Task ID you want to delete : ")
            if ID.isdigit():
                delete_task(int(ID))    
            else:
                print("\nPlease enter correct ID.\n")
        elif choice == "4":
            ID=input("\nEnter the Task ID you want to update : ")
            if ID.isdigit():
                update_task(int(ID))
            else:
                print("\nPlease enter correct ID.\n")
        elif choice == "5":
            drop_task()
        elif choice == "6":
            print("\nExiting the App. Goodbye!")
            time.sleep(3)
            break
        else:
            print("\nPlease enter valid input\n.")
         

if __name__ == "__main__":
    todo()