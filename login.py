#=====================================================IMPORT REQURIED MODULES FROM TKINTER=====================================================================
from tkinter import *                #this is to import required from tkinter
from tkinter import messagebox       #Imported message box
import mysql.connector               #Imported mysql connector for connecting to database
#====================================================CONNECTING TO DATABASE OF MYSQL==========================================================================
#The below are details of my data base 
mb=mysql.connector.connect(
host="localhost",                   #host name for mysql
user="praveen",                     #my user name for mysql
password="Praveen@9",               #my password to open and work with mysql
database="cab")                     #name of  my data base created 
mycursor=mb.cursor()
#====================================================CREATING OF TABLES IN DATABASE============================================================================

#Created my first table in cab database to store and show user details
#mycursor.execute("create table userdetails (First_Name varchar(255), Last_Name varchar(255), Mobile_Number varchar(255),gender varchar(255),email varchar(255),password varchar(255))")
#Created my second table in cab database to store and show bookings of the user
#mycursor.execute("create table mybookings (Name varchar(255), Age int, Mobile_Number varchar(30), gender varchar(255),Hours int,Min int, Avenue varchar(255), Car_Name varchar(255))")

#================================================VERIFY EMAIL ID AND PASSWORD IN LOGIN==========================================================================
def submit():       #Function to verify email and password
    mycursor.execute("select email,password from userdetails")    #selects email,password from userdetails
    x=mycursor.fetchall()           #fetches the selected
    mail=Email.get()                #gets email from table
    key=Password.get()              #gets password from table

    if(len(mail)==0 or len(key)==0):         #checks if the email and password are entered
        messagebox.showinfo("!!ERROR!!", "PLEASE FILL IN THE DATA")    #displays message box to enter all feilds

    if ('@' not in mail):                    #checks the entered email is correct are not
        messagebox.showinfo("!!ERROR!!", "PLEASE PROVIDE A VALID MAIL ID")  #displays message box  
    else:
        pass
    if(len(key)<6):                 #checks if the password length is less than 6
        messagebox.showinfo("!!ERROR!!","PLEASE ENSURE LENGTH OF PASSWORD(ATLEAST 6)")
    else:
        pass
        
    for i in x:    #checks the email and password in database
        if(mail in i[0]):
            if(key in i[1]):
                mb.commit()     #commit is to execute in database
                main_menu()     #calls the main_memu function
            else:
                messagebox.showinfo("!!ERROR!!","PASSWORD IS INCORRECT")  #checks the password is correct are not
        else:
            pass

#===============================================================SAVE BOOKINGS MADE BY USER================================================================================
def savebookings():   #Function to store or save user bookings in database
    #messagebox.showinfo("Message","Cab Booked Successfully")
#to insert the booking details into the table from tkinter window
    mycursor.execute("insert into mybookings values(%s,%s,%s,%s,%s,%s,%s,%s)", (Name.get(),Age.get(), Mobile_Number.get(), var1.get(), Hours.get(),Mins.get(),clicked.get(),car.get()))
    return messagebox.showinfo("Notification","CAB BOOKED SUCESSFULLY!!!")
#to commit the action done above
    mb.commit()
#to set the values to NULL on the window after they are inserted in the table
    Name.set("")
    Age.set("")
    Mobile_Number.set("")
    Hours.set("")
    Mins.set("")
#=============================================================SHOW BOOKINGS MADE BY USER================================================================================== 
def showbookings():   #Function to show the bookings made by the user on the window
    top6=Toplevel()   #Toplevel is used for creating a new window on the existing window
    top6.title("User Details")     #to set the title of the window
    top6.geometry('1300x700')      #to set the geometry of the window
#Lable is to print some text on the window and palce is position of the lable
    Label(top6,text="YOUR BOOKINGS",font=('georgia 18 bold'),fg='green').place(x=500,y=600)
#executes the command ie; selects all the data in the table mybookings 
    mycursor.execute("select * from mybookings")
#fetches all the selected data from table
    x=mycursor.fetchall()
#BACK button destroys the existing window
    b1=Button(top6,text="BACK",fg="black",bg="white",height=1,width=7,font=('time 10 bold'),relief=RAISED,command=top6.destroy)
    b1.place(x=40,y=530)
