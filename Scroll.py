import tkinter as tk

def on_canvas_configure(event):
    # Update the scrollable region to encompass the entire canvas
    canvas.configure(scrollregion=canvas.bbox("all"))

def on_mousewheel(event):
    # Scroll the canvas vertically when using the mouse wheel
    canvas.yview_scroll(-1 * int(event.delta / 120), "units")

root = tk.Tk()
root.title("Scrollable Canvas")

# Create a scrollbar
scrollbar = tk.Scrollbar(root, orient="vertical")

# Create a canvas with the scrollbar attached to it
canvas = tk.Canvas(root, yscrollcommand=scrollbar.set)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Bind the scrollbar to the canvas
scrollbar.config(command=canvas.yview)

# Bind the mouse wheel event to scroll the canvas
canvas.bind_all("<MouseWheel>", on_mousewheel)

# Add some content to the canvas
frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

for i in range(30):
    label = tk.Label(frame, text=f"Label {i}")
    label.pack()

# Configure the canvas to update the scrollable region when resized
canvas.bind("<Configure>", on_canvas_configure)

root.mainloop()
