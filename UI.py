import tkinter as tk
import os
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from ultralytics import YOLO

MODEL_PATH = '/Users/alioguzhan/Desktop/Python/BitirmeProjesi/ikinci calisma/best.pt'
model = YOLO(MODEL_PATH)

def predict(image_path):
    results = model(image_path)

    if results[0].probs is not None:
        class_id = int(results[0].probs.top1)
        class_name = model.model.names[class_id]
        print("YOLO tahmini:", class_name)
        if class_name == "hastalikli":
            return "Hastalıklı"
        else:
            return "Sağlıklı"
    else:
        return "Tahmin yapılamadı"

class ALLApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ALL Detection")
        self.root.geometry("800x600")

        self.image_path = None

        # Background
        bg_image = Image.open('/Users/alioguzhan/Desktop/Python/BitirmeProjesi/ikinci calisma/ChatGPT Image 10 Nis 2025 14_57_28.png').resize((800, 600))
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        self.bg_label = tk.Label(root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # load icons
        self.gallery_icon = Image.open('/Users/alioguzhan/Desktop/Python/BitirmeProjesi/ikinci calisma/gallery.png').resize((60, 60))
        self.gallery_photo = ImageTk.PhotoImage(self.gallery_icon)

        self.bacteria_icon = Image.open('/Users/alioguzhan/Desktop/Python/BitirmeProjesi/ikinci calisma/bacteria.png').resize((60, 60))
        self.bacteria_photo = ImageTk.PhotoImage(self.bacteria_icon)

        self.load_image_btn = tk.Button(root, image=self.gallery_photo, command=self.select_image,
                                        bg="#ffffff", borderwidth=0, highlightthickness=0, cursor="hand2")
        self.load_image_btn.place(x=350, y=300, width=60, height=60)

        self.image_label = tk.Label(root, bg="#ffffff", borderwidth=2, relief="solid")
        self.image_label.place(x=530, y=280, width=200, height=200)

        self.predict_btn = tk.Button(root, image=self.bacteria_photo, command=self.predict_result,
                                     bg="#ffffff", borderwidth=0, highlightthickness=0, cursor="hand2")
        self.predict_btn.place(x=420, y=300, width=60, height=60)

        self.result_label = tk.Label(root, text="", font=("Helvetica", 20, "bold"),
                                     bg="#ffffff", fg="black")
        self.result_label.place(x=580, y=285)

    def select_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if file_path:
            self.image_path = file_path
            img = Image.open(file_path)
            img.thumbnail((200, 200))
            img_tk = ImageTk.PhotoImage(img)
            self.image_label.configure(image=img_tk)
            self.image_label.image = img_tk

    def predict_result(self):
        if not self.image_path:
            messagebox.showwarning("Eksik Bilgi", "Lütfen önce bir görsel seçin.")
            return
        result = predict(self.image_path)
        self.result_label.config(text=result, fg="green" if result == "Sağlıklı" else "red")


# Uygulama başlat
root = tk.Tk()
app = ALLApp(root)
root.mainloop()