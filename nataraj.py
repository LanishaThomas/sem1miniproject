import customtkinter as ctk
from PIL import Image

# Initialize the app
ctk.set_appearance_mode("light")  # Set theme
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.geometry("1024x768")
app.title("Nataraja Statue")

# Header Section
header_frame = ctk.CTkFrame(app, height=70, corner_radius=0)
header_frame.pack(fill="x")

header_label = ctk.CTkLabel(header_frame, text="Nataraja Statue", font=("Helvetica", 24, "bold"))
header_label.pack(side="left", padx=20)

menu_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
menu_frame.pack(side="right", padx=20)

menu_buttons = ["Home", "Products", "About Us", "Testimonial"]
for menu in menu_buttons:
    btn = ctk.CTkButton(menu_frame, text=menu, width=80, height=30, corner_radius=10)
    btn.pack(side="left", padx=5)

# Content Section
content_frame = ctk.CTkFrame(app, fg_color="white", corner_radius=15)
content_frame.pack(fill="both", expand=True, padx=20, pady=20)

content_title = ctk.CTkLabel(content_frame, text="Nataraja Statue", font=("Helvetica", 28, "bold"))
content_title.pack(pady=10)

content_text = (
    "Nataraja statues are sculptures of Shiva as the lord of dance and are symbolic of his roles as the creator, \n"
    "preserver, and destroyer of the universe. The earliest bronze Nataraja sculptures date back to the Pallava period, \n"
    "between the 7th and 9th centuries CE. The Chola dynasty, which ruled from 880–1279, is credited with evolving \n"
    "the present form of the Nataraja statue.\n\n"
    "Symbolism:\n"
    "- Flaming aureole: Symbolizes the circle of the world\n"
    "- Long dreadlocks: Represent the dynamism of his dance\n"
    "- Four arms: Each holding a symbolic object\n"
    "- Damaru (hand drum): Represents the primal sound, or the big bang"
)

content_label = ctk.CTkLabel(content_frame, text=content_text, font=("Helvetica", 14), justify="left", wraplength=600)
content_label.pack(pady=10, side= "left", padx=20)

# Image Section
image_path = "C:/Users/Srushti/OneDrive/Desktop/sem 1 mini project/indiVOuge/nataraj.png"  # Replace with your image path
try:
    image = Image.open(image_path)
    image = image.resize((300, 400))  # Resize to fit the UI
    ctk_image = ctk.CTkImage(light_image=image, dark_image=image, size=(300, 400))

    image_label = ctk.CTkLabel(content_frame, image=ctk_image, text="")
    image_label.pack(side="right", padx=20)
except FileNotFoundError:
    image_label = ctk.CTkLabel(content_frame, text="[Image Placeholder]", text_color="gray", font=("Helvetica", 16))
    image_label.pack(side="right", padx=20)

# Price and Buy Section
price_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
price_frame.pack(pady=20, side="bottom")

price_label = ctk.CTkLabel(price_frame, text="5000 RS", font=("Helvetica", 20, "bold"))
price_label.pack(side="left", padx=10)

buy_button = ctk.CTkButton(price_frame, text="BUY NOW", font=("Helvetica", 16, "bold"), width=150)
buy_button.pack(side="left", padx=10)

# Certified Section
certified_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
certified_frame.pack(pady=10, side="bottom")

certified_label = ctk.CTkLabel(certified_frame, text="Certified", font=("Helvetica", 16, "bold"), text_color="green")
certified_label.pack()

# Run the app
app.mainloop()
