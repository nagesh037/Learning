from tabulate import tabulate
from json import loads,dumps
import datetime
import argparse

def add_task(tasks):
    data = {}
    task_name = input("Enter the task Name:")
    data['Id'] = len(tasks) + 1
    data['Task'] = task_name
    data['Date(YYYY/MM/DD)'] = str(datetime.datetime.now().strftime("%Y-%m-%d"))
    data['Completed?'] = False
    return data

def view_task(tasks):
    if len(tasks) == 0:
        print("Please add the task")
        return None
    cols = tasks[0].keys()
    rows = [x.values() for x in tasks]
    table = tabulate(rows,cols,tablefmt='grid')
    print(table)

def edit_task(tasks):
    id_com = 0
    if len(tasks) == 0:
        print("No task to edit")
        return None
    try:
        id_com = int(input("Enter the id to edit task name:"))
    except ValueError:
        print("Please enter a valid Id number")
    if id_com > len(tasks):
        print("The index is out of range")
        return None
    update_name = input("Enter the updated name:")
    tasks[id_com - 1 ]["Task"] = update_name
    print("Task name Updated")
    save_file(tasks)
    view_task(tasks)

def mark_task(tasks):
    id_com = 0
    if len(tasks) == 0:
        print("No task to mark")
        return None
    try:
        id_com = int(input("Enter the id to mark the task:"))
    except ValueError:
        print("Please enter a valid Id number")
    if id_com > len(tasks):
        print("The index is out of range")
        return None
    tasks[id_com - 1]["Completed?"] = True
    print("The task completed Congrats:)")
    save_file(tasks)
    view_task(tasks)

def save_file(task_list):
    try:
        with open('task.json','w') as json_file:
            data_json = dumps(task_list,indent=2)
            json_file.write(data_json)
    except FileNotFoundError as err:
            print("I think the Task.json file is missing:()")

def main():
    task_list = []
    choice = 0
    
    try:
        with open("task.json",'r+') as json_file:
            data_json = json_file.read()
            task_list = loads(data_json)
    except FileNotFoundError as err:
        pass

    parser = argparse.ArgumentParser(description="This is command line tool to add the task and manage them")

    parser.add_argument('-a',"--add",action='store_true',help="You add the task")
    parser.add_argument('-v',"--view",action='store_true',help="View your task")
    parser.add_argument('-m','--mark',action='store_true',help="You can mark your task as complete")
    parser.add_argument('-e','--edit',action="store_true",help="You can edit your tasks")

    args = parser.parse_args()

    if args.view:
        view_task(task_list)
    if args.add:
        add_task(task_list)
    if args.mark:
        mark_task(task_list)
    if args.edit:
        edit_task(task_list)

    print("Welcome to Tabulate Task")
    while(True):
        print("1.Add the task")
        print("2.View the task")
        print("3.Edit the task")
        print("4.Mark the task as completed")
        print("5.Quit")
        try:
            choice = int(input("Enter the choice:"))
        except ValueError:
            print("Please enter only integer values that is shown as above")
        if choice == 1:
            temp_data = add_task(task_list)
            task_list.append(temp_data)
            save_file(task_list)
            print("Task added successfully")
        elif choice == 2:
            view_task(task_list)
        elif choice == 3:
            edit_task(task_list)
        elif choice == 4:
            mark_task(task_list)
        elif choice == 5:
            print("Thank you for using our Task Tabulator:)")
            break

if __name__ == '__main__':
    main()