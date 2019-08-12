from tkinter import *
from tkinter import Tk
from tkinter import messagebox
from tkinter import Button
from tkinter import Entry
from tkinter import StringVar
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import tkinter
import tkinter.filedialog
import base64


root=Tk()
root.title("Cryptosis")

canvas1 = Canvas(root, width=800, height=1000)


img = PhotoImage(file="11.ppm")
canvas1.create_image(5,40, anchor=NW, image=img)

#input="Insert your text here...or browse your file"
output="Outputs"


#root.title("Cryptosis")


#text.tag_add("Write Here", "1.0", "1.4")
#text.tag_add("Click Here", "1.8", "1.13")

#text.tag_config("Write Here", background="yellow", foreground="black")
#text.tag_config("Click Here", background="black", foreground="white")

text = Text(root, height=10, width=90)
#text.tag_config("Write Here")
input1="Insert your text here...or browse your file"
text.insert(INSERT,input1)
canvas1.create_window(400, 500, window=text)


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
            print(input)

def Crypt():

    #ASCII---------------------------------------------------------------------------------------

    input1 = text.get("1.0", END)
    list=[]
    for i in input1 :
        list+=i
    output = "ASCII = " + ''.join(" "+ str(ord(c)) for c in input1) + "\n"

    #Base64--------------------------------------------------------------------------------------

    encodedBytes = base64.b64encode(input1.encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")
    output +="Base64 = " + encodedStr +"\n"

    #HEX-----------------------------------------------------------------------------------------
    output += "HEX = ...SOON" +"\n"



    #Cesar-----------------------------------------------------------------------------------------

    input1 = text.get("1.0", END)
    Alphabet1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Alphabet2 = "abcdefghijklmnopqrstuvzxyz"
    numbers="1234567890"

    #key = int(input("Enter your key : "))
    key=3

    n=len(input1)
    m=len(Alphabet1)
    k=len(Alphabet2)
    l=len(numbers)
    output_cesar=""
    for i in range(n):

        if input1[i]==" ":
            output_cesar+=" "
        if input1[i]=="\n":
            output_cesar+=" "

        for j in range(m):
            if input1[i]==Alphabet1[j]:
                output_cesar += Alphabet1[j+key]
            if input1[i]==Alphabet2[j]:
                output_cesar += Alphabet1[j + key]



    print(output_cesar)
    output += "CESAR = " + output_cesar

    #-------------------------------------------------------------------------------------------------
    #Enregistred file and output
    with open("output.txt", "w") as f1:
        for line in output:
            f1.write(line)

    text1.delete('1.0', END)
    text1.insert(INSERT,output)
    print("File registered")

def Decrypt():
    try:

        decodedMessage = ""

        input = text.get("1.0", END)
        for item in input.split():
            decodedMessage+= chr(int(item))
        output = "ASCII to Plaintext =  "  + decodedMessage +"\n"
        print(decodedMessage)
        text1.delete('1.0', END)
        text1.insert(INSERT, output)

    except:

        encodedBytes=base64.b64decode(input)
        decodedStr = str(encodedBytes, "utf-8")
        output = "Base64 to Plaintext =  " + decodedStr
        text1.delete('1.0', END)
        text1.insert(INSERT,output)
        print("File registered")

text1 = Text(root, height=10, width=90)
text1.insert(INSERT, output)
canvas1.create_window(400, 700, window=text1)


button2 = Button(root, text='   Browse  ', command=set_filename )
canvas1.create_window(250, 900, window=button2)

button3 = Button(root, text='  Crypt  ', command=Crypt)
canvas1.create_window(350, 900, window=button3)

button4 = Button(root, text='  Decrypt  ', command=Decrypt )
canvas1.create_window(450, 900, window=button4)

button1 = Button(root, text='  EXIT  ', command=ExitApplication )
canvas1.create_window(550, 900, window=button1)

#button3 = Button(root, text='  Modify IDs  ', command=openexcel )
#canvas1.create_window(500, 900, window=button3)

canvas1.pack()

root.mainloop()

