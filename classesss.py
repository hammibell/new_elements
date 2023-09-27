from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.geometry("500x500")
root.title("New Elements with the Class function")

list1 = ["Label", "Button", "Dropdown"]

dropdown = ttk.Combobox(root, values = list1, state = "readonly")
dropdown.pack()
selected_var = StringVar()


class CreateElements():
    
    def __init__(self):
        print("this is CreateElements class")
        
    def createNewElements():
        element = dropdown.get()
        
        if element == "Label":
            
            
            def createNewElement1(self):
        
              label = Label(root, text = "A new label has been created using class", fg = "red")
              label.pack()
                
        if element == "Button":
                    
            def createNewElement2(self):
                
                btn = Button(root, text = "Button", padx = 20, pady = 10, command = self.showmsg)
                btn.pack()
                
                
        if element == "Dropdown":
             def createNewElement3(self):
                  
                 random = ["1", "2", "3", "4"]
                 seelcted_var2 = StringVar()
                 dropdown1 = ttk.Combobox(root, values = random)
                 element1 = dropdown1.get()
                 dropdown1.pack()
               
        if element1 == element1 <=4:
            
            messagebox.showinfo("Alert", "You clicked on a dropdown menu from Classes")
                   
                                   
        if element == "Dropdown":
            
             def createNewElement4(self):
                random = ["1", "2", "3", "4"]
                seelcted_var2 = StringVar()
                element1 = dropdown1.get()
                dropdown2 = ttk.Combobox(root, values = random)
                dropdown2.pack()
                
        if element1 == element1 <=4:
                    messagebox.showinfo("Alert", "You clicked on a dropdown menu from Classes")
                    
    
def showmsg(self):
    messagebox.showinfo("Alert", "You clicked on a button using Classes")

create_elements = CreateElements()
btn3 = Button(root, text = "Create Element", padx = 30, pady = 20, command = create_elements.createNewElements)
btn3.pack()                   
root.mainloop()
        
        

      
        
def showmsg(self):
        messagebox.showinfo("Alert", "You created new elements using the Class Functionality")
    
createNewElements = CreateElements()


btn_create = Button(root, text = "Click to create label and button element", padx = 30, pady = 20, command = createNewElements.createNewElement)
btn_create.pack()



root.mainloop()