#All the below lines are lables used to dispaly text
#grid is same palce but places in the form of rows and columns(in tables)
    Label(top6, text="Name",font=('time 15 bold'),fg='red').grid(row=0, column=0)
    Label(top6, text="Age",font=('time 15 bold'),fg='red').grid(row=0, column=1)
    Label(top6, text="Mobile Number",font=('time 15 bold'),fg='red').grid(row=0, column=2)
    Label(top6, text="Gender",font=('time 15 bold'),fg='red').grid(row=0, column=3)
    Label(top6, text="Hours",font=('time 15 bold'),fg='red').grid(row=0, column=4)
    Label(top6, text="Mins",font=('time 15 bold'),fg='red').grid(row=0, column=5)
    Label(top6, text="Avenue",font=('time 15 bold'),fg='red').grid(row=0, column=6)
    Label(top6, text="Car Name",font=('time 15 bold'),fg='red').grid(row=0, column=7)
    r=1     #initilize c(column) value to 1
    for i in x:     #to print the data from the table in the database on to window
        Label(top6, text=i[0],font=('time 15 bold')).grid(row=r ,column=0)
        Label(top6, text=i[1],font=('time 15 bold')).grid(row=r ,column=1)
        Label(top6, text=i[2],font=('time 15 bold')).grid(row=r ,column=2)
        Label(top6, text=i[3],font=('time 15 bold')).grid(row=r ,column=3)
        Label(top6, text=i[4],font=('time 15 bold')).grid(row=r ,column=4)
        Label(top6, text=i[5],font=('time 15 bold')).grid(row=r ,column=5)
        Label(top6, text=i[6],font=('time 15 bold')).grid(row=r ,column=6)
        Label(top6, text=i[7],font=('time 15 bold')).grid(row=r ,column=7)
        r=r+1     #increment the value of column by one(1)
#========================================================SAVE USER DETAILS TO DATABASE======================================================================
def savedata():        #Function to store or save user bookings in database
#to insert the user details into the table from tkinter window
    mycursor.execute("insert into userdetails values(%s,%s,%s,%s,%s,%s)", (First_Name.get(),Last_Name.get(),mobilenumber.get(),var.get(),Email.get(),Password.get()))
    mb.commit()    #executes the above commands
#--------SETS ALL THE VALUES TO NULL AFTER THEY ARE STORED--------#
    First_Name.set("")
    Last_Name.set("")
    mobilenumber.set("")
    Email.set("")
    Password.set("")
#=======================================================SHOW ALL USER DETAILS ON WINDOW======================================================================
def show():        #function to show the user detailes entered during the registration
    top5=Toplevel()    #creatation of new window
    top5.title("User Details")    #title of the window
    top5.geometry('1300x700')     #window size
#Lable "YOUR DETAILS" which just displays the text on the on the window 
    Label(top5,text="YOUR DETAILS",font=('georgia 18 bold'),fg='white',bg='black').place(x=500,y=600)
#selects all the details in userdetails
    mycursor.execute("select * from userdetails")
#fetch all the data in table
    x=mycursor.fetchall()
#BACK which destroys the existing window
    b1=Button(top5,text="BACK",fg="black",bg="white",height=1,width=7,font=('time 10 bold'),relief=RAISED,command=top5.destroy)
    b1.place(x=40,y=530)
#All the below lines are lables which displays the text over window 
    Label(top5, text="First Name", fg='red',font=('time 15 bold')).grid(row=0, column=0)
    Label(top5, text="Last Name", fg='red',font=('time 15 bold')).grid(row=0, column=1)
    Label(top5, text="Mobile Number", fg='red',font=('time 15 bold')).grid(row=0, column=2)
    Label(top5, text="Gender", fg='red',font=('time 15 bold')).grid(row=0, column=3)
    Label(top5, text="E-mail", fg='red',font=('time 15 bold')).grid(row=0, column=4)
    Label(top5, text="Password", fg='red',font=('time 15 bold')).grid(row=0, column=5)
    r=1   #initlize the value of row by 1(one)
    for i in x:   #for loop to print the details from data base on window
        Label(top5, text=i[0],font=('time 15 bold')).grid(row=r ,column=0)
        Label(top5, text=i[1],font=('time 15 bold')).grid(row=r ,column=1)
        Label(top5, text=i[2],font=('time 15 bold')).grid(row=r ,column=2)
        Label(top5, text=i[3],font=('time 15 bold')).grid(row=r ,column=3)
        Label(top5, text=i[4],font=('time 15 bold')).grid(row=r ,column=4)
        Label(top5, text=i[5],font=('time 15 bold')).grid(row=r ,column=5)
        r=r+1    #increment of the row by one(1)

