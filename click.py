import tkinter as tk
from tkinter import simpledialog

class ClickCounterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("FawokClicker")

        self.load_settings()

        self.label = tk.Label(master, text=f"Количество кликов: {self.click_count}", font=("Helvetica", 16), fg="white")
        self.label.pack(pady=10)

        self.button_text = self.get_button_text()
        self.button = tk.Button(master, text=self.button_text, command=self.increment_click, font=("Helvetica", 12))
        self.button.pack()

        self.reset_button_text = self.get_reset_button_text()
        self.reset_button = tk.Button(master, text=self.reset_button_text, command=self.reset_clicks, font=("Helvetica", 12), bg="lightcoral")
        self.reset_button.pack()

        self.master.resizable(width=False, height=False)

        self.master.protocol("WM_DELETE_WINDOW", self.save_settings_on_exit)

    def increment_click(self):
        self.click_count += 1
        self.label.config(text=f"Количество кликов: {self.click_count}")

    def reset_clicks(self):
        self.click_count = 0
        self.label.config(text=f"Количество кликов: {self.click_count}")

    def load_settings(self):
        try:
            with open("cfg.fawok", "r", encoding="utf-8") as file:
                data = file.readlines()
                self.click_count = int(data[0].strip()) if data and data[0].strip().isdigit() else 0
                self.country = data[1].strip() if data and len(data) > 1 else ""
                self.language = data[2].strip() if data and len(data) > 2 else ""
        except FileNotFoundError:
            self.click_count = 0
            self.country = ""
            self.language = ""

        self.choose_language()

    def save_settings_on_exit(self):
        self.save_settings()
        self.master.destroy()

    def save_settings(self):
        with open("cfg.fawok", "w", encoding="utf-8") as file:
            file.write(f"{self.click_count}\n{self.country}\n{self.language}")

    def choose_language(self):
        if not self.language:
            result = simpledialog.askstring("Выбор языка", "Выберите язык (USA или RUSSIA):")
            if result and result.upper() in ["USA", "RUSSIA"]:
                self.language = result.upper()
                self.country = "Россия" if self.language == "RUSSIA" else "USA"
            else:
                self.language = "RUSSIA"
                self.country = "Россия"

    def get_button_text(self):
        if self.language == "RUSSIA":
            return "Кликнуть"
        elif self.language == "USA":
            return "Click"
        else:
            return "Click"

    def get_reset_button_text(self):
        if self.language == "RUSSIA":
            return "Сбросить клики"
        elif self.language == "USA":
            return "Reset Clicks"
        else:
            return "Reset Clicks"\

if __name__ == "__main__":
    root = tk.Tk()
    app = ClickCounterApp(root)
    root.mainloop()
