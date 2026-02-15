# Import & from statements that is the "glue" that holds this project together 
import tkinter as tk
import random
from PIL import Image, ImageTk
# Initial positions of the players black & white
white = 1
black = 1
# Size of the grid size
spot = 70
# First player is the black piece
player_1 = "black"
# Boolean value that gets the reset function going
game_over = False
# Function for animation of the pieces
def animate_piece(piece, end_x, end_y, steps=20, delay=20):
    start_x, start_y = canvas.coords(piece)
    distance_x = (end_x - start_x) / steps
    distance_y = (end_y - start_y) / steps
    def step(step_num=0):
        if step_num <= steps:
            canvas.coords(piece, start_x + distance_x*step_num, start_y + distance_y*step_num)
            canvas.after(delay, step, step_num+1)
    step()
# Function for rolling the dice
def roll_dice():
    global player_1, game_over
    # Conditional to restart the game
    if game_over:
        reset()
        game_over = False
        return
    dice_number = random.randint(1, 6)
    # Prints a random number on the GUI
    show_dice.config(text=f"{player_1} rolled: {dice_number}")
    #canvas.update()
    # Moves the black piece depending on the number rolled
    if player_1 == "black":
        move_black(dice_number)
        #canvas.update()
        ladders()
        #canvas.update()
        snakes()
        #canvas.update()
        player_1 = "white"
    # Moves the white piece depending on the number rolled
    else:
        move_white(dice_number)
        #canvas.update()
        ladders()
        #canvas.update()
        snakes()
        #canvas.update()
        player_1 = "black"
    winner()
# This function does not allow the white piece to move above 100
def move_white(dice_number):
    global white
    white += dice_number
    if white > 100:
        white = 100
    update_white_piece_position()
# Updates the position of the white piece on the board
def update_white_piece_position():
    global white
    row = (white - 1) // 10
    column = (white - 1) % 10
    if row % 2 == 1:
        column = 9 - column
    x = column * spot + 2
    y = 650 - (row * spot)
    animate_piece(white_piece, x, y)
# This function does not allow the black piece to move above 100
def move_black(dice_number):
    global black
    black += dice_number
    if black > 100:
        black = 100
    update_black_piece_position()
# Updates the position of the black piece on the board
def update_black_piece_position():
    global black
    row = (black - 1) // 10
    column = (black - 1) % 10
    if row % 2 == 1:
        column = 9 - column
    x = column * spot + 35
    y = 650 - (row * spot)
    animate_piece(black_piece, x, y)
# Function on the spots that have the ladders & forces the player to go up
def ladders():
    global black, white

    if player_1 == "black":
        if black == 2: black = 23
        elif black == 6: black = 45
        elif black == 20: black = 59
        elif black == 52: black = 72
        elif black == 57: black = 96
        elif black == 71: black = 92
        update_black_piece_position()

    else:
        if white == 2: white = 23
        elif white == 6: white = 45
        elif white == 20: white = 59
        elif white == 52: white = 72
        elif white == 57: white = 96
        elif white == 71: white = 92
        update_white_piece_position()
# Function on the spots that have the snakes & forces the player to go down
def snakes():
    global black, white

    if player_1 == "black":
        if black == 50: black = 5
        elif black == 56: black = 8
        elif black == 73: black = 15
        elif black == 87: black = 49
        elif black == 43: black = 17
        elif black == 98: black = 40
        elif black == 84: black = 63
        update_black_piece_position()

    else:
        if white == 50: white = 5
        elif white == 56: white = 8
        elif white == 73: white = 15
        elif white == 87: white = 49
        elif white == 43: white = 17
        elif white == 98: white = 40
        elif white == 84: white = 63
        update_white_piece_position()
# Function for determining the winner
def winner():
    global game_over
    if black == 100:
        if player_1 == "white":
            win.config(text="black wins Snakes & Ladders!")
            game_over = True
    elif white == 100:
        if player_1 == "black":
            win.config(text="white wins Snakes & Ladders!")
            game_over = True
# Reset function which allows to reset the game & restart 
def reset():
    global black, white, player_1, game_over
    if black == 100 or white == 100:
        black = 1
        white = 1
        player_1 = "black"
        update_black_piece_position()   
        update_white_piece_position()
        win.config(text="")
        show_dice.config(text="")
# GUI Setup 
background = tk.Tk()
background.geometry("360x360")
background.title("Snakes and Ladders")
# Title "Snakes & Ladders" printed 
title = tk.Label(background, text="Snakes and Ladders", font=("Times New Roman", 25))
title.pack(pady=12)
canvas = tk.Canvas(background, height=(900), width=(900))
canvas.pack(pady=15)
# Snakes & Ladders board printed on the GUI
bg_image = Image.open("Snakes_and_Ladders.png")
bg_image = bg_image.resize((700, 700))
bg_photo = ImageTk.PhotoImage(bg_image)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")
# Button on the dice
dice_button = tk.Button(background, text="Dice", font=("Times New Roman", 25), command=roll_dice)
dice_button.place(x=1200, y=240)
# Prints out the text of whatever number on the dice is rolled
show_dice= tk.Label(background, text="", font=("Times New Roman", 25))
show_dice.place(x=1160, y=310)
# Black piece image and establishing it on background
black_piece_img = Image.open("black.png").resize((30,30))
black_piece_photo = ImageTk.PhotoImage(black_piece_img)
black_piece = canvas.create_image(0, 650, image=black_piece_photo, anchor="nw")
# White piece image and establishing it on background
white_piece_img = Image.open("white.png").resize((30,30))
white_piece_photo = ImageTk.PhotoImage(white_piece_img)
white_piece = canvas.create_image(35, 650, image=white_piece_photo, anchor="nw")
# Prints the text of whoever player wins the game
win = tk.Label(background, text="", font=("Times New Roman", 25))
win.place(x=1090, y=350)
# Runs game
background.mainloop()