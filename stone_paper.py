import random
uscore = 0
cscore = 0
while True:
    print(f"current user score:{uscore},current computer score:{cscore} \n")
    user = int(input("your move 1 for stone , 2 for scissor , 3 for paper \n"))
    comp = random.randint(1,3)

    if user == 1 and comp == 2:
        uscore+=1
        print("user won ")
    elif user == 2 and comp == 3:
        uscore+=1
        print("user won ")
    elif user == 3 and comp == 1:
        uscore+=1
        print("user won ")
    elif user == comp :
        print("Draw")
    else:
        print("computer won")
        cscore+=1
    if uscore==5:
        print("USER WON THE GAME")
        break
    elif cscore == 5:
        print("COMPUTER WON THE GAME")
        break
      
      
      
      # UI FOR STONE PAPER SCISSOR   
# import tkinter as tk
# import random

# # ---------------- GAME VARIABLES ----------------
# uscore = 0
# cscore = 0

# # ---------------- GAME FUNCTION ----------------
# def play(user):
#     global uscore, cscore

#     comp = random.randint(1, 3)

#     choices = {
#         1: "🪨 Stone",
#         2: "✂️ Scissor",
#         3: "📄 Paper"
#     }

#     user_choice.config(text="You: " + choices[user])
#     computer_choice.config(text="Computer: " + choices[comp])

#     # User wins
#     if (user == 1 and comp == 2) or \
#        (user == 2 and comp == 3) or \
#        (user == 3 and comp == 1):

#         uscore += 1
#         result.config(text="🎉 You Won!", fg="green")

#     # Draw
#     elif user == comp:
#         result.config(text="🤝 Draw!", fg="orange")

#     # Computer wins
#     else:
#         cscore += 1
#         result.config(text="💻 Computer Won!", fg="red")

#     score.config(text=f"You   {uscore}  :  {cscore}   Computer")

#     # Check winner
#     if uscore == 5:
#         result.config(text="🏆 YOU WON THE GAME!", fg="green")
#         disable_buttons()

#     elif cscore == 5:
#         result.config(text="💻 COMPUTER WON THE GAME!", fg="red")
#         disable_buttons()


# # ---------------- DISABLE BUTTONS ----------------
# def disable_buttons():
#     stone_button.config(state="disabled")
#     scissor_button.config(state="disabled")
#     paper_button.config(state="disabled")


# # ---------------- RESET GAME ----------------
# def reset():
#     global uscore, cscore

#     uscore = 0
#     cscore = 0

#     score.config(text="You   0  :  0   Computer")
#     user_choice.config(text="You: -")
#     computer_choice.config(text="Computer: -")
#     result.config(text="Choose your move!", fg="black")

#     stone_button.config(state="normal")
#     scissor_button.config(state="normal")
#     paper_button.config(state="normal")


# # ---------------- WINDOW ----------------
# root = tk.Tk()
# root.title("Stone Scissor Paper")
# root.geometry("600x600")
# root.resizable(False, False)
# root.configure(bg="#f4f4f4")


# # ---------------- TITLE ----------------
# title = tk.Label(
#     root,
#     text="STONE • SCISSOR • PAPER",
#     font=("Arial", 24, "bold"),
#     bg="#f4f4f4"
# )
# title.pack(pady=25)


# subtitle = tk.Label(
#     root,
#     text="First to 5 points wins!",
#     font=("Arial", 13),
#     bg="#f4f4f4"
# )
# subtitle.pack()


# # ---------------- SCORE ----------------
# score = tk.Label(
#     root,
#     text="You   0  :  0   Computer",
#     font=("Arial", 22, "bold"),
#     bg="#f4f4f4"
# )
# score.pack(pady=30)


# # ---------------- CHOICES ----------------
# user_choice = tk.Label(
#     root,
#     text="You: -",
#     font=("Arial", 16),
#     bg="#f4f4f4"
# )
# user_choice.pack(pady=5)


# computer_choice = tk.Label(
#     root,
#     text="Computer: -",
#     font=("Arial", 16),
#     bg="#f4f4f4"
# )
# computer_choice.pack(pady=5)


# # ---------------- RESULT ----------------
# result = tk.Label(
#     root,
#     text="Choose your move!",
#     font=("Arial", 20, "bold"),
#     bg="#f4f4f4"
# )
# result.pack(pady=25)


# # ---------------- BUTTONS ----------------
# button_frame = tk.Frame(root, bg="#f4f4f4")
# button_frame.pack(pady=15)


# stone_button = tk.Button(
#     button_frame,
#     text="🪨\nStone",
#     font=("Arial", 14, "bold"),
#     width=10,
#     height=3,
#     command=lambda: play(1)
# )
# stone_button.grid(row=0, column=0, padx=10)


# scissor_button = tk.Button(
#     button_frame,
#     text="✂️\nScissor",
#     font=("Arial", 14, "bold"),
#     width=10,
#     height=3,
#     command=lambda: play(2)
# )
# scissor_button.grid(row=0, column=1, padx=10)


# paper_button = tk.Button(
#     button_frame,
#     text="📄\nPaper",
#     font=("Arial", 14, "bold"),
#     width=10,
#     height=3,
#     command=lambda: play(3)
# )
# paper_button.grid(row=0, column=2, padx=10)


# # ---------------- RESET BUTTON ----------------
# reset_button = tk.Button(
#     root,
#     text="🔄  Play Again",
#     font=("Arial", 13, "bold"),
#     width=15,
#     command=reset
# )
# reset_button.pack(pady=30)


# root.mainloop()