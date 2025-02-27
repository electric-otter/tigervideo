import tkinter as tk
import os
newproject = tk.Tk()
folder_name = "project"
file_name = "myproject.tvid"
file_path = os.path.join(folder_name, file_name)

def create():
  if not os.path.exists(folder_name):
    os.makedirs(folder_name)
  os.chdir(path)
newproject.title("TigerVideo - Start an fresh project.")
createbutton = tk.Button(newproject, text="Start now", command=create)
createbutton()
newproject.mainloop()
