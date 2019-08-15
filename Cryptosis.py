from tkinter import *
from tkinter import Tk
from tkinter import messagebox
from tkinter import Button
from tkinter import Entry
from tkinter import StringVar
from tkinter import scrolledtext

from tkinter import Tk
from tkinter.filedialog import askopenfilename
import tkinter
import tkinter.filedialog
import base64
from tkinter.ttk import *
import webbrowser


root=Tk()
root.title("Cryptosis")
root.iconbitmap('icon.ico')



height = root.winfo_screenheight()
width = root.winfo_screenwidth()
canvas1 = Canvas(root, width=width/2.5, height=height-300)
print("\n width x height = %d x %d (in pixels)\n" %(width, height))
img = PhotoImage(file="cry.ppm")
canvas1.create_image(2,40, anchor=NW, image=img)
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)

#scrollbar = Scrollbar(root)
#scrollbar.pack( side = RIGHT, fill = Y )
#mylist = Listbox(root, yscrollcommand = scrollbar.set )
#for line in range(100):
 #  mylist.insert(END, 'This is line number' + str(line))
#mylist.pack( side = LEFT, fill = BOTH )
#scrollbar.config( command = mylist.yview )
#input="Insert your text here...or browse your file"
output="Outputs"


#root.title("Cryptosis")


#text.tag_add("Write Here", "1.0", "1.4")
#text.tag_add("Click Here", "1.8", "1.13")

#text.tag_config("Write Here", background="yellow", foreground="black")
#text.tag_config("Click Here", background="black", foreground="white")

text = Text(root, height=10, width=60)
#text.tag_config("Write Here")
input1="Insert your text here...or browse your file"
text.insert(INSERT,input1)
canvas1.create_window(400, 500, window=text)

def Contact():

    contact = Tk()
    contact.title("Contact")
    height_root = canvas1.winfo_screenheight()
    width_root = canvas1.winfo_screenwidth()
    Contact_canvas = Canvas(contact, width=width_root/2, height=height_root/2)
    ourMessage = 'Welcome in our software Cryptosis , i wish that its useful for you'
    ourMessage1 = 'if there any quations , please contact us in : www.Crisis.com'

    whatever_you_do = "Welcome in our software Cryptosis , hopely is useful for you ," \
                      "if there's any question , please contact us in "
    new = 1
    url = "https://www.crisis.com"

    def openweb() :
        webbrowser.open(url, new=new)

    #Btn = Button(contact, text="This opens Google", command=openweb)
    #contact.iconbitmap('./Img/fb.png')
    #x_image = './Img/fb.png'
    #x_image_for_button = PhotoImage(file=x_image)
    #Btn = Button(contact, image='icon.ico', command=openweb)
    b = Button(contact, text="Click Here",command=openweb)
    #b.config(width="40", height="40")
    b.place(x=5, y=5)

    msg = Message(contact, text=whatever_you_do)
    msg.config(bg='white', font=('times', 16, 'bold'))
    msg.pack()
    b.pack()
    #contact.pack()
    #messageVar = Text(contact )
    #Contact_canvas = Text(Contact)
    #contact.config(bg='lightgreen')
"""def Key():

    key = Tk()
    key.title("The key")
    cesar_key="Your Key"
    height_root = canvas1.winfo_screenheight()
    width_root = canvas1.winfo_screenwidth()
    key_canvas = Canvas(key, width=320, height=80)
    key_text = Text(key, height=1, width=30)
    key_text.insert(INSERT, cesar_key)
    key_canvas.create_window(150, 20, window=key_text)
    button_key = Button(key, text='   Enter  ', command=take_key(cesar_key))
    key_canvas.create_window(200, 60, window=button_key)
    button_key1 = Button(key, text='   Annuler  ', command=key_canvas.destroy)
    key_canvas.create_window(100, 60, window=button_key1)"""








def About_us():

    messagebox.showinfo("Info", "  Crisis Lab  ")
    b = Button(canvas1, text="Info", image=r'.\Img\fb.png', compound=CENTER)

def Options():

    MsgBox = messagebox.showinfo('Notification', 'SOON...',icon='info')



#--------------------------------------------------------------------------------------------------
def ExitApplication():
    MsgBox = messagebox.askquestion('Notification', 'Are you sure you want to exit the application',
                                       icon='warning')
    if MsgBox == 'yes':
        root.destroy()
    else:
        messagebox.showinfo('Return', 'You will now return to the application screen')


FILETYPES = [("text files", "*")]

filename = StringVar(root)

entry = Entry(root, textvariable=filename)


