from tkinter import *
import random

master = Tk(className="Best Game Ever")


# ----------------------------------------------------
# This checks to see if the guess is in the answer,
# then adds it to the correct place in the feedback
def guess():
    if dead == False:
        x = check.get()
        global response
        global answer
        global wrong_list
        global correct
        global incorrect
        guessed = False
        for i in wrong_list:
            if i == x:
                guessed = True
        if len(x) == 1 and guessed == False:
            if x in answer:
                for i in range(len(answer)):
                    if (answer[i] == x):
                        response[i] = x
                check.set("")
            else:
                incorrect += 1
                wrong_list += x
                check.set("")
        else:
            guessed = False
            check.set("")
        if "".join(answer) == "".join(response):
            answer = words[random.randint(0, len(words) - 1)]
            response = []
            wrong_list = []
            for letter in answer:
                response += "_"
            correct += 1
        return "".join(response)


# ----------------------------------------------------
# Updates the GUI
def update():
    global dead
    fill.set(response)
    wrong.set(wrong_list)
    score.set("Correct: " + str(correct))
    photo = PhotoImage(file=images[incorrect] + ".png")
    img.configure(image=photo)
    img.image = photo
    if (incorrect == 6):
        dead = True
    master.after(10, update)


# ----------------------------------------------------
# Allows user to use keyboard
def key(event):
    guess()


# ----------------------------------------------------
# Assigning variables correctly
check = StringVar()
fill = StringVar()
score = StringVar()
wrong = StringVar()
words = ["adjective", "nearly", "universe", "fort", "arrangement", "ruler", "character", "hospital", "ordinary", "vote",
         "money", "pale", "religious", "whistle", "body", "dropped", "you", "fireplace", "factory", "almost",
         "tropical", "detail", "noun", "loose", "stood", "collect", "discuss", "finally", "standard", "salt", "hunter",
         "pond", "dress", "ran", "eleven", "necessary", "saved", "wolf", "anybody", "cap", "lie", "against", "task",
         "percent", "satisfied", "change", "at", "stove", "told", "previous", "thrown", "characteristic", "smallest",
         "changing", "dinner", "please", "local", "successful", "see", "friend", "voice", "pain", "waste",
         "opportunity", "reader", "run", "theory", "yet", "parallel", "southern", "breakfast", "tales", "steep",
         "complex", "bar", "industrial", "congress", "reach", "heard", "selection", "wear", "where", "equator",
         "jungle", "though", "equally", "daughter", "phrase", "statement", "remain", "fat", "fact", "visitor", "milk",
         "huge", "boat", "replace", "thank", "sweet", "piece", "corn", "provide", "mix", "none", "folks", "hurried",
         "zero", "iron", "offer", "zoo", "create", "declared", "frog", "claws", "announced", "information", "service",
         "triangle", "minerals", "spider", "position", "population", "open", "promised", "cheese", "enjoy", "result",
         "right", "slightly", "engineer", "blew", "learn", "to", "rich", "hot", "beginning", "sing", "flight",
         "alphabet", "mice", "play", "direct", "angry", "length", "manner", "government", "glad", "noon", "silver",
         "get", "off", "window", "bottle", "instead", "century", "powder", "system", "finest", "path", "parts", "watch",
         "least", "number", "village", "certainly", "daily", "thou", "flat", "physical", "calm", "gentle", "direction",
         "twice", "than", "fighting", "sound", "muscle", "beyond", "best", "labor", "production", "team",
         "manufacturing", "copy", "construction", "grass", "flag", "over", "already"]
wrong_list = []
response = []
answer = []
answer = words[random.randint(0, len(words) - 1)]
dead = False
for letter in answer:
    response += "_"
correct = 0
incorrect = 0
images = ["0", "1", "2", "3", "4", "5", "6"]
photo = PhotoImage(file= images[incorrect] + ".png")
# ----------------------------------------------------
# Builds the GUI
img = Label(master, image=photo)
img.grid(row=0, column=0)
count = Label(master, width=20, textvariable=wrong, font=("Helvetica", 16))
count.grid(row=0, column=1)
count = Label(master, width=20, textvariable=score, font=("Helvetica", 16))
count.grid(row=1, column=0, columnspan=2)
other = Label(master, width=20, textvariable=fill, font=("Helvetica", 16))
other.grid(row=2, column=0, columnspan=2)
entry = Entry(master, textvariable=check, width=10, font=("Helvetica", 16))
entry.bind("<Return>", key)
entry.grid(padx=5, pady=5, row=3, column=0)
button = Button(master, text="Guess", width=10, command=guess, font=("Helvetica", 16))
button.grid(padx=5, pady=5, row=3, column=1)
update()
master.mainloop()