#============================================================LOGIN PAGE OF THE CAB BOOKING=====================================================================================     
def login():   #function to execute the login page
    top2=Toplevel()    #window of the login page
    top2.title("Login Page")   #title of the window
    top2.geometry('400x400')   #window size
#heading on the top of the window
    Label(top2,text="G-1'S LOGIN",font=('time 15 bold'),fg='blue').place(x=140,y=50)
    user = PhotoImage(file='user.png')
    b1=Button(top2,image=user,border=0)
    b1.place(x=20,y=140)
    lock = PhotoImage(file='password.png')
    b2=Button(top2,image=lock,border=0)
    b2.place(x=20,y=200)
#lable showing text "E-MAIL"
    Label(top2,text="E-MAIL",font=('time 15 bold')).place(x=50,y=140)
#entry box to enter the email
    e1=Entry(top2,bd=5,textvariable=Email)
    e1.place(x=150,y=140)     #position of the entry box
#lable showing text "Password"
    Label(top2,text = 'Password',font = ('time 15 bold')).place(x=50,y=200)
#show ="*" displays the password in the form of stars(*)
    e2=Entry(top2,show = '*',bd=5,textvariable=Password)
    e2.place(x=150,y=200)
#b4 is the login button which allows to login to the home page
    b4=Button(top2,text="Login",fg='white',bg='red',height=1,width=8,font=('time 15 bold'),command=submit)
    b4.place(x=130,y=300)
    top2.mainloop()
        
#======================================================REGISTRATION PAGE FOR CAB BOOKING====================================================================================
root=Tk() #root window
root.title('Cab Booking') #title of the window
root.geometry("1300x700") # window size
#================DEFINING VARIABLES TYPES OF REGISTRATION PAGE===============#
First_Name=StringVar()    
Last_Name=StringVar()     
mobilenumber=StringVar()
Email=StringVar()
Password=StringVar()
#applying canvas to the window
canvas = Canvas(root,width=1300, height=700, bg='white')
canvas.pack()
#inserting image on window with coordinates
cab_4 = PhotoImage(file='background_1.png')
canvas.create_image(0,0, image=cab_4, anchor=NW)
#lable text as heading on the window
Label(root,text="G-1 CABS REGISTRATION",font=('time 20 bold'),fg='black').place(x=410,y=50)
#===========NAMES OF THE ENTRYS IN REGISTRATION============#
Label(root,text=" FIRST NAME ",font=('time 15 bold')).place(x=100,y=150)
Entry(root,textvariable=First_Name,bd=5).place(x=340,y=150)
Label(root,text="LAST NAME",font=('time 15 bold')).place(x=100,y=200)
Entry(root,textvariable=Last_Name,bd=5).place(x=340,y=200)
Label(root,text="MOBILE NUMBER",font=('time 15 bold')).place(x=100,y=250)
Entry(root,textvariable=mobilenumber,bd=5).place(x=340,y=250)
Label(root,text='GENDER',font=('time 15 bold')).place(x=100,y=300)
#RADIO BUTTON FOR GENDER
var=StringVar()
r1=Radiobutton(root,text='MALE',variable=var,value='Male')
r1.place(x=320,y=300)
r1=Radiobutton(root,text='FEMALE',variable=var,value='Female')
r1.place(x=420,y=300)
Label(root,text="E-MAIL",font=('time 15 bold')).place(x=100,y=350)
Entry(root,textvariable=Email,bd=5).place(x=340,y=350)
Label(root,text = 'Password',font = ('time 15 bold')).place(x=100,y=400)
Entry(root,show = '*',textvariable=Password,bd=5).place(x=340,y=400)
#BUTTON FOR REGISTER
Button(root,text="Register",fg='white',bg='green',height=1,width=10,font=('time 12 bold'),command=savedata).place(x=150,y=500)
#BUTTON  FOR GO TO LOGIN
Button(root,text="Go To Login",fg='white',bg='green',height=1,width=12,font=('time 12 bold'),command=login).place(x=300,y=500)
#================DEFINING VARIABLES TYPES OF LOGIN PAGE===============#
Name=StringVar()
Age=IntVar()
Hours=IntVar()
Mins=IntVar()
Mobile_Number=StringVar()
var1=StringVar()
clicked = StringVar()
car = StringVar()
#============================================================CAB BOOKING WINDOW===============================================================================================
def open_window1():  #Function fo booking
    top1=Toplevel()  #new window
    top1.title("Book Cab")  #title of window
    top1.geometry('1300x700') #window size