def set_filename():
    file = tkinter.filedialog.askopenfilename(
        parent=root, initialdir='*',
        title='Choose file',
        filetypes=[('Text file', '.txt')]
    )
    with open(file) as f:
        with open("input.txt", "w") as f1:
            for line in f:
                f1.write(line)
                #input.write(line)
            text.delete('1.0', END)
            input=line
            text.insert(INSERT, input)


"""def Copy():

    def __init__(self, master, **kw) :
        output.__init__(self, master, **kw)
        self.bind('<Control-c>', self.copy)
        self.bind('<Control-x>', self.cut)
        self.bind('<Control-v>', self.paste)

    def copy(self, event=None) :
        self.clipboard_clear()
        cp_text = self.get("sel.first", "sel.last")
        self.clipboard_append(cp_text)
        print(cp_text)"""
def Copy():
    MsgBox = messagebox.showinfo('Notification', 'SOON...',icon='info')
def Share():
    MsgBox = messagebox.showinfo('Notification', 'SOON...',icon='info')



def Crypt():

    #ASCII-----------------------------------------------------------------------------------------

    input1 = text.get("1.0", END)
    list=[]
    for i in input1 :
        list+=i
    output = "ASCII = " + ''.join(" "+ str(ord(c)) for c in input1) + "\n"

    #Base64----------------------------------------------------------------------------------------

    encodedBytes = base64.b64encode(input1.encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")
    output +="Base64 = " + encodedStr +"\n"

    #HEX-------------------------------------------------------------------------------------------
    output += "HEX = ...SOON" +"\n"



    #Cesar-----------------------------------------------------------------------------------------

    input1 = text.get("1.0", END)
    Alphabet1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Alphabet2 = "abcdefghijklmnopqrstuvwxyz"
    numbers="1234567890/~!#$%^&*(()_+}{?><|\-.,][="

    #key = int(input("Enter your key : "))
    MsgBox = messagebox.askquestion('Notification', 'Do you have the key for CESAR encryption?',
                                       icon='info')
    if MsgBox == 'yes':
        key = Tk()
        key.title("The key")
        cesar_key = "Your Key"
        height_root = canvas1.winfo_screenheight()
        width_root = canvas1.winfo_screenwidth()
        key_canvas = Canvas(key, width=320, height=80)
        key_text = Text(key, height=1, width=30)
        key_text.insert(INSERT, cesar_key)
        key_canvas.create_window(150, 20, window=key_text)
        button_key = Button(key, text='   Enter  ', command=key_text.get("1.0", END))
        key_canvas.create_window(200, 60, window=button_key)
        button_key1 = Button(key, text='   Annuler  ', command=key_canvas.destroy)
        key_canvas.create_window(100, 60, window=button_key1)
        cesar_key=key_text.get("1.0", END)
        print(cesar_key)
        key_canvas.pack()


    else:
        messagebox.showinfo('Return', 'The program will continue without teh key')

    n=len(input1)
    m=len(Alphabet1)
    l=len(numbers)
    output_cesar=""
    for i in range(n):

        if input1[i]==" ":
            output_cesar+=" "

        if input1[i]=="\n":
            output_cesar+=" "

        for j in range(m):

            if input1[i]==Alphabet1[j]:

                if j+key<=25 :
                    output_cesar += Alphabet1[j+key]
                else :
                    X=25-j
                    Y=key-X
                    output_cesar += Alphabet1[Y]


            if input1[i]==Alphabet2[j]:
                if j + key <= 25 :
                    output_cesar += Alphabet1[j + key]
                else :
                    X = 25 - j
                    Y = key - X -1
                    output_cesar += Alphabet1[Y]

            if input1[i]==numbers[j]:
                output_cesar+=numbers[j]


    output += "CESAR = " + output_cesar

    #-------------------------------------------------------------------------------------------------
    #Enregistred file and output
    with open("output.txt", "w") as f1:
        for line in output:
            f1.write(line)

    text1.delete('1.0', END)
    text1.insert(INSERT,output)
    print("File registered")
    #messagebox.showinfo("Info", "Your outputs is saved in output.txt , you'll find it in your Cryptosis file.")
def Decrypt() :
    try :

        decodedMessage = ""
        input = text.get("1.0", END)

        for item in input.split() :
            decodedMessage += chr(int(item))
            output = "ASCII to Plaintext =  " + decodedMessage + "\n"
            print(decodedMessage)
            text1.delete('1.0', END)
            text1.insert(INSERT, output)
    except:
         return Base64()

            # Base64-------------------------------------------------------------------------------------
def Base64():

    try:
        input = text.get("1.0", END)
        encodedBytes = base64.b64decode(input)
        decodedStr = str(encodedBytes, "utf-8")
        output = "Base64 to Plaintext =  " + decodedStr
        text1.delete('1.0', END)
        text1.insert(INSERT, output)
        with open("output.txt", "w") as f1 :
            for line in output :
                f1.write(line)

    except:
        return Cesar()

def Cesar():

    try:
        input1 = text.get("1.0", END)
        Alphabet1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        Alphabet2 = "abcdefghijklmnopqrstuvwxyz"
        numbers = "1234567890/~!#$%^&*(()_+}{?><|\-.,][="

        # key = int(input("Enter your key : "))
        key = 3

        n = len(input1)
        m = len(Alphabet1)
        l = len(numbers)
        output_cesar = ""
        for i in range(n) :

            if input1[i] == " " :
                output_cesar += " "

            if input1[i] == "\n" :
                output_cesar += " "

            for j in range(m) :

                if input1[i] == Alphabet1[j] :

                    if j + key >= 0 :
                        output_cesar += Alphabet1[j - key + 1]
                    else :
                        X = 25 - j
                        Y = key - X
                        output_cesar += Alphabet1[Y + 1]

                if input1[i] == Alphabet2[j] :
                    if j + key >= 0 :
                        output_cesar += Alphabet1[j - key + 1]
                    else :
                        X = 25 - j
                        Y = key - X - 1
                        output_cesar += Alphabet1[Y + 1]

                if input1[i] == numbers[j] :
                    output_cesar += numbers[j]
        text1.delete('1.0', END)
        output = "Cesar to Plaintext =  " + output_cesar
        text1.insert(INSERT, output)
        with open("output.txt", "w") as f1 :
            for line in output :
                f1.write(line)
    except:
        MsgBox = messagebox.showinfo('Notification', 'Nothing Found',icon='info')


#Menu----------------------------------------------------------------------------------------------

menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Open',command=set_filename)
filemenu.add_command(label='Options',command=Options)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=ExitApplication)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='Contact' ,command=Contact)
helpmenu.add_command(label='About us' , command=About_us)



