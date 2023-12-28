import turtle as t
import pandas

s = t.Screen()
s.title("US States Game")
img = "states.gif"
s.addshape(img)
t.shape(img)

data = pandas.read_csv("50_states.csv")

t1 = t.Turtle()
t1.penup()
guessed = []
while len(guessed) <= 50:
    guess = s.textinput(title = 'Guess the state', prompt = "What's another state's name?").title()
    if guess == "Exit":
        print("you gotta learn",[state for state in data.state.to_list() if state not in guessed])
        break

    elif guess in guessed:
        print("already guessed")

    elif guess in data.state.to_list():
        guessed.append(guess)
        curr = data[data.state == guess]
        t1.goto(int(curr.x.iloc[0]), int(curr.y.iloc[0]))
        t1.write(guess)

t.bye()
