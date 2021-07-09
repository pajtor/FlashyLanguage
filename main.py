from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

score_correct = 0
score_wrong = 0

# csv
german_csv = "data/1k_german.csv"
spanish_csv = "data/1k_spanish.csv"
french_csv = "data/1k_french.csv"
# russian_csv = "data/1k_russian.csv"
turkish_csv = "data/1k_turkish.csv"
# data
data_german = pandas.read_csv(german_csv)
data_spanish = pandas.read_csv(spanish_csv)
data_french = pandas.read_csv(french_csv)
# data_russian = pandas.read_csv(russian_csv)
data_turkish = pandas.read_csv(turkish_csv)
to_learn_german = data_german.to_dict(orient="records")
to_learn_spanish = data_spanish.to_dict(orient="records")
to_learn_french = data_french.to_dict(orient="records")
# to_learn_russian = data_russian.to_dict(orient="records")
to_learn_turkish = data_turkish.to_dict(orient="records")

score_remaining_german = 1000
score_remaining_spanish = 1000
score_remaining_french = 1000
score_remaining_russian = 1000
score_remaining_turkish = 1000


##### French START #####
def next_card_french():
    global current_card, flip_timer, score_wrong
    current_card = random.choice(to_learn_french)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    check_mark.config(command=is_known_french)
    x_mark.config(command=next_card_wrong_french)
    window.title("Learn French")
    square_flag_2.config(image=square_flag_fr, command=flip_back_french)
    square_flag_1.config(image=square_flag_gb, command=flip_french)


def next_card_wrong_french():
    global current_card, flip_timer, score_wrong
    current_card = random.choice(to_learn_french)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    score_wrong += 1
    label_wrong.config(text=f"Wrong: {score_wrong}")


def flip_french():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def flip_back_french():
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)


def is_known_french():
    global score_correct, score_remaining_french
    to_learn_french.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    # data.to_csv("data/words_to_learn.csv", index=False)
    score_correct += 1
    score_remaining_french -= 1
    label_correct.config(text=f"Correct: {score_correct}")
    label_remaining.config(text=f"Remaining Words: {score_remaining_french}")
    if score_remaining_french == 0:
        label_remaining.config(text=f"Ran out of words. Congrats!")
    next_card_french()


##### French END #####

