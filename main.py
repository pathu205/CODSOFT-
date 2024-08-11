import tkinter as tk
from tkinter import *

root = Tk()
root.title("To-Do List")
root.geometry("400x550+400+100")
root.resizable(False, False)

task_list = []

def addTask():
    task = task_add.get()
    task_add.delete(0, END)

    if task:
        task_list.append(task)
        with open("tasklist.txt", 'a') as taskfile:
            taskfile.write(f"{task}\n")
        listbox.insert(END, task)

def deleteTask():
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt", "w") as taskfile:
            for task in task_list:
                taskfile.write(f"{task}\n")

        listbox.delete(ANCHOR)

def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            task = task.strip()
            if task:
                task_list.append(task)
                listbox.insert(END, task)
    except FileNotFoundError:
        file = open("tasklist.txt", "w")
        file.close()

def updateTask():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        new_task = task_add.get()
        old_task = listbox.get(selected_task_index)

        if new_task:
            task_list[selected_task_index[0]] = new_task
            with open("tasklist.txt", "w") as taskfile:
                for task in task_list:
                    taskfile.write(f"{task}\n")

            listbox.delete(selected_task_index)
            listbox.insert(selected_task_index, new_task)

            task_add.delete(0, END)

def selectTask(event):
    selected_task_index = listbox.curselection()
    if selected_task_index:
        task_add.delete(0, END)
        task_add.insert(0, listbox.get(selected_task_index))

# Title
heading = Label(root, text="YOUR TASKS", font="Arial 20 bold", fg="white", bg='orange')
heading.place(x=110, y=20)

# Task Addition Space
frame = Frame(root, width=400, height=50, bg="sky blue")
frame.place(x=0, y=90)

task = StringVar()
task_add = Entry(frame, width=18, font="Arial 20", bd=0, textvariable=task)
task_add.place(x=10, y=7)
task_add.focus()

button = Button(frame, text="ADD", font="Arial 20 bold", width=6, bg="orange", fg="#fff", bd=0, command=addTask)
button.place(x=287, y=0)

# List of Tasks
frame1 = Frame(root, bd=3, width=700, height=20, bg="orange")
frame1.pack(pady=(160, 0))

listbox = Listbox(frame1, font=("Arial", 12), width=40, height=16, bg="sky blue", fg="white", cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Bind the selectTask function to the Listbox
listbox.bind('<<ListboxSelect>>', selectTask)

openTaskFile()

# To delete the task 
delete_button = Button(root, text="DELETE", font="Arial 20 bold", width=6, bg="orange", fg="#fff", bd=0, command=deleteTask)
delete_button.place(x=60, y=480)

# Update Task Button 
update_button = Button(root, text="UPDATE", font="Arial 20 bold", width=6, bg="orange", fg="#fff", bd=0, command=updateTask)
update_button.place(x=220, y=480)

root.mainloop()