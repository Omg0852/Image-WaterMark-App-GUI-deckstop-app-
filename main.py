import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont



# Function to add watermark to an image



def add_watermark(image_path, text):
    original = Image.open(image_path).convert("RGBA")  # opening the Image file and store a converted Copy of thr image

    # Make the image editable
    txt = Image.new("RGBA", original.size, (255, 255, 255, 0))
    d = ImageDraw.Draw(txt)

    # Load a font
    font = ImageFont.truetype("arial.ttf", 80)

    # Position the text/WaterMark at right corner at the bottom
    width, height = original.size
    textbbox = d.textbbox((0, 0), text, font=font)
    textwidth, textheight = textbbox[2], textbbox[3]
    x = width - textwidth - 10
    y = height - textheight - 10

    d.text((x, y), text, fill=(255, 0, 0, 128), font=font)

    watermarked = Image.alpha_composite(original, txt)
    return watermarked



def open_image():
    file_path = filedialog.askopenfilename()  # This line opens a dialog box where you can select an image file from your computer. The file path of the selected image is stored in the variable file_path
    if file_path:
        img = Image.open(file_path)
        img.thumbnail((500, 500))
        img = ImageTk.PhotoImage(img)  # Convert the image into a format that Tkinter can display.
        panel.config(image=img)       #  Update the panel widget to display the processed image.
        panel.image = img
        panel.image_path = file_path    # Store the image and its file path in the panel widget for future use.



def add_text_watermark():
    if panel.image_path:
        watermarked = add_watermark(panel.image_path, watermark_text.get()) # This line calls the add_watermark function, passing the image file path and the watermark text entered by the user.
        watermarked.thumbnail((1000, 500))  # This line resizes the watermarked image to a maximum size of 1000x500 pixels, keeping the aspect ratio.
        img = ImageTk.PhotoImage(watermarked)  # Convert the watermarked image into a format that Tkinter can display.
        panel.config(image=img)  # Update the panel widget to show the watermarked image.
        panel.image = img
        watermarked.save("watermarked_image.png")  # This line saves the watermarked image to a file named watermarked_image.png.


def exit_app():
    root.destroy()

# Create the main window


root = tk.Tk()
root.title("Image Watermarking")

# Add widgets
panel = tk.Label(root)
panel.pack()

watermark_text = tk.Entry(root)
watermark_text.pack()

open_button = tk.Button(root, text="Open Image", command=open_image, bg="yellow", fg="black")
open_button.pack()

watermark_button = tk.Button(root, text="Add Watermark", command=add_text_watermark, bg="blue", fg="black")
watermark_button.pack()


# Add the exit button
exit_button = tk.Button(root, text="Exit", command=exit_app, bg="red", fg="white")
exit_button.pack(side=tk.BOTTOM, anchor=tk.E)



# Start the application
root.mainloop()
