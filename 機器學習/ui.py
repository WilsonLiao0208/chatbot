import tkinter as tk
import torch
from torchvision.transforms.functional import pil_to_tensor
from torchvision import transforms
from PIL import Image, ImageDraw

class PaintApp:
    def __init__(self, master, model):
        self.master = master
        master.title("手寫數字辨識")
        self.model = model
        # self.normalize = transforms.Normalize((0.1307,), (0.3081,))
        
        self.number = tk.StringVar()
        self.number.set('?') 
        self.number_label = tk.Label(master, textvariable=self.number, font=('Arial',40,'bold'),)
        self.number_label.pack()
        
        self.canvas = tk.Canvas(master, width=500, height=500, bg="black")
        self.canvas.pack()
        
        self.img = Image.new("L", (500, 500), "black")
        self.draw = ImageDraw.Draw(self.img)

        self.canvas.bind("<B1-Motion>", self.paint)

        self.save_button = tk.Button(master, text="辨識數字", command=self.identify)
        self.save_button.pack()
        
        self.clear_button = tk.Button(master, text="清空畫布", command=self.clear)
        self.clear_button.pack()
    
    def paint(self, event):
        x1, y1 = (event.x - 10), (event.y - 10)
        x2, y2 = (event.x + 10), (event.y + 10)
        self.canvas.create_oval(x1, y1, x2, y2, fill="white",outline='white')
        self.draw.ellipse([x1, y1, x2, y2], fill="white")

    def identify(self):
        img = self.img.resize((28,28))
        img = pil_to_tensor(img)
        img = img.to(torch.float32)/255.0
        # img = self.normalize(img)
        img = torch.reshape(img, (1,1,28,28))
        result = model(img)
        result = result.argmax(dim=1).item()
        self.number.set(str(result))
        self.master.update_idletasks()
        
    def clear(self):
        self.canvas.delete("all")
        self.draw.rectangle((0, 0, 500, 500), fill="black")

model = torch.jit.load('model.pt')
model.eval()
root = tk.Tk()
app = PaintApp(root, model)
root.mainloop()