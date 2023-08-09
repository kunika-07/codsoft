from  tkinter import * 
import tkinter.messagebox

def entertask():
    
    input_text=""
    def add():
        input_text=entry_task.get(1.0, "end-1c")     
        if input_text=="":
            tkinter.messagebox.showwarning(title="Warning!",message="Please Enter some Text")
        else:
            listbox_task.insert(END,input_text)
            #close the root1 window
            root1.destroy()
    root1=Tk()
    root1.title("Add task")
    entry_task=Text(root1,width=25,height=3)
    entry_task.pack()
    button_temp=Button(root1,text="Add task",command=add)
    button_temp.pack()
    root1.mainloop()
    

#function to facilitate the delete task from the Listbox
def deletetask(): 
    selected=listbox_task.curselection()
    listbox_task.delete(selected[0])


def markcompleted():
    marked=listbox_task.curselection()
    temp=marked[0]              #store the text of selected item in a string
    temp_marked=listbox_task.get(marked)        #update it 
    temp_marked=temp_marked+" ✔"
    #delete it then insert it 
    listbox_task.delete(temp)
    listbox_task.insert(temp,temp_marked)

window=Tk()
window.title("To-Do List APP")

#frame container having different widgets
frame_task=Frame(window)
frame_task.pack()

#listbox
listbox_task=Listbox(frame_task,bg="skyblue",fg="black",height=6,width=50,font = "TimesNewRoman")  
listbox_task.pack(side=tkinter.LEFT)

#Scrolldown
scrollbar_task=Scrollbar(frame_task)
scrollbar_task.pack(side=tkinter.RIGHT,fill=tkinter.Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)   #. The command option is used to associate a function or method that will be called when the scrollbar is moved.
#Button widget 
entry_b=Button(window,text="Add the task",width=50,command=entertask)
entry_b.pack(pady=3)

delete_b=Button(window,text="Delete selected task",width=50,command=deletetask)
delete_b.pack(pady=3)

mark_b=Button(window,text="Mark as completed ",width=50,command=markcompleted)
mark_b.pack(pady=3)


window.mainloop()

