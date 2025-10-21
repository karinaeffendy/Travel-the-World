#importing tkinter
from tkinter import *

#Create main window
root = Tk()
root.title("Choose Your Own Adventure: Travel Itinerary")
root.geometry("400x500")
root.configure(bg="light blue")

#Define frames (pages)
page1 = Frame(root, bg="light blue")
page2 = Frame(root, bg="light blue")
page3 = Frame(root, bg="light blue")
page4 = Frame(root, bg="light blue")
page5 = Frame(root, bg="light blue")
page6 = Frame(root, bg="light blue")
page7 = Frame(root, bg="light blue")
page8 = Frame(root, bg="light blue")
page9 = Frame(root, bg="light blue")
page10 = Frame(root, bg="light blue")
page11 = Frame(root, bg="light blue")
page12 = Frame(root, bg="light blue")
page13 = Frame(root, bg="light blue")
page14 = Frame(root, bg="light blue")
page15 = Frame(root, bg="light blue")
page16 = Frame(root, bg="light blue")
page17 = Frame(root, bg="light blue")
page18 = Frame(root, bg="light blue")
page19 = Frame(root, bg="light blue")
page20 = Frame(root, bg="light blue")
page21 = Frame(root, bg="light blue")
page22 = Frame(root, bg="light blue")
page23 = Frame(root, bg="light blue")
page24 = Frame(root, bg="light blue")
page25 = Frame(root, bg="light blue")
page26 = Frame(root, bg="light blue")
page27 = Frame(root, bg="light blue")
page28 = Frame(root, bg="light blue")
page29 = Frame(root, bg="light blue")
page30 = Frame(root, bg="light blue")
page31 = Frame(root, bg="light blue")
page32 = Frame(root, bg="light blue")
page33 = Frame(root, bg="light blue")
page34 = Frame(root, bg="light blue")
page35 = Frame(root, bg="light blue")
page36 = Frame(root, bg="light blue")
page37 = Frame(root, bg="light blue")
page38 = Frame(root, bg="light blue")
page39 = Frame(root, bg="light blue")
page40 = Frame(root, bg="light blue")
page41 = Frame(root, bg="light blue")
page42 = Frame(root, bg="light blue")
page43 = Frame(root, bg="light blue")
page44 = Frame(root, bg="light blue")
page45 = Frame(root, bg="light blue")
page46 = Frame(root, bg="light blue")
page47 = Frame(root, bg="light blue")
page48 = Frame(root, bg="light blue")
page49 = Frame(root, bg="light blue")
page50 = Frame(root, bg="light blue")
page51 = Frame(root, bg="light blue")
page200 = Frame(root, bg="light blue")

for frame in [page1, page2, page3, page4, page5, page6, page7, page8, page9, 
              page10, page11, page12, page13, page14, page15, page16, page17,
              page18, page19, page20, page21, page22, page23, page24, page25,
              page26, page27, page28, page29, page30, page31, page32, page33,
              page34, page35, page36, page37, page38, page39, page40, page41,
              page42, page43, page44, page45, page46, page47, page48, page49,
              page50, page51, page200]:
    frame.grid(row=0, column=0, sticky='nsew')


#Welcome page, highlighting what the app is about 
Label(page1, text="Travel the World", font=("Helvetica", 24, "bold"), bg="light blue").pack(pady=30)
Label(page1, text="Find a new country to travel to", font=("Helvetica", 16), bg="light blue").pack(pady=10)
Label(page1, text="Are you Ready?", font=("Helvetica", 16), bg="light blue").pack(pady=10)

Button(page1, text="Go!", font=("Helvetica", 16), bg="lightblue",
       command=lambda: show_frame(page2)).pack(pady=10)

#First Question 
Label(page2, text="What continent would you like to travel to?", font=("Helvetica", 20, "bold"), bg="light blue").pack(pady=30)

Button(page2, text="Oceania", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page3)).pack(pady=10)

Button(page2, text="Asia", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page4)).pack(pady=10)

Button(page2, text="Europe", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page5)).pack(pady=10)

Button(page2, text="Africa", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page6)).pack(pady=10)

Button(page2, text="Americas - North and South", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page7)).pack(pady=10)

#Page 3 - Question 2 - Oceania 
Label(page3, text="What Region would you like to travel to?", font=("Helvetica", 20, "bold"), bg="light blue").pack(pady=30)

Button(page3, text="Australasia", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page8)).pack(pady=10)

Button(page3, text="Melanseia", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page9)).pack(pady=10)

Button(page3, text="Micronesia", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page10)).pack(pady=10)

Button(page3, text= "Polynesia", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page11)).pack(pady=10)

#Page 4 - Question 2 - Asia
Label(page4, text="What Region would you like to travel to?", font=("Helvetica", 20, "bold"), bg="light blue").pack(pady=30)

Button(page4, text="Central Asia", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page12)).pack(pady=10)

Button(page4, text="East Asia", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page13)).pack(pady=10)

Button(page4, text="South Asia", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page14)).pack(pady=10)

