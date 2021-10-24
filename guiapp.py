import tkinter

def showWindow():
    mainwindow = tkinter.Tk()
    mainwindow.title('Test Vote Tool')
    mainwindow.geometry('800x600+50+50')
    mainwindow.resizable(False,False)

    labelframe_widget = tkinter.LabelFrame(mainwindow,text='Main Entries')
    label_widget = tkinter.Label(labelframe_widget,text='This application allows you to manually enter the names of the students\n of the course in Mechanics applied to Machines and the corresponding grade of the course.\nAt the end of the procedure the arithmetic average will be calculated and saved externally in the mediacorso.json file.')
    labelframe_widget.pack()
    label_widget.pack()
    mainwindow.mainloop()