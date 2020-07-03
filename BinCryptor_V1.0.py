from tkinter import * 
HEIGHT = 680
WIDTH = 400

root = Tk()

def window(main):
    """Defines the window characteristics"""
    main.title("BinCryptor 1.0")
    main.update_idletasks()
    width = main.winfo_width() #Width of the current screen
    height = main.winfo_height() #Height of the current screen
    x = (main.winfo_screenwidth() // 2) - (width // 2)
    y = (main.winfo_screenheight() // 2) - (height // 2)
    main.geometry(f'{width}x{height}+{x}+{y}') #Adjusts the height and width

def encryptToBinary(message):
    string = message.replace(" ","#")
    chars = [i for i in string]
    codes = [ord(i) for i in chars]
    binaries = [str(bin(i)) for i in codes]
    cipher = ''.join(binaries).replace("0b","lO")
    crypticText.delete(0.0, 'end')
    crypticText.insert(0.0, cipher)

def decryptFromBinary(cipher):
    binaries = cipher.split("lO")
    codes = [int(i,2) for i in binaries[1::1]]
    chars = [chr(i) for i in codes]
    message = ''.join(chars).replace("#",' ')
    simpleText.delete(0.0, 'end')
    simpleText.insert(0.0, message)

def retrieve_input(): 
    """Simple Function to store input to variable"""
    inputValue = simpleText.get("1.0","end-1c") #Our Variable
    #"1.0" = start from first character in the text widget
    #"end-1c = delete the last character that Text creates every time"
    return inputValue

def retrieve_encrypted_input(): 
    """Simple Function to store input to variable"""
    inputValue = crypticText.get("1.0","end-1c") #Our Variable
    #"1.0" = start from first character in the text widget
    #"end-1c = delete the last character that Text creates every time"
    return inputValue

def clearMsg(event):
    simpleText.delete(0.0, 'end')

def clearCipher(event):
    crypticText.delete(0.0, 'end')

def reset():
    """Resets all Input Fields"""
    simpleText.delete(0.0, 'end')
    crypticText.delete(0.0, 'end')
    simpleText.insert(INSERT, "Enter Message Here...\n\nDouble-click to edit\nRight-click to Copy\nShift + Left-click to Paste")
    crypticText.insert(INSERT, "Paste Your Cipher Here...\n\nDouble-click to edit\nRight-click to Copy\nShift + Left-click to Paste")

def copy_message_to_clipboard(event):
    field_value = event.widget.get('1.0', 'end-1c')
    root.clipboard_clear()
    root.clipboard_append(field_value)
    clearMsg(event)
    simpleText.insert(INSERT, "Copied!")

def copy_cipher_to_clipboard(event):
    field_value = event.widget.get('1.0', 'end-1c')
    root.clipboard_clear()
    root.clipboard_append(field_value)
    clearCipher(event)
    crypticText.insert(INSERT, "Copied!")

def paste_message_to_text(event):
    text = simpleText.selection_get(selection = 'CLIPBOARD')
    simpleText.insert(INSERT, text)

def paste_cipher_to_text(event):
    text = crypticText.selection_get(selection = 'CLIPBOARD')
    crypticText.insert(INSERT, text)

canvas = Canvas(root, height=HEIGHT, width=WIDTH,highlightthickness = 0)
canvas.pack()

backgroundImage = PhotoImage(file="tech_Circle4.png")
backgroundLabel = Label(root, image = backgroundImage)
backgroundLabel.place(relwidth = 1, relheight = 1)

upperFrame = Frame(root,bg='white', bd=0, highlightcolor = "blue")
upperFrame.place(relx=0.5, rely=0.145, relwidth=0.75, relheight=0.3, anchor='n')
lowerFrame = Frame(root, bg='white', bd=0, highlightcolor= "blue")
lowerFrame.place(relx=0.5, rely=0.57, relwidth=0.75, relheight=0.3, anchor='n')

topScrollBar = Scrollbar(upperFrame)
topScrollBar.pack(side=RIGHT,fill=Y)
bottomScrollbar = Scrollbar(lowerFrame)
bottomScrollbar.pack(side = RIGHT, fill=Y)

simpleText = Text(upperFrame, yscrollcommand = topScrollBar.set, wrap=WORD, bg='black', fg='green', font=("Courier", 14, "bold"))
simpleText.insert(INSERT, "Enter Message Here...\n\nDouble-click to edit\nRight-click to Copy\nShift + Left-click to Paste")
simpleText.pack(fill=BOTH, anchor='center')
simpleText.bind("<Double-Button-1>", clearMsg)
simpleText.bind("<Button-3>", copy_message_to_clipboard)
simpleText.bind("<Shift-Button-1>", paste_message_to_text)
topScrollBar.config(command = simpleText.yview)

crypticText = Text(lowerFrame, bg='black', fg='green', yscrollcommand = bottomScrollbar.set, wrap=WORD, font=("Courier", 14, "bold"))
crypticText.insert(INSERT, "Paste Your Cipher Here...\n\nDouble-click to edit\nRight-click to Copy\nShift + Left-click to Paste")
crypticText.pack(fill=BOTH, anchor='center')
crypticText.bind("<Double-Button-1>", clearCipher)
crypticText.bind("<Button-3>", copy_cipher_to_clipboard)
crypticText.bind("<Shift-Button-1>", paste_cipher_to_text)
bottomScrollbar.config(command = crypticText.yview)

encryptButton = Button(root, text = "ENCRYPT" , bg ="#3077F7",fg="white", font=("Courier", 14, "bold"),command = lambda: encryptToBinary(retrieve_input()))
encryptButton.place(relx=0.125, rely=0.45, relwidth=0.75)
decryptButton = Button(root, text = "DECRYPT" , bg="red",fg="white", font=("Courier",14, "bold"), command = lambda: decryptFromBinary(retrieve_encrypted_input()) )
decryptButton.place(relx=0.125, rely = 0.51, relwidth=0.75)
resetButton = Button(root, text="RESET", bg="green",fg="white",font=("Courier",14,"bold"),command = reset)
resetButton.place(relx=0.125,rely=.875,relwidth=0.75)

window(root)
root.mainloop()