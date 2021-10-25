import tkinter

def showWindow():
    mainwindow = tkinter.Tk()
    mainwindow.title('Test Vote Tool')
    mainwindow.geometry('635x300+50+50')
    mainwindow.resizable(False,False)

    #Definition of the menu bar
    menubar = tkinter.Menu(mainwindow)
    filemenu = tkinter.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Info", command=openInfo)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=quit)

    mainwindow.config(menu=menubar)
    
    menubar.add_cascade(label="File", menu=filemenu)

    #Definition of the Instruction Label Frame
    labelframe_widget = tkinter.LabelFrame(mainwindow,text='Instructions')
    labelframe_widget.grid(column=0, row=0, padx=5, pady=5)
    label_widget = tkinter.Label(labelframe_widget,text='This application allows you to manually enter the names of the students\n of the course in Mechanics applied to Machines and the corresponding grade of the course.\nAt the end of the procedure the arithmetic average will be calculated and saved externally in the mediacorso.json file.')
    label_widget.pack()

    #Definition of the Input Label Frame
    mainwindow.mainloop()

def openInfo():
    infoWindow = tkinter.Tk()
    infoWindow.title('Info')
    infoWindow.geometry('315x100+100+100')
    labelframe_widget = tkinter.LabelFrame(infoWindow,text='Instructions')
    labelframe_widget.grid(column=0, row=0, padx=5, pady=5)
    label_widget = tkinter.Label(labelframe_widget,text='TEST VOTE TOOL 1.0')
    label_widget1 = tkinter.Label(labelframe_widget,text='This is an experimental GUI version of the Test Vote Tool.\nStay tuned for more info.')
    label_widget.pack()
    label_widget1.pack()
    infoWindow.resizable(False,False)

def exit():
    quit()