from tkinter import *     #install all the packages or the python will show the module not found error
from PIL import ImageTk,Image
def fun(name_1,name_2):
    import pandas as pd
    import numpy as np
    attendance = pd.read_csv(name_1)
    unique = attendance['username'].unique().tolist() #to extract unique names from repeated names
    data = pd.DataFrame()
    for name in unique:
        joined = attendance.loc[attendance.username == name][attendance.useraction == 'joined']["timestamp"] 
        left = attendance.loc[attendance.username == name ][attendance.useraction == 'left']["timestamp"]
        time_1 = pd.to_datetime(joined) #changing the data in string format to datetime format
        time_2 = pd.to_datetime(left)
        arr_1 = time_1.to_numpy() #converted to numpy to make arithmetic calculation more easier
        arr_2 = time_2.to_numpy()
        subract = arr_2 - arr_1 #to find time duration , the datas in subract will be in nano seconds and will be in a single
        newarr = np.array_split(subract.astype('timedelta64[m]'),1) #breaking of various element in a single subset and converting the nanoseconds to minutes
        sum = np.sum(newarr) #suming up all the datas(time duration) obtained
        print(f"Then {name} stayed in the meet for a time duration of: {sum}", name)
        let = pd.DataFrame(data={'Name of the students': [name],'Time duration': [sum]})
        data = data.append(let)
    data.to_csv(name_2,index=False)
    print(f"The output datas written to the csv file in the path:{name_2}") #writing into the csv file path specified
window=Tk() #from here on it will the gui part
window.title("attendance automater")
window.geometry('800x600') #give the breadth and width of the image u want to apply
image1 = Image.open("C:\\Users\\YOGESH T\\Downloads\\my_bot.gif") #replace this with the path of the image you want to add to the gui inside .open("")
test = ImageTk.PhotoImage(image1)
label1 = Label(image=test)
label1.image = test
label1.place(x= 0, y= 0)
lb1= Label(window, text="Enter the file path need to be scanned:")
lb1.grid(column=0, row=0)
lb2= Label(window, text=" ")
lb2.grid(column=0, row=4)
name_1 = Entry(window,width=50)
name_1.grid(column=1, row=0)
lb1= Label(window, text="Enter the file path to which output should be stored:")
lb1.grid(column=0, row=1)
lb2= Label(window, text=" ")
lb2.grid(column=0, row=4)
name_2 = Entry(window,width=50)
name_2.grid(column=1, row=1)
def clicked():
	res=fun(name_1.get(),name_2.get())
	lb2.configure(text=res)
btn = Button(window, text = 'click to proceed', command=clicked)
btn.grid(column=2, row=2)
window.mainloop()
