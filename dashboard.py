from tkinter import *
from PIL import Image, ImageTk

class MITSHSTOCK:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")

        try:
            image = Image.open("images/trolly.png")  
            resized_image = image.resize((70, 70), Image.Resampling.LANCZOS)
            self.icon_title = ImageTk.PhotoImage(resized_image)
        except Exception as e:
            print(f"Error loading image: {e}")
            self.icon_title = None

        title = Label(
            self.root,
            text="Inventory Management System",
            image=self.icon_title if self.icon_title else None,
            compound="left",
            font=("times new roman", 40, "bold"),
            bg="#010c48",
            fg="white",
            anchor="w"
        )
        title.place(x=0, y=0, relwidth=1, height=70)

        # logout button
        btn_logout = Button(self.root,
        text="Logout", 
        font=("times new roman", 15, "bold"),
        bg="yellow",
        cursor="hand2").place(x=1100,y=10,height=50, width=150)

        #clock
        self.lbl_clock = Label(self.root, text="Welcome to Inventory Management System\t\t Date: DD-MM_YYY\t\t Time: HH:MM:SS",
            font=("times new roman", 15, "bold"),
            bg="#4d636d",
            fg="white",
        )
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30) 

        # Left Menu
        self.MenuLogo=Image.open("images/purchs_prcss.jpg")
        self.MenuLogo = self.MenuLogo.resize((200,200),Image.Resampling.LANCZOS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)
        LeftMenu = Frame(self.root, 
        bd=2, 
        relief=RIDGE,
        bg="white")

        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)
        LeftMenu.place(x=0, y=102, width=200,height=565)
        

root = Tk()
obj = MITSHSTOCK(root)
root.mainloop()
