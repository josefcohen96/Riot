from Match import Match
import tkinter as tk
from tkinter import messagebox
from Result import Result
from Player import Player
import logging


class LoginWindow:
    def __init__(self, master):
        # requests.get()
        # todo add connection to server
        self.master = master
        self.master.title("Login")
        self.master.geometry("300x200")

        self.label_username = tk.Label(self.master, text="Username", font=("Roboto", 14), bg='#F2F2F2')
        self.label_username.pack()

        self.entry_username = tk.Entry(self.master, font=("Roboto", 12))
        self.entry_username.pack()

        self.label_password = tk.Label(self.master, text="Password", font=("Roboto", 14), bg='#F2F2F2')
        self.label_password.pack()

        self.entry_password = tk.Entry(self.master, show="*", font=("Roboto", 12))
        self.entry_password.pack()

        self.button_login = tk.Button(self.master, text="Login", command=self.login, font=("Roboto", 12), bg="#0D47A1",
                                      fg="#FFFFFF")
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
        self.master.geometry("400x400")

        self.label_welcome = tk.Label(master=self.master, text="Welcome, %s" % self.player.name)
        self.label_welcome.pack()

        self.button_join_room = tk.Button(master=self.master, text="Join Room", command=self.join_room)
        self.button_join_room.pack()

        self.button_leave_room = tk.Button(master=self.master, text="Leave Room", command=self.leave_room,
                                           state=tk.DISABLED)
        self.button_leave_room.pack()

        self.button_view_champs_dict = tk.Button(master=self.master, text="View Champs Dict",
                                                 command=self.view_champs_dict)
        self.button_view_champs_dict.pack()

        self.room_box = tk.LabelFrame(master=self.master)
        self.room_box.pack(fill="both", expand="yes", padx=10, pady=10)

        self.player_list_label = tk.Label(master=self.room_box, text="", font=("Arial", 12))
        self.player_list_label.pack()

    def join_room(self):

        self.match_obj.player_list.append(self.player)

        # Update the player list label with the updated player list
        player_list_text = ""
        for i, player in enumerate(self.match_obj.player_list, start=1):
            player_list_text += "Player  %d : %s\n" % (i, player)
        self.player_list_label.config(text=player_list_text)

        self.button_join_room.config(state=tk.DISABLED)
        self.button_leave_room.config(state=tk.NORMAL)

    def leave_room(self):
        if self.player not in self.match_obj.player_list:
            messagebox.showinfo("Info", "You are not in the room.")
            return

        self.match_obj.player_list.remove(self.player)

        # Update the player list label with the updated player list
        player_list_text = ""
        for i, player in enumerate(self.match_obj.player_list, start=1):
            player_list_text += "Player  %d : %s\n" % (i, player)
        self.player_list_label.config(text=player_list_text)

        # Disable the "Leave Room" button and enable the "Join Room" button
        self.button_leave_room.config(state=tk.DISABLED)
        self.button_join_room.config(state=tk.NORMAL)

    def view_champs_dict(self):
        champs_dict = self.player.champ_dict
        messagebox.showinfo("Champs Dict", str(champs_dict))


if __name__ == '__main__':
    logging.basicConfig(filename='MyApp.log', level=logging.DEBUG)
    logging.info('Starting MyApp')
    root = tk.Tk()
    login_window = LoginWindow(root)
    root.mainloop()
    # input("Press Enter to continue...")
    logging.info('Exiting MyApp')