#canvas to the window
    canvas = Canvas(top1,width=1300, height=700, bg='white')
    canvas.pack()
#insert image on the window    
    cab_4 = PhotoImage(file='background_3.png')
    canvas.create_image(0,0, image=cab_4, anchor=NW)
#=================NAMES OF THE ENTRIES IN LOGIN FORM====================#
    Label(top1,text="CAB BOOKING",font=('time 20 bold'),fg='black').place(x=500,y=70)
    b1=Button(top1,text="BACK",fg="black",bg="white",height=1,width=7,font=('time 10 bold'),relief=RAISED,command=top1.destroy)
    b1.place(x=40,y=530)
    Label(top1, text="Name", font=('georgia 14 bold')).place(x=200, y=130)
    Entry(top1,textvariable=Name,bd=5).place(x=410,y=130)
    Label(top1, text="Age", font=('georgia 14 bold')).place(x=200, y=180)
    Entry(top1,textvariable=Age,bd=5).place(x=410,y=180)
    Label(top1,text='Gender',font=('georgia 14 bold')).place(x=200,y=230)
#Radio button for gender  
    #var1=StringVar()
    r2=Radiobutton(top1,text='MALE',font=('georgia 10 bold'),variable=var1,value='Male')
    r2.place(x=400,y=230)
    r2=Radiobutton(top1,text='FEMALE',font=('georgia 10 bold'),variable=var1,value='Female')
    r2.place(x=500,y=230)
    #clicked = StringVar()
    Label(top1, text="Avenue", font=('georgia 14 bold')).place(x=200, y=280)
    drop = OptionMenu(top1, clicked, "Vijayawad to Rajahmundry", "Vizag to Rajahmundry","Banglore to hyderabad","Delhi to Punjab", "Amritsar to Ludhiana", "LPU to Delhi")
    drop.place(x=410,y=280)
    Label(top1, text="Time", font=('georgia 14 bold')).place(x=200, y=330)
    Label(top1, text="Hours", font=('georgia 14 bold')).place(x=350, y=330)
    Entry(top1,bd=5,width=5,textvariable=Hours).place(x=440,y=330)
    Label(top1, text="Mins", font=('georgia 14 bold')).place(x=500, y=330)
    Entry(top1,bd=5,width=5,textvariable=Mins).place(x=580,y=330)
    Label(top1, text="Mobile Number", font=('georgia 14 bold')).place(x=200, y=380)
    Entry(top1,bd=5,textvariable=Mobile_Number).place(x=410,y=380)
    b1=Button(top1,text="Select Cab",height=1,width=8,font='georgia 12 bold',relief=RAISED,command=cab_select)
    b1.place(x=325,y=450)
    top1.mainloop()
    
#======================================================SELECTING REQUIRED CAB AND BOOK========================================================================================
def cab_select():         #function to show all cabs avaliable
    top3=Toplevel()       #creates a new window 
    top3.title("Cabs")    #title of window
    top3.geometry('1300x700')     
    Label(top3,text="G-1 CABS",font=('georgia 18 bold'),fg='red').place(x=590,y=50) #Heading in the window
