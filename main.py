from tkinter import *

import pandas
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
CARD_BACKGROUND_COLOR = "#91C2AF"
french_word = ""
english_word = ""
dict_index = 0
is_french = True
# --------------------| Wrong Button |------------------------
def wrong_button_pressed():

    print("wrong")


    get_random_word()


# --------------------| Right Button |------------------------
def right_button_pressed():

    print("right!")
    data_dict.pop(dict_index)
    words_to_study_data = pandas.DataFrame(data_dict)
    words_to_study_data.to_csv("data/words_to_learn.csv", index=False)

    get_random_word()


# --------------------| Flash Cards |------------------------

def get_random_word():
    global french_word
    global english_word
    global dict_index

    dict_index = random.randint(0, len(data_dict) - 1)
    print(dict_index)
    random_dict = data_dict[dict_index]

    french_word = random_dict['French']
    english_word = random_dict['English']
    word_label.config(text=french_word)

    print("Random Pair:", {'French': french_word, 'English': english_word})


def flip_card():
    print("countdown")
    global is_french
    if is_french:
        canvas.image = canvas.create_image(430,314, image = back_card_image)
        word_label.config(text=english_word,bg=CARD_BACKGROUND_COLOR,fg="white",)
        language_label.config(text="English",bg=CARD_BACKGROUND_COLOR,fg="white")
        is_french = False

    else:

        canvas.image = canvas.create_image(430, 314, image=front_card_image)
        word_label.config(text=french_word, bg="white", fg="black")
        language_label.config(text="French", bg="white", fg="black")
        is_french = True

    window.after(3000,flip_card)
# --------------------| UI |------------------------


window = Tk()
window.title("Flashy")
window.geometry("1000x750")
window.config(padx=50,pady=50)
window.config(bg=BACKGROUND_COLOR)

try:
    df = pd.read_csv("data/words_to_learn.csv")
    data_dict = df.to_dict(orient="records")
    print("file found")

except FileNotFoundError:
    df = pd.read_csv("data/french_words.csv")
    data_dict = df.to_dict(orient="records")
    print("first time opening game")

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image,highlightthickness=0,command=wrong_button_pressed)
wrong_button.grid(column=0,row=1)
wrong_button.config(padx=50,pady=50)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image,highlightthickness=0,command=right_button_pressed)
right_button.grid(column=1,row=1)
right_button.config(padx=50,pady=50)

canvas = Canvas(width=820, height=570)
front_card_image = PhotoImage(file="images/card_front.png")
back_card_image = PhotoImage(file="images/card_back.png")
canvas.create_image(430, 314, image=front_card_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

word_label = Label(text=french_word,bg="white",font=("Arial", 60, "bold"))
language_label = Label(text="French",bg="white",font=("Arial", 40, "bold"))
word_label.place(x=425,y=330,anchor="center")
language_label.place(x=425,y=150,anchor="center")

get_random_word()
canvas.grid(column=0,row=0,columnspan=2)
window.after(3000,flip_card)


window.mainloop()