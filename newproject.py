import tkinter
import os
newproject = tkinter.Tk()
folder_name = "project"
file_name = "myproject.tvid"
file_path = os.path.join(folder_name, file_name)

def create():
  if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    
root.title("TigerVideo - Start an fresh project.")
turn_off = tk.Button(root, text="Start now", command=create)
newproject.mainloop()