#CAR images storing in file
    cab = PhotoImage(file='car.png')    
    cab_1 = PhotoImage(file='Tata Indica.png')  
    cab_2 = PhotoImage(file='swift.png')
    cab_3 = PhotoImage(file='Mahindra scorpio.png')
    cab_4 = PhotoImage(file='Chevrolet Tavera.png')
    cab_5 = PhotoImage(file='innova.png')
    #car = StringVar()
    Label(top3, text="Cabs", font=('georgia 14 bold')).place(x=100, y=100)   #lable to show cab names
#DROP is used to show list of cab names to select
    drop = OptionMenu(top3, car, "Taxi cab","Tata Indica Cab","Swift Cab","Mahindra scorpio Cab","Chevrolet Tavera Cab","Innova Cab")
    drop.place(x=180,y=100)
#when clicked on BOOK button your cab is booked and data is saved in MY BOOKINGS
    b=Button(top3,text="Book",fg='white',bg='black',height=2,width=10,font='georgia 12 bold',relief=RAISED,command=savebookings)
    b.place(x=1000,y=100)
#button b1 shows the taxi image
    b1=Button(top3,image=cab,text='Taxi',font=('georgia 14 bold'),border=0,compound=TOP)
    b1.place(x=150,y=190)
#button b2 shows the Tata Indica image
    b2=Button(top3,image=cab_1,text='Tata Indica',font=('georgia 14 bold'),border=0,compound=TOP)
    b2.place(x=500,y=190)
#button b3 shows the Swift image
    b3=Button(top3,image=cab_2,text='Swift',font=('georgia 14 bold'),border=0,compound=TOP)
    b3.place(x=850,y=190)
#button b4 shows the Mahindra scorpio image 
    b4=Button(top3,image=cab_3,text='Mahindra scorpio',font=('georgia 14 bold'),border=0,compound=TOP)
    b4.place(x=150,y=450)
#button b5 shows the Chevrolet Tavera image
    b5=Button(top3,image=cab_4,text='Chevrolet Tavera',font=('georgia 14 bold'),border=0,compound=TOP)
    b5.place(x=500,y=450)
#button b6 shows Innova image 
    b6=Button(top3,image=cab_5,text='Innova',font=('georgia 14 bold'),border=0,compound=TOP)
    b6.place(x=850,y=450)
#BACK is to close the existing window and go back
    Button(top3,text="BACK",height=1,width=7,font=('georgia 13 bold'),relief=RAISED,command=top3.destroy).place(x=30,y=600)
    top3.mainloop()        #closes the window top3

#=======================================================HOME PAGE OF THE CAB BOOKING======================================================================== 
def main_menu():     #function to show home page
    top=Toplevel()  #creates a new window
    top.title("Main Menu")     #window title
    top.geometry('1300x700')   #window geometry
#appling canvas to window and pack it
    canvas = Canvas(top,width=1300, height=645, bg='white')
    canvas.pack()
    cab_3 = PhotoImage(file='background.png')   #place image on the window 
    canvas.create_image(0,0, image=cab_3, anchor=NW)    #image cordinates on window
#Create three buttons "CAB BOOKING" AND "MY BOOKINGS" AND "USER DETAILS" AND "BACK"
#passed function to all buttons individually
    b1=Button(top,text="BOOK CAB",height=1,width=14,font=('georgia 18 bold'),relief=RAISED,command=open_window1)
    b1.place(x=500,y=100)  #places button b1
    b2=Button(top,text="MY BOOKINGS",height=1,width=14,font=('georgia 18 bold'),relief=RAISED,command=showbookings)
    b2.place(x=900,y=100)  #places button b2
    b4=Button(top,text="USER DETAILS",height=1,width=14,font=('georgia 18 bold'),relief=RAISED,command=show)
    b4.place(x=100,y=100)  #places button b4
    b3=Button(top,text="BACK",height=1,width=7,font=('georgia 13 bold'),relief=FLAT,command=top.destroy)
    b3.place(x=50,y=550)   #places button b4
    top.mainloop()   #closes the window top 
'''
def message():
    messagebox.showinfo("Message","Account Created Sucessfully")
'''

root.mainloop() #closes the window root
