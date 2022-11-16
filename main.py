# How to test Typing Speed using Python?

# Difficulty Level : Basic
# Last Updated : 05 Sep, 2020
# Prerequisites: Python GUI – tkinter

#We will create a program test the typing speed of the user with a basic GUI application using Python language. Here the Python libraries like Tkinter and Timeit are used for the GUI and Calculation of time for speed testing respectively.  Also, the Random function is used to fetch the random words for the speed testing calculation. Following command is used to install the above-mentioned libraries:

# pip install tkintertable
# pip install pytest-timeit
# Firstly, all the libraries are imported that are installed as mentioned above, and using the bottom-up approach the programming for testing the typing speed using python is created. 

# Below is the implementation.

# importing all libraries
from tkinter import ttk
from tkinter import *
from timeit import default_timer as timer
import random
BROWSE_FONT = ('verdana', 20)
# creating window using gui

root = Tk()
root.title('Py-Tytest')
root.geometry("510x800")

style=PhotoImage(file='test.png')

frmone= ttk.Frame(root)
frmone.grid()
ttk.Label(frmone,image=style).grid(row=0, column=0 , columnspan=4)

frmtwo= ttk.Frame(root)
frmtwo.grid()
ttk.Label(frmtwo, text="WPM", padding="5",width="5").grid(column=0, row=1)
ttk.Label(frmtwo, text="__", padding="5",background="white",width=10).grid(column=1, row=1)
ttk.Label(frmtwo, text="Time Remaining", padding="5",width="15").grid(column=2, row=1)
ttk.Label(frmtwo, text="60", padding="5",background="white",width="10").grid(column=3, row=1)

frmthree= ttk.Frame(frmtwo ,padding="5")
frmthree.grid(column=0, row=2 , columnspan=4)
ttk.Label(frmthree, text="Alpha gamma beta are the three \nmain components of \nradioactivity", padding="20",background="white", font=BROWSE_FONT).grid(column=0, row=2)

textbox = ttk.Entry(frmtwo , width=60 )
textbox.grid(column=0, row=3 , columnspan=4) 
ttk.Label(frmtwo, text="Drop mouse here ↑ and start typing.", padding="10").grid(column=0, row=4,columnspan=4)

frmfour= ttk.Frame(frmtwo ,padding="5")
frmfour.grid(column=0, row=5 , columnspan=4)
ttk.Button(frmfour, text="Reset").grid(column=0, row=5)
ttk.Button(frmfour, text="Pause").grid(column=1, row=5)
ttk.Button(frmfour, text="Exit →",command=root.destroy).grid(column=2, row=5)

ttk.Label(frmtwo, text="Python GUi Typing Test App.\nCopyright Biodata.io.\nexxcencorp.").grid(column=0, row=6,columnspan=4)

  
# # the size of the window is defined

  
# x = 0
  
# # defining the function for the test
# def game():
#     global x
  
#     # loop for destroying the window
#     # after on test
#     if x == 0:
#         window.destroy()
#         x = x+1
  
#     # defining function for results of test
#     def check_result():
#         if entry.get() == words[word]:
  
#             # here start time is when the window
#             # is opened and end time is when
#             # window is destroyed
#             end = timer()
  
#             # we deduct the start time from end
#             # time and calculate results using
#             # timeit function
#             print(end-start)
#         else:
#             print("Wrong Input")
  
#     words = ['programming', 'coding', 'algorithm',
#              'systems', 'python', 'software']
  
#     # Give random words for testing the speed of user
#     word = random.randint(0, (len(words)-1))
  
#     # start timer using timeit function
#     start = timer()
#     windows = Tk()
#     windows.geometry("450x200")
  
#     # use lable method of tkinter for labling in window
#     x2 = Label(windows, text=words[word], font="times 20")
  
#     # place of labling in window
#     x2.place(x=150, y=10)
#     x3 = Label(windows, text="Start Typing", font="times 20")
#     x3.place(x=10, y=50)
  
#     entry = Entry(windows)
#     entry.place(x=280, y=55)
  
#     # buttons to submit output and check results
#     b2 = Button(windows, text="Done",
#                 command=check_result, width=12, bg='grey')
#     b2.place(x=150, y=100)
  
#     b3 = Button(windows, text="Try Again", 
#                 command=game, width=12, bg='grey')
#     b3.place(x=250, y=100)
#     windows.mainloop()
  
  
# x1 = Label(window, text="Lets start playing..", font="times 20")
# x1.place(x=10, y=50)
  
# b1 = Button(window, text="Go", command=game, width=12, bg='grey')
# b1.place(x=150, y=100)
  
# calling window
root.mainloop()
# Output:

# Video Player

# 00:00
# 00:15


# In the above code, we first create the speed testing window using Tkinter. 
# The function is defined for calculating and printing the correct output after the user input. 
# A specific list of words is provided to the user to type and test the speed of typing. For that, 
# we provide a list of words and generate them with the random function. 