#importing tkinter
from tkinter import *

#Create main window
root = Tk()
root.title("Choose Your Own Adventure: Travel Itinerary")
root.geometry("450x500")
root.configure(bg="light blue")

#Create a function for frames 
def show_frame(frame):
    frame.tkraise()

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


for frame in [page1, page2, page3, page4, page5, page6, page7, page8, page9, 
              page10, page11, page12, page13, page14, page15, page16, page17,
              page18, page19, page20]:
    frame.grid(row=0, column=0, sticky='nsew')


#Welcome page, using labels and button is provide the user with information about the project 
show_frame(page1)
Label(page1, text="Travel the World", font=("Helvetica", 24, "bold"), bg="light blue").pack(pady=30)
Label(page1, text="Find a new country to travel to", font=("Helvetica", 16), bg="light blue").pack(pady=10)
Label(page1, text="Are you Ready?", font=("Helvetica", 16), bg="light blue").pack(pady=10)

Button(page1, text="Go!", font=("Helvetica", 16), bg="lightblue",
       command=lambda: show_frame(page2)).pack(pady=10)

#Use lables and buttons to allow users to interact with the project 
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

#Create a label asking the user which region they want to travel to and create buttons for the user to interact and answer the question 
Label(page3, text="What Region would you like to travel to?", font=("Helvetica", 20, "bold"), bg="light blue").pack(pady=30)

Button(page3, text="Australasia", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page8)).pack(pady=10)

Button(page3, text="Melanseia", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page9)).pack(pady=10)

Button(page3, text="Micronesia", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page10)).pack(pady=10)

Button(page3, text= "Polynesia", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page11)).pack(pady=10)

#Use labels and buttons for the user to interact with the project 
Label(page8, text="What are your expectations with travelling?", font=("Helvetica", 20, "bold"), bg="light blue").pack(pady=30)

Button(page8, text="Food", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page12)).pack(pady=10)

Button(page8, text="Scenery", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page13)).pack(pady=10)

Button(page8, text="Adventure", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page14)).pack(pady=10)

Button(page8, text= "Culture", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page15)).pack(pady=10)

#Create a label to ask the user a questions and buttons for the user to interact with and answer the question 
Label(page12, text="What city would you like to travel to?", font=("Helvetica", 20, "bold"), bg="light blue").pack(pady=30)

Button(page12, text="Sydney", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page13)).pack(pady=10)

Button(page12, text="Melbourne", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page14)).pack(pady=10)

Button(page12, text="Perth", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page15)).pack(pady=10)

Button(page12, text= "Hobart", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page16)).pack(pady=10)

#Use labels to allow the user to understand what is happening with the itinerary and buttons for the user to interact with 
Label(page13, text="You should visit Midden!", font=("Helvetica", 16, "bold"), bg="light blue").pack(pady=10)
Label(page13, text="It has a unique dining experience with a focus on,", font=("Helvetica", 16, "bold"), bg="light blue").pack(pady=10)
Label(page13, text="using native Australian ingredients!", font=("Helvetica", 16, "bold"), bg="light blue").pack(pady=10)
Label(page13, text="What are your other expectations with travelling?", font=("Helvetica", 16, "bold"), bg="light blue").pack(pady=10)

Button(page13, text="Scenery", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page17)).pack(pady=10)

Button(page13, text="Adventure", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page18)).pack(pady=10)

Button(page13, text= "Culture", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page19)).pack(pady=10)

#Use labels to highlight the travel itinerary and a button for the user to interact with 
Label(page17, text="You should visit the Blue Mountains!", font=("Helvetica", 16, "bold"), bg="light blue").pack(pady=10)
Label(page17, text="Just an hour and a half drive from the city.", font=("Helvetica", 16, "bold"), bg="light blue").pack(pady=10)
Label(page17, text="You are able to see the beauty of the Australian landscape!", font=("Helvetica", 16, "bold"), bg="light blue").pack(pady=10)
Button(page17, text="Finish Results", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page20)).pack(pady=10)

#Create an end page for the user, highlighting the final travel itinerary using labels and a button to restart the project 
Label(page20, text="Final Travel Itinerary", font=("Helvetica", 24, "bold"), bg="light blue").pack(pady=30)
Label(page20, text="You will be visiting Sydney, Australia!", font=("Helvetica", 16, "bold"), bg="light blue").pack(pady=10)
Label(page20, text="Where you will visit Midden to try Australian food,", font=("Helvetica", 16, "bold"), bg="light blue").pack(pady=10)
Label(page20, text="and the Blue Mountains for Sydney's beautiful outdoors!", font=("Helvetica", 16, "bold"), bg="light blue").pack(pady=10)
Button(page20, text="🏠 Restart Adventure", font=("Helvetica", 12), bg="white",
       command=lambda: show_frame(page1)).pack(pady=20)

root.mainloop()