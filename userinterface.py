import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog

# Classic Windows 90s colors & fonts
WINDOW_BG = '#c0c0c0'
BUTTON_BG = '#e0e0e0'
BUTTON_FG = '#000080'
FONT = ('MS Sans Serif', 10)

class YouTubeUtilityUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("YouTube Utilities - Candlelight Foundation")
        self.geometry("500x400")
        self.configure(bg=WINDOW_BG)
        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(self, text="YouTube Utilities", font=('MS Sans Serif', 14, 'bold'), bg=WINDOW_BG, fg='#000080')
        title.pack(pady=(10, 0))

        subtitle = tk.Label(self, text="A collection of scripts to make YouTube tasks easier", font=FONT, bg=WINDOW_BG)
        subtitle.pack(pady=(0, 20))

        # Buttons for each utility (update these as you add scripts)
        button_frame = tk.Frame(self, bg=WINDOW_BG)
        button_frame.pack(pady=10)

        self.add_utility_button(button_frame, "Download Video", self.download_video)
        self.add_utility_button(button_frame, "Get Video Info", self.get_video_info)
        self.add_utility_button(button_frame, "Manage Playlists", self.manage_playlists)
        self.add_utility_button(button_frame, "Batch Process", self.batch_process)

        # Add plain retro graphics (lines/boxes)
        canvas = tk.Canvas(self, width=460, height=80, bg=WINDOW_BG, highlightthickness=0)
        canvas.pack(pady=(30, 0))
        canvas.create_rectangle(10, 10, 450, 70, outline='#000080', width=2)
        canvas.create_line(10, 40, 450, 40, fill='#000080')
        canvas.create_text(230, 25, text="Retro Status Bar", font=FONT, fill='#000080')
        canvas.create_text(230, 55, text="Ready.", font=FONT, fill='#000000')

    def add_utility_button(self, parent, text, command):
        btn = tk.Button(parent, text=text, font=FONT, bg=BUTTON_BG, fg=BUTTON_FG, width=22, command=command, relief=tk.RAISED, bd=2)
        btn.pack(pady=5)

    # --- Placeholder methods for utilities ---
    def download_video(self):
        url = simpledialog.askstring("Download Video", "Enter YouTube video URL:")
        if url:
            messagebox.showinfo("Download", f"Would download video from:\n{url}\n(Integrate your script here)")

    def get_video_info(self):
        url = simpledialog.askstring("Get Video Info", "Enter YouTube video URL:")
        if url:
            messagebox.showinfo("Video Info", f"Would fetch info for:\n{url}\n(Integrate your script here)")

    def manage_playlists(self):
        messagebox.showinfo("Playlists", "Would open playlist management tool.\n(Integrate your script here)")

    def batch_process(self):
        messagebox.showinfo("Batch Process", "Would open batch processing tool.\n(Integrate your script here)")

if __name__ == "__main__":
    app = YouTubeUtilityUI()
    app.mainloop()