Button(page4, text= "South-East Asia", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page15)).pack(pady=10)

Button(page4, text= "Western Asia (Middle East)", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page16)).pack(pady=10)

#Page 5 - Question 2 - Europe
Label(page5, text="What Region would you like to travel to?", font=("Helvetica", 20, "bold"), bg="light blue").pack(pady=30)

Button(page5, text="Nordic/Scandinavian", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page17)).pack(pady=10)

Button(page5, text="Eastern Europe", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page18)).pack(pady=10)

Button(page5, text="Central Europe", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page19)).pack(pady=10)

Button(page5, text= "Southern Europe", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page20)).pack(pady=10)

Button(page5, text= "British Isles", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page21)).pack(pady=10)

Button(page5, text= "Baltics", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page22)).pack(pady=10)

#Page 6 - Question 2 - Africa
Label(page6, text="What Region would you like to travel to?", font=("Helvetica", 20, "bold"), bg="light blue").pack(pady=30)

Button(page6, text="Northern Africa", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page23)).pack(pady=10)

Button(page6, text="West Africa", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page24)).pack(pady=10)

Button(page6, text="East Africa", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page25)).pack(pady=10)

Button(page6, text= "Middle Africa", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page26)).pack(pady=10)

Button(page6, text= "Southern Africa", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page27)).pack(pady=10)

#Page 7 - Question 2 - America
Label(page7, text="What Region would you like to travel to?", font=("Helvetica", 20, "bold"), bg="light blue").pack(pady=30)

Button(page7, text="North America", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page28)).pack(pady=10)

Button(page7, text="Central America", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page29)).pack(pady=10)

Button(page7, text="Caribbean", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page30)).pack(pady=10)

Button(page7, text= "South America", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page31)).pack(pady=10)

#Page 8 - Question 3 - Oceania - Australasia
Label(page8, text="What are your expectations with travelling?", font=("Helvetica", 20, "bold"), bg="light blue").pack(pady=30)

Button(page8, text="Food", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page32)).pack(pady=10)

Button(page8, text="Scenery", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page33)).pack(pady=10)

Button(page8, text="Adventure", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page34)).pack(pady=10)

Button(page8, text= "Culture", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page35)).pack(pady=10)

#Page 9 - Question 3 - Oceania - Melanseia 
Label(page9, text="What are your expectations with travelling?", font=("Helvetica", 20, "bold"), bg="light blue").pack(pady=30)

Button(page9, text="Food", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page36)).pack(pady=10)

Button(page9, text="Scenery", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page37)).pack(pady=10)

Button(page9, text="Adventure", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page38)).pack(pady=10)

Button(page9, text= "Culture", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page39)).pack(pady=10)

#Page 10 - Question 3 - Micronesia 
Label(page10, text="What are your expectations with travelling?", font=("Helvetica", 20, "bold"), bg="light blue").pack(pady=30)

Button(page10, text="Food", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page40)).pack(pady=10)

Button(page10, text="Scenery", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page41)).pack(pady=10)

Button(page10, text="Adventure", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page42)).pack(pady=10)

Button(page10, text= "Culture", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page43)).pack(pady=10)

#Page 11 - Question 3 - Polynesia 
Label(page11, text="What are your expectations with travelling?", font=("Helvetica", 20, "bold"), bg="light blue").pack(pady=30)

Button(page11, text="Food", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page44)).pack(pady=10)

Button(page11, text="Scenery", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page45)).pack(pady=10)

Button(page11, text="Adventure", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page46)).pack(pady=10)

Button(page11, text= "Culture", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page47)).pack(pady=10)

#Page 12 - Question 3 - Asia - Central Asia 
Label(page12, text="What are your expectations with travelling?", font=("Helvetica", 20, "bold"), bg="light blue").pack(pady=30)

Button(page12, text="Food", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page48)).pack(pady=10)

Button(page12, text="Scenery", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page49)).pack(pady=10)

Button(page12, text="Adventure", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page50)).pack(pady=10)

Button(page12, text= "Culture", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page51)).pack(pady=10)

#Page 13 - Question 3 - Asia - Central Asia 
Label(page13, text="What are your expectations with travelling?", font=("Helvetica", 20, "bold"), bg="light blue").pack(pady=30)

Button(page13, text="Food", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page48)).pack(pady=10)

Button(page13, text="Scenery", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page49)).pack(pady=10)

Button(page13, text="Adventure", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page50)).pack(pady=10)

Button(page13, text= "Culture", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page51)).pack(pady=10)

#end page 
ending_label = Label(page200, text="", wraplength=500, font=("Helvetica", 14), bg="light blue")
ending_label.pack(pady=50)
Button(page50, text="🏠 Restart Adventure", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page1)).pack(pady=20)
# ---------------- FUNCTIONS ----------------
def show_frame(frame):
    frame.tkraise()

def show_ending(message):
    ending_label.config(text=f"{message}\n\n✨ Thanks for playing! ✨")
    show_frame(page15)

# Start on page 1
show_frame(page1)

root.mainloop()