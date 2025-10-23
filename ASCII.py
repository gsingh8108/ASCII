from tkinter import *
root = Tk()

root.title("Encryption")
root.geometry("400x400")
root.configure(background='cyan')

entry_name = Entry(root)
entry_name.place(relx = 0.5, rely = 0.4, anchor=CENTER)

label = Label(root, text="Name in Ascii : ", bg="blue", fg="white")
label2 = Label(root, text="Encrypted Name : ", bg="blue", fg="white")

def asciiConverter(): 
    
    input_name = entry_name.get()
    
    for letter in input_name:
        label['text'] += str(ord(letter)) + " "
        ascii = int(ord(letter))
        encrypted = ascii - 1
        label2['text'] += str(chr(encrypted))
        
button = Button(root, text="Display The Ascii Code And Encrypted Value", command=asciiConverter, bg="gold", fg="black")
button.place(relx = 0.5, rely = 0.5, anchor=CENTER)

label.place(relx = 0.5, rely = 0.6, anchor=CENTER)
label2.place(relx = 0.5, rely = 0.7, anchor=CENTER)

root.mainloop()