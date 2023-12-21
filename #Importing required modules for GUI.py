#Importing required modules for GUI
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
#Modules required for uploading files
from tkinter import filedialog
from tkinter.filedialog import askopenfile
#Modules required for face recognition and reading the image
import cv2
import face_recognition
#Code for GUI
my_w = tk.Tk()
my_w.geometry("500x500") # Size of the window
my_w.title('Pancard Authenticator')
my_font1 = ('times', 19, 'bold')
l1 = tk.Label(my_w, text='Pancard Authenticator', width=30, font=my_font1)
l1.grid(row=0, column=1)
l2 = tk.Label(my_w, text='INSTRUCTIONS',width=22,font=my_font1)
l2.grid(row=1, column=1)
l3 = tk.Label(my_w, text='1.FIRST UPLOAD PAN CARD PHOTO AND THEN YOUR PHOTO IN JPG FORMAT ONLY')
l3.grid(row=2,column=1,columnspan=5)
l4 = tk.Label(my_w, text='2.IF THE RESULT IS TRUE THEN THE PHOTOS OF THE PERSON ARE MATCHING')
l4.grid(row=3,column=1,columnspan=5)
l5 = tk.Label(my_w, text='3.IF THE RESULT IS FALSE THEN THE PHOTOS OF THE PERSON ARE NOT MATCHING')
l5.grid(row=4,column=1,columnspan=5)
b3 = tk.Button(my_w, text='Upload Pancard and Photo',
 width=20, command=lambda: check())
b3.grid(row=36, column=1)
blank = Entry(my_w) #It s where the result is shown
blank.grid(row=8, column=1,pady=10)
#The main function once the check button is clicked
def check():
#For uploading Pancard
 file1 = filedialog.askopenfilename()
 file_name1 = file1.replace('/', '\\\\')
 print(file_name1)
 #For uploading image
 file2 = filedialog.askopenfilename()
 file_name2 = file2.replace('/', '\\\\')
 print(file_name2)
#Processing 1st image
 img1 = cv2.imread(file_name1)
 rgb_img = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
 img_encoding1 = face_recognition.face_encodings(rgb_img)[0]
#Processing 2nd image
 img2 = cv2.imread(file_name2)
 rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
 img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]
#Comparing and giving the result
 result = face_recognition.compare_faces([img_encoding1], img_encoding2)
 print("Result: ", result)
 blank.insert(0, result )
my_w.mainloop() # Keep the window open