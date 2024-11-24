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

        LeftMenu.place(x=0, y=102, width=200,height=565)

        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)

        # Menue
        try:
            arrow_image = Image.open("images/arrow.png")  # Load arrow image
            resized_arrow = arrow_image.resize((20, 20), Image.Resampling.LANCZOS)  # Resize to smaller dimensions
            self.side_icon = ImageTk.PhotoImage(resized_arrow)  # Convert to PhotoImage
        except Exception as e:
            print(f"Error loading arrow image: {e}")
            self.side_icon = None

        lbl_menu= Label(LeftMenu,
        text="Menu", 
        font=("times new roman", 20),
        bg="#009688").pack(side=TOP, fill=X)

        #employee
        btn_employee= Button(LeftMenu,
        text="Employee", 
        image=self.side_icon if self.side_icon else None,
        compound=LEFT,  
        padx=5,
        anchor="w",      
        font=("times new roman", 20),
        bg="white", 
        bd=3,
        cursor="hand2").pack(side=TOP, fill=X)

        #Category
        btn_category= Button(LeftMenu,
        text="Category", 
        image=self.side_icon if self.side_icon else None,
        compound=LEFT,  
        padx=5,
        anchor="w",      
        font=("times new roman", 20),
        bg="white", 
        bd=3,
        cursor="hand2").pack(side=TOP, fill=X)

        #projucts
        btn_projects= Button(LeftMenu,
        text="Projucts", 
        image=self.side_icon if self.side_icon else None,
        compound=LEFT,  
        padx=5,
        anchor="w",      
        font=("times new roman", 20),
        bg="white", 
        bd=3,
        cursor="hand2").pack(side=TOP, fill=X)


        #Sales
        btn_sales= Button(LeftMenu,
        text="Sales", 
        image=self.side_icon if self.side_icon else None,
        compound=LEFT,  
        padx=5,
        anchor="w",      
        font=("times new roman", 20),
        bg="white", 
        bd=3,
        cursor="hand2").pack(side=TOP, fill=X)

        #Exit
        btn_exit= Button(LeftMenu,
        text="Exit", 
        image=self.side_icon if self.side_icon else None,
        compound=LEFT,  
        padx=5,
        anchor="w",      
        font=("times new roman", 20),
        bg="white", 
        bd=3,
        cursor="hand2").pack(side=TOP, fill=X)



#       Content
        self.lbl_employee=Label(self.root,text="Total Employee\n[ 0 ]",bd=5,relief=RIDGE, bg="#33bbf9",fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_employee.place(x=300, y=120, height=150, width=300)

        self.lbl_supplier=Label(self.root,text="Total Employee\n[ 0 ]", bg="#4C5866",bd=5,relief=RIDGE,fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_supplier.place(x=650, y=120, height=150, width=300)

        self.lbl_category=Label(self.root,text="Total Category\n[ 0 ]", bg="#614051",bd=5,relief=RIDGE,fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_category.place(x=1000, y=120, height=150, width=300)

        self.lbl_products=Label(self.root,text="Total Projucts\n[ 0 ]", bg="#30A667",bd=5,relief=RIDGE, fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_products.place(x=300, y=300, height=150, width=300)

        self.lbl_Sales=Label(self.root,text="Total Sales\n[ 0 ]", bg="#872657",bd=5,relief=RIDGE, fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_Sales.place(x=650, y=300, height=150, width=300)


         #footer
        self.lbl_footer = Label(self.root, text="MitshStock- Inventory Management System\n For any Technical issues \ncontact: 0648363423",
            font=("times new roman", 12, "bold"),
            bg="#4d636d",
            fg="white",
        ).pack(side=BOTTOM, fill=X)        

root = Tk()
obj = MITSHSTOCK(root)
root.mainloop()
