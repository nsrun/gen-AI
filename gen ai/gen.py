import torch
from diffusers import StableDiffusionPipeline
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
##### A futuristic city at sunset
# 1. Load the Model (this may take a few seconds)
model_id = "CompVis/stable-diffusion-v1-4"
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Loading Gen AI model on {device}...")
pipe = StableDiffusionPipeline.from_pretrained(model_id)
pipe = pipe.to(device)

def show_main_app():
    # Main Generation Window
    main_window = Tk()
    main_window.title("Gen AI -NGT Studio")
    main_window.geometry("700x600")
    main_window.configure(bg="#f0f0f0")

    style = ttk.Style()
    style.configure("TButton", font=("Arial", 10, "bold"), padding=10)
    style.configure("TLabel", background="#f0f0f0", font=("Arial", 11))

    # Header
    ttk.Label(main_window, text="GEN AI - Image NGT Studio", font=("Arial", 20, "bold")).pack(pady=20)

    # Prompt Area
    ttk.Label(main_window, text="Enter your prompt:").pack()
    prompt_entry = ttk.Entry(main_window, width=60, font=("Arial", 12))
    prompt_entry.pack(pady=10)
    prompt_entry.insert(0, "A futuristic city at sunset")

    status_label = ttk.Label(main_window, text="Ready", foreground="blue")
    status_label.pack()

    image_label = ttk.Label(main_window)
    image_label.pack(pady=20)

    def generate_image():
        prompt = prompt_entry.get()
        if not prompt:
            status_label.config(text="Please enter a prompt!", foreground="red")
            return
        
        status_label.config(text="Generating image... please wait", foreground="orange")
        main_window.update()

        try:
            image = pipe(prompt, num_inference_steps=50).images[0]
            
            # Show preview
            display_image = image.resize((500, 500))
            img_tk = ImageTk.PhotoImage(display_image)
            image_label.config(image=img_tk)
            image_label.image = img_tk
            
            # Save
            image.save("generatedimage.png")
            status_label.config(text="Image generated and saved successfully!", foreground="green")
            open_btn.config(state=NORMAL)
        except Exception as e:
            status_label.config(text=f"Error: {str(e)}", foreground="red")

    def open_image():
        if os.path.exists("generatedimage.png"):
            os.startfile("generatedimage.png") # Opens in default Windows viewer
        else:
            messagebox.showwarning("Warning", "No image found. Generate one first!")

    # Buttons
    btn_frame = ttk.Frame(main_window)
    btn_frame.pack(pady=10)

    gen_btn = ttk.Button(btn_frame, text="Generate Image", command=generate_image)
    gen_btn.grid(row=0, column=0, padx=10)

    open_btn = ttk.Button(btn_frame, text="Open Result Image", command=open_image)
    open_btn.grid(row=0, column=1, padx=10)

    main_window.mainloop()

# 2. Setup Login Window
login_window = Tk()
login_window.title("Gen AI Authentication")
login_window.geometry("700x600")
login_window.configure(bg="#101820") # Dark Blue Background
login_window.eval('tk::PlaceWindow . center')

# Custom Styles for Dark Theme
style = ttk.Style()
style.theme_use('clam')
style.configure("Dark.TLabel", background="#101820", foreground="white", font=("Arial", 11))
style.configure("Header.TLabel", background="#101820", foreground="#00d2ff", font=("Arial", 20, "bold"))
style.configure("Login.TButton", font=("Arial", 10, "bold"), padding=10, background="#00d2ff")

ttk.Label(login_window, text="Gen AI -NGT Studio", style="Header.TLabel").pack(pady=30)

ttk.Label(login_window, text="Username:", style="Dark.TLabel").pack()
user_entry = ttk.Entry(login_window, font=("Arial", 11))
user_entry.pack(pady=5)
user_entry.insert(0, "admin")

ttk.Label(login_window, text="Password:", style="Dark.TLabel").pack()
pass_entry = ttk.Entry(login_window, show="*", font=("Arial", 11))
pass_entry.pack(pady=5)
pass_entry.insert(0, "1234")

def try_login():
    if user_entry.get() == "admin" and pass_entry.get() == "1234":
        login_window.destroy()
        show_main_app()
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password")

ttk.Button(login_window, text="LOGIN SECURELY", command=try_login, style="Login.TButton").pack(pady=30)

login_window.mainloop()