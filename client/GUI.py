import tkinter
import tkinter.messagebox
import customtkinter
from Match import Match
import Player

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

import tkinter as tk
from tkinter import messagebox
from Result import Result
from Player import Player


class LoginWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.master.geometry("300x200")

        self.label_username = tk.Label(self.master, text="Username")
        self.label_username.pack()

        self.entry_username = tk.Entry(self.master)
        self.entry_username.pack()

        self.label_password = tk.Label(self.master, text="Password")
        self.label_password.pack()

        self.entry_password = tk.Entry(self.master, show="*")
        self.entry_password.pack()

        self.button_login = tk.Button(self.master, text="Login", command=self.login)
        self.button_login.pack()

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        print(username, password)
        match_obj = Match()
        result_obj = match_obj.login(username=username, password=password)

        if result_obj.error == Result.ErrorCode.ok:
            self.master.destroy()
            main_window = MainWindow(result_obj.value)
        else:
            messagebox.showerror("Error", "Invalid username or password")


class MainWindow:
    def __init__(self, player: Player):
        self.player = player
        self.match_obj = Match()
        self.master = tk.Tk()
        self.master.title("Main Window")
        self.master.geometry("300x200")

        self.label_welcome = tk.Label(master=self.master, text="Welcome, %s" % self.player.name)
        self.label_welcome.pack()

        self.button_join_room = tk.Button(master=self.master, text="Join Room", command=self.join_room)
        self.button_join_room.pack()

        self.button_view_champs_dict = tk.Button(master=self.master, text="View Champs Dict",
                                                 command=self.view_champs_dict)
        self.button_view_champs_dict.pack()


        self.room_box = tk.LabelFrame(master=self.master)
        self.room_box.pack(fill="both", expand="yes", padx=10, pady=10)

        self.player_list_label = tk.Label(master=self.room_box, text="", font=("Arial", 12))
        self.player_list_label.pack()

    def join_room(self):
        self.match_obj.player_list.append((self.player))

        # Update the player list label with the updated player list
        player_list_text = ""
        for i, player in enumerate(self.match_obj.player_list, start=1):
            player_list_text += "Player  %d : %s\n" % (i, player)
        self.player_list_label.config(text=player_list_text)

    def view_champs_dict(self):
        champs_dict = self.player.champ_dict
        messagebox.showinfo("Champs Dict", str(champs_dict))


if __name__ == '__main__':
    root = tk.Tk()
    login_window = LoginWindow(root)
    root.mainloop()
