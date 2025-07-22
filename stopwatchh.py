import tkinter as tk

# Global variables
counter = 0
running = False

# Convert seconds to hh:mm:ss
def convert_time(sec):
    hrs = sec // 3600
    mins = (sec % 3600) // 60
    secs = sec % 60
    return f"{hrs:02}:{mins:02}:{secs:02}"

# Update time every second
def update_time():
    global counter
    if running:
        time_label.config(text=convert_time(counter))
        counter += 1
        root.after(10, update_time)

# Start button action
def start():
    global running
    if not running:
        running = True
        update_time()

# Pause button action
def pause():
    global running
    running = False

# Reset button action
def reset():
    global counter, running
    running = False
    counter = 0
    time_label.config(text="00:00:00")

# GUI setup
root = tk.Tk()
root.title("Stopwatch App")
root.geometry("300x200")
root.resizable(False, False)

time_label = tk.Label(root, text="00:00:00", font=("bold", 40))
time_label.pack(pady=20)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack()

tk.Button(button_frame, text="Start", command=start, width=8, bg="red", fg="black").grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Pause", command=pause, width=8, bg="blue", fg="black").grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Reset", command=reset, width=8, bg="yellow", fg="black").grid(row=0, column=2, padx=5)

root.mainloop()
