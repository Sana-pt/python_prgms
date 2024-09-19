d1=[]
while True:
    print(" TASK MENU DRIVEN\n1.ADD TASK\n2.VIEW ALL TASKS\n3.UPDATE TASK\n4.MARK TASK AS COMPLETED\n5.DELETE TASK\n6.SEARCH TASK BY NAME\n7.EXIT\n")
    choice=int(input("Enter your choice: "))
    if choice==1:
        task_name = input("Enter task name: ")
        for task in d1:
            if task['name']==task_name:
                print("Name exists.Enter another name.")
                break
        else:
            description = input("Enter task description: ")
            due_date = input("Enter due date: ")
            priority = input("Enter priority(High, Medium, Low): ")
            task={"name":task_name,"description":description,"due_date":due_date,"priority":priority,"completed":False}
            d1.append(task)
            print("TASK SUCCESSFULLY ADDED")
    elif choice==2:
        if not d1:
            print("No tasks.")
        else:
            for task in d1:
                print(f"Task Name:{task['name']}")
                print(f"Description:{task['description']}")
                print(f"Due Date:{task['due_date']}")
                print(f"Priority:{task['priority']}")
                print(f"completed:{'Yes ' if task['completed']else'No'}")  
                print()
    elif choice==3:
        task_name=input("Enter task name to update: ")
        for task in d1:
            if task['name']==task_name:
                new_name=input("Enter new task name: ")
                for n in d1:
                    if n['name']==new_name:
                        print("New task name exists.Enter another new name.")
                        break
                else:
                    new_description=input("Enter new task description: ")
                    new_due_date=input("Enter new due date: ")
                    new_priority = input("Enter new priority(High, Medium, Low): ")

                    task['name']=new_name
                    task['description']=new_description
                    task['due_date']=new_due_date
                    task['priority']=new_priority
                    print("Successfully updated task")
                    break
        else:
            print("Invalid")
    elif choice==4:
        task_name=input("Enter task name to mark as completed: ")
        for task in d1:
            if task['name']==task_name:
                task['completed']=True
                print(f"completed task {task_name}")
                break
        else:
            print("Invalid")
    elif choice==5:
        task_name=input("Enter task name to dlt: ")
        for task in d1:
            if task['name']==task_name:
                d1.remove(task)
                print(f"task {task_name} deleted successfully")
                break
        else:
            print("Invalid")
    elif choice==6:
        task_name=input("Enter task name to search: ")
        for task in d1:
            if task['name']==task_name:
                print(f"Task Name:{task['name']}")
                print(f"Description:{task['description']}")
                print(f"Due Date:{task['due_date']}")
                print(f"Priority:{task['priority']}")
                print(f"completed:{'Yes ' if task['completed']else'No'}") 
                break
        else:
            print("Invalid")
    elif choice==7:
        print("Exit")   
        break
    else:
        print("Invalid")