#----------------------------------------------------------------------------------------------------
text1= Text(root, height=1, width=5)
text1.insert(INSERT, "INPUT")
canvas1.create_window(60, 400, window=text1)



text1= Text(root, height=1, width=6)
text1.insert(INSERT, "OUTPUT")
canvas1.create_window(63, 600, window=text1)

text1 = Text(root, height=10, width=60)
text1.insert(INSERT, output)
canvas1.create_window(400, 700, window=text1)


#Buttons-------------------------------------------------------------------------------------------

button2 = Button(root, text='   Browse  ', command=set_filename )
canvas1.create_window(700, 428, window=button2)


button3 = Button(root, text='  Crypt  ', command=Crypt)
canvas1.create_window(700, 468, window=button3)

button4 = Button(root, text='  Decrypt  ', command=Decrypt )
canvas1.create_window(700, 508, window=button4)

button1 = Button(root, text='  EXIT  ', command=ExitApplication )
canvas1.create_window(700, 548, window=button1)

button1 = Button(root, text='  Copy  ', command=Copy)
canvas1.create_window(700, 648, window=button1)

button1 = Button(root, text='  Share  ', command=Share )
canvas1.create_window(700, 708, window=button1)

#button3 = Button(root, text='  Modify IDs  ', command=openexcel )
#canvas1.create_window(500, 900, window=button3)

w = Label(root, text='Crisis.com | ©2020')

canvas1.pack()


saveinfo = Label(root,
                 text=" Your Outputs and Inputs will be saved in text files , you'll find it in your Cryptosis file.")

saveinfo.pack()
#text2 = Text(root,height=10, width=90)
#s = Scrollbar(root)
#ext2.focus_set()
##s.pack(side=RIGHT, fill=text2.winfo_height)

#s.config(command=text2.winfo_height)
##text2.insert(INSERT, output)



#canvas1.create_window(400, 700, window=text2)
#canvas1.create_window(750, 700, window=s)
w.pack()

#s = Scrollbar(root)
#T = Text(root)

#T.focus_set()
#s.pack(side=RIGHT, fill=Y)
#T.pack(side=LEFT, fill=Y)
#s.config(command=T.yview)
#T.config(yscrollcommand=s.set)

#for i in range(40):
 #  T.insert(END, "This is line %d\n" % i)
#scrollbar.config( command = mylist.yview )
root.mainloop()

