from tkinter import *
from word import Word
BACKGROUND_COLOR = "#B1DDC6"

#data extract part
word=Word()
def flip_card(event):
    print("This is called")
    word.is_French=not word.is_French
    if word.is_French:
        create_french_word()
    else:
        canvas.itemconfig(card_word, text=word.english_word)
        canvas.itemconfig(card_text, text="English")
        canvas.itemconfig(card_image, image=card_back_image)

def create_french_word():
    canvas.itemconfig(card_word, text=word.french_word)
    canvas.itemconfig(card_text, text="French")
    canvas.itemconfig(card_image, image=card_front_image)

def right_button_click():
    word.learn(word.data)
    next_word()
    create_french_word()

def wrong_button_click():
    next_word()
    create_french_word()

def next_word():
    if word.empty:
        window.destroy()
    else:
        word.generate_word()

def create_file():
    word.create_file()
    window.destroy()

def sound():
    print(word.is_French)
    if word.is_French:
        word.speak_word(word.french_word,"French")
    else:
        word.speak_word(word.english_word,"English")
window = Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.resizable(False, False)
window.protocol("WM_DELETE_WINDOW",create_file)
# Canvas
canvas = Canvas(window,width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)

card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")

card_image = canvas.create_image(400, 263, image=card_front_image)
card_text =canvas.create_text(385,171,text="French",font=("Arial",25,"bold"))
card_word=canvas.create_text(385,271,text=word.french_word,font=("Arial",25,"bold"))
canvas.grid(row=0, column=0, columnspan=2, pady=20)
canvas.tag_bind(card_image,"<Button-1>", flip_card)
canvas.tag_bind(card_text,"<Button-1>", flip_card)
canvas.tag_bind(card_word,"<Button-1>", flip_card)
# Buttons
right_image = PhotoImage(file="./images/right.png")
wrong_image = PhotoImage(file="./images/wrong.png")

wrong_button = Button(image=wrong_image,highlightthickness=0,
                      bd=0,bg=BACKGROUND_COLOR,
                      activebackground=BACKGROUND_COLOR,command=wrong_button_click
                      )
right_button = Button(image=right_image,highlightthickness=0,
                      bd=0,bg=BACKGROUND_COLOR,
                      activebackground=BACKGROUND_COLOR,command=right_button_click)
wrong_button.grid(row=1, column=0, padx=40, pady=20)
right_button.grid(row=1, column=1, padx=40, pady=20)
sound_button = Button(
    window, text="🔊",
    command=sound,
    bg=BACKGROUND_COLOR, bd=0
)
sound_button.place(x=470,y=171)
window.mainloop()
