import tkinter

def showWindow():
    mainwindow = tkinter.Tk()
    mainwindow.title('Test Vote Tool')
    mainwindow.geometry('800x600+50+50')
    mainwindow.resizable(False,False)

    menubar = tkinter.Menu(mainwindow)
    filemenu = tkinter.Menu(menubar)
    filemenu.add_command(label="Info", command=openInfo)
    filemenu.add_command(label="Exit", command=quit)

    mainwindow.config(menu=menubar)
    
    menubar.add_cascade(label="File", menu=filemenu)

    labelframe_widget = tkinter.LabelFrame(mainwindow,text='Main Entries')
    label_widget = tkinter.Label(labelframe_widget,text='This application allows you to manually enter the names of the students\n of the course in Mechanics applied to Machines and the corresponding grade of the course.\nAt the end of the procedure the arithmetic average will be calculated and saved externally in the mediacorso.json file.')
    labelframe_widget.pack()
    label_widget.pack()
    mainwindow.mainloop()

def openInfo():
    infoWindow = tkinter.Tk()
    infoWindow.title('Info')
    infoWindow.geometry('300x300+100+100')
    infoWindow.resizable(False,False)

def exit():
    quit()