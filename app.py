import tkinter as tk
from tkinter import filedialog, Menu, Text
import os

root = tk.Tk()
root.title("Favarite Apps")

apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]
        # check if it opens saved programs
        # print(tempApps)
        
def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("Executables", "*.exe"), ("All files", "*.*")))
    apps.append(filename)
    # print("filename is:", filename)
    for app in apps:
        label=tk.Label(frame, text=app, bg="gray", font=("Arial", 12))
        label.pack()

def runApp():
    for app in apps:
        os.startfile(app)

# Menu and Submenu
menubar = Menu(root)

fileMenu = Menu(menubar, tearoff=0)
fileMenu.add_command(label="Create new Session", command=addApp)
fileMenu.add_command(label="Open/Run Apps", command=runApp)
fileMenu.add_command(label="Save")
fileMenu.add_command(label="Save as...")
fileMenu.add_command(label="Close")

fileMenu.add_separator()

fileMenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=fileMenu)
editMenu = Menu(menubar, tearoff=0)
editMenu.add_command(label="Undo")

editMenu.add_separator()

editMenu.add_command(label="Cut")
editMenu.add_command(label="Copy")
editMenu.add_command(label="Paste")
editMenu.add_command(label="Delete")
editMenu.add_command(label="Select All")

menubar.add_cascade(label="Edit", menu=editMenu)
helpMenu = Menu(menubar, tearoff=0)
helpMenu.add_command(label="Help Index")
helpMenu.add_command(label="About...")
menubar.add_cascade(label="Help", menu=helpMenu)
# End of menubar and menu Items

# pack is used to show objects in the window
canvas = tk.Canvas(root, height=400, width=1000, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relheight=0.7, relwidth=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=addApp)
openFile.pack(side="right")

runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#263D42", command=runApp)
runApps.pack(side="right")

for app in apps:
    label = tk.Label(frame, text=app, font=("Arial", 12))
    label.pack()

root.config(menu=menubar)
root.mainloop()
#  save the details for future open
with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