##### German START #####
def next_card_german():
    global current_card, flip_timer, score_wrong
    current_card = random.choice(to_learn_german)
    canvas.itemconfig(card_title, text="German", fill="black")
    canvas.itemconfig(card_word, text=current_card["German"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    check_mark.config(command=is_known_german)
    x_mark.config(command=next_card_wrong_german)
    window.title("Learn German")
    square_flag_2.config(image=square_flag_de, command=flip_back_german)
    square_flag_1.config(image=square_flag_gb, command=flip_german)


def next_card_wrong_german():
    global current_card, flip_timer, score_wrong
    current_card = random.choice(to_learn_german)
    canvas.itemconfig(card_title, text="German", fill="black")
    canvas.itemconfig(card_word, text=current_card["German"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    score_wrong += 1
    label_wrong.config(text=f"Wrong: {score_wrong}")


def flip_german():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def flip_back_german():
    canvas.itemconfig(card_title, text="German", fill="black")
    canvas.itemconfig(card_word, text=current_card["German"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)


def is_known_german():
    global score_correct, score_remaining_german
    to_learn_german.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    # data.to_csv("data/words_to_learn.csv", index=False)
    score_correct += 1
    score_remaining_german -= 1
    label_correct.config(text=f"Correct: {score_correct}")
    label_remaining.config(text=f"Remaining Words: {score_remaining_german}")
    if score_remaining_german == 0:
        label_remaining.config(text=f"Ran out of words. Congrats!")
    next_card_german()


##### German END #####

##### Spanish START #####
def next_card_spanish():
    global current_card, flip_timer, score_wrong
    current_card = random.choice(to_learn_spanish)
    canvas.itemconfig(card_title, text="Spanish", fill="black")
    canvas.itemconfig(card_word, text=current_card["Spanish"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    check_mark.config(command=is_known_spanish)
    x_mark.config(command=next_card_wrong_spanish)
    window.title("Learn Spanish")
    square_flag_2.config(image=square_flag_es, command=flip_back_spanish)
    square_flag_1.config(image=square_flag_gb, command=flip_spanish)


def next_card_wrong_spanish():
    global current_card, flip_timer, score_wrong
    current_card = random.choice(to_learn_spanish)
    canvas.itemconfig(card_title, text="Spanish", fill="black")
    canvas.itemconfig(card_word, text=current_card["Spanish"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    score_wrong += 1
    label_wrong.config(text=f"Wrong: {score_wrong}")


def flip_spanish():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def flip_back_spanish():
    canvas.itemconfig(card_title, text="Spanish", fill="black")
    canvas.itemconfig(card_word, text=current_card["Spanish"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)


def is_known_spanish():
    global score_correct, score_remaining_spanish
    to_learn_spanish.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    # data.to_csv("data/words_to_learn.csv", index=False)
    score_correct += 1
    score_remaining_spanish -= 1
    label_correct.config(text=f"Correct: {score_correct}")
    label_remaining.config(text=f"Remaining Words: {score_remaining_spanish}")
    if score_remaining_spanish == 0:
        label_remaining.config(text=f"Ran out of words. Congrats!")
    next_card_spanish()


##### Spanish END #####

##### Turkish START #####
def next_card_turkish():
    global current_card, flip_timer, score_wrong
    current_card = random.choice(to_learn_turkish)
    canvas.itemconfig(card_title, text="Turkish", fill="black")
    canvas.itemconfig(card_word, text=current_card["Turkish"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    check_mark.config(command=is_known_turkish)
    x_mark.config(command=next_card_wrong_turkish)
    window.title("Learn Turkish")
    square_flag_2.config(image=square_flag_tr, command=flip_back_turkish)
    square_flag_1.config(image=square_flag_gb, command=flip_turkish)


def next_card_wrong_turkish():
    global current_card, flip_timer, score_wrong
    current_card = random.choice(to_learn_turkish)
    canvas.itemconfig(card_title, text="Turkish", fill="black")
    canvas.itemconfig(card_word, text=current_card["Turkish"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    score_wrong += 1
    label_wrong.config(text=f"Wrong: {score_wrong}")


def flip_turkish():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def flip_back_turkish():
    canvas.itemconfig(card_title, text="Turkish", fill="black")
    canvas.itemconfig(card_word, text=current_card["Turkish"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)


def is_known_turkish():
    global score_correct, score_remaining_turkish
    to_learn_turkish.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    # data.to_csv("data/words_to_learn.csv", index=False)
    score_correct += 1
    score_remaining_turkish -= 1
    label_correct.config(text=f"Correct: {score_correct}")
    label_remaining.config(text=f"Remaining Words: {score_remaining_turkish}")
    if score_remaining_turkish == 0:
        label_remaining.config(text=f"Ran out of words. Congrats!")
    next_card_turkish()


##### Turkish END #####


window = Tk()
window.title("Learn Language")
window.config(padx=50, pady=15, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Select Flag", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=1, column=0, columnspan=5)

# check marks
x_mark_image = PhotoImage(file="images/wrong.png")
x_mark = Button(image=x_mark_image, highlightthickness=0)
x_mark.grid(row=2, column=0)
check_mark_image = PhotoImage(file="images/right.png")
check_mark = Button(image=check_mark_image, highlightthickness=0)
check_mark.grid(row=2, column=4)
# square flags
square_flag_fr = PhotoImage(file="images/square_fr.png")
square_flag_de = PhotoImage(file="images/square_de.png")
square_flag_ru = PhotoImage(file="images/square_ru.png")
square_flag_es = PhotoImage(file="images/square_es.png")
square_flag_tr = PhotoImage(file="images/square_tr.png")
square_flag_gb = PhotoImage(file="images/square_gb.png")
square_flag_1 = Button(image=square_flag_gb, highlightthickness=0)
square_flag_2 = Button(image=square_flag_tr, highlightthickness=0)
square_flag_1.grid(row=2, column=1, sticky="e", padx=25)
square_flag_2.grid(row=2, column=3, sticky="w", padx=25)
# round flags
round_flag_de = PhotoImage(file="images/round_de.png")
round_flag_es = PhotoImage(file="images/round_es.png")
round_flag_fr = PhotoImage(file="images/round_fr.png")
round_flag_ru = PhotoImage(file="images/round_ru.png")
round_flag_tr = PhotoImage(file="images/round_tr.png")
round_flag_de_button = Button(image=round_flag_de, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card_german)
round_flag_es_button = Button(image=round_flag_es, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card_spanish)
round_flag_fr_button = Button(image=round_flag_fr, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card_french)
round_flag_ru_button = Button(image=round_flag_ru, highlightthickness=0, bg=BACKGROUND_COLOR)
round_flag_tr_button = Button(image=round_flag_tr, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card_turkish)
round_flag_de_button.grid(row=0, column=0, pady=15)
round_flag_es_button.grid(row=0, column=1, pady=15)
round_flag_fr_button.grid(row=0, column=2, pady=15)
round_flag_ru_button.grid(row=0, column=3, pady=15)
round_flag_tr_button.grid(row=0, column=4, pady=15)

label_correct = Label(text=f"Correct: {score_correct}", font=("Arial", 20))
label_correct.grid(row=3, column=3, sticky="s", padx=50)
label_wrong = Label(text=f"Wrong: {score_wrong}", font=("Arial", 20))
label_wrong.grid(row=3, column=1, sticky="n", padx=50)
label_remaining = Label(text=f"Remaining Words: {score_remaining_french}",
                        font=("Arial", 15))  # her dile özel skor gösterimi ayarlanacak
label_remaining.grid(row=2, column=2)

window.mainloop()
