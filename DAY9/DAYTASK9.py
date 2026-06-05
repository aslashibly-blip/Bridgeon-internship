from typing import Dict,List,Any
class TaskNotFoundError(Exception):
    pass
class InvalidTaskDataError(Exception):
    pass

tasks:Dict[int,Dict[str,Any]]={}
next_id:int=1

def get_all_tasks()->List[Dict[str,Any]]:
    return list(tasks.values())

def get_task(id:int)->Dict[str,Any]:
    if id not in tasks:
        raise TaskNotFoundError("Task not found")
    return tasks[id]

def validate_task_data(data:Dict[str,Any])->None:
    if"title" not in data or data["title"].strip()=="":
        raise InvalidTaskDataError("Title is required")
    
    if"completed" in data and type(data["completed"]) is not bool:
        raise InvalidTaskDataError("Completed must be True or False")
    
def create_task(data:Dict[str,Any])->Dict[str,Any]:
    global next_id

    validate_task_data(data)

    task={
        "id":next_id,
        "title":data["title"],
        "completed":data.get("completed",False)
    }

    tasks[next_id]=task
    next_id+=1

    return task

def update_task(id:int,data:Dict[str,Any])->Dict[str,Any]:
    if id not in tasks:
        raise TaskNotFoundError("Task not found")
    
    validate_task_data(data)

    tasks[id]["title"]=data["title"]
    tasks[id]["completed"]=data.get("completd",tasks[id]["completed"])

    return tasks[id]

def delete_task(id:int)->bool:
    if id not in tasks:
        raise TaskNotFoundError("Task not found")
    
    del tasks[id]
    return True

def show_menu()->None:
    print("\n====TASK CRUD MENU====")
    print("1.view all tasks")
    print("2.view one task")
    print("3.create task")
    print("4.update task")
    print("5.delete task")
    print("6.Exit")

while True:
    show_menu()

    choice=input("Enter your choice")
    try:
        if choice=="1":
            all_tasks=get_all_tasks()

            if not all_tasks:
                print("No tasks found")
            else:
                for task in all_tasks:
                    print(task)

        elif choice=="2":
            task_id=int(input("Enter task id:"))
            task=get_task(task_id)
            print(task)

        elif choice=="3":
            title=input("Enter task title")

            task_data={
                "title":title,
                "completed":False
             }
            
            new_task=create_task(task_data)
            print("Task created:",new_task)

        elif choice=="4":
            task_id=int(input("Enter task_id :"))
            title=input("Enter new title:")
            completed_input=input("is completed? yes/no:").lower()

            completed=completed_input=="yes"

            updated_data={
                "title":title,
                "completed":completed
            }

            updated_task=update_task(task_id,updated_data)
            print("task updated:",new_task)
        elif choice=="5":
            task_id=int(input("enter task id:"))
            delete_task(task_id) 
            print("task deleted successfully.")
        elif choice=="6":
            print("existing program...")
            break
        else:
          print("invalid choice.pleace try again.")
    except TaskNotFoundError as e:
      print("Erorr:",e)
    except InvalidTaskDataError as e:
     print("Erorr:",e)
    except ValueError:
        print("Error:please enter a valid number")




                
    
            
        