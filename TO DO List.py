#!/usr/bin/env python
# coding: utf-8

# In[ ]:


tasks = []

def add_task():
    task = input("Enter Your Task:")
    tasks.append(task)
    print("----Task Added Successfully----")

def view_task():
    if len(tasks) == 0:
        print("There is no Task")
    else:
        print("The list of task:")
        for i,task in enumerate(tasks):
            print(f"{i+1}.{task}")
        
def delete_task():
    if len(tasks) == 0:
        print("There is no Task")
    else:
        print("The list of task:")
        for i,task in enumerate(tasks):
            print(f"{i+1}.{task}")
        choice = int(input("Enter Task Number to delete:"))
        
        if 0 < choice < len(tasks):
            del tasks[choice-1]
            print("----Task Successfully deleted----")
        else:
            print("----Invalid Task Number----")

def main():
    while True:
        print("----Welcome TO-DO List Application----")
        print("1. Add Task")
        print("2. View Task")
        print("3. Delete Task")
        print("4. Exit") 
       
        choice = int(input("Enter Your Choice:"))
    
        if choice == 1:
            add_task()
    
        elif choice == 2:
            view_task()
    
        elif choice == 3:
            delete_task()
    
        elif choice == 4:
            print("---Thanks For Using TO DO list---")
            break
    
        else:
            print("---Invalid Choice---")

if __name__ == "__main__":
    main()
    


# In[ ]:




