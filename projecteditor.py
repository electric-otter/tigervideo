import tkinter as tk
from tkinter import filedialog, messagebox
import cv2
import numpy as np
import json
import os

class TVIDEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("TVID Video Editor")
        
        self.video_data = []  # Holds video frame data
        self.current_frame_index = 0
        self.effects = {"grayscale": self.apply_grayscale, "invert": self.apply_invert, "blur": self.apply_blur}
        
        self.canvas = tk.Canvas(root, width=640, height=480, bg="black")
        self.canvas.pack()
        
        tk.Button(root, text="Open .tvid", command=self.open_tvid).pack()
        tk.Button(root, text="Save .tvid", command=self.save_tvid).pack()
        tk.Button(root, text="Apply Effect", command=self.apply_effect).pack()
        tk.Button(root, text="Export Video", command=self.export_video).pack()
        
        self.effect_var = tk.StringVar(value="grayscale")
        self.effect_menu = tk.OptionMenu(root, self.effect_var, *self.effects.keys())
        self.effect_menu.pack()
    
    def open_tvid(self):
        file_path = filedialog.askopenfilename(filetypes=[("TVID Files", "*.tvid")])
        if file_path:
            with open(file_path, "r") as f:
                self.video_data = json.load(f)
            self.show_frame()
    
    def save_tvid(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".tvid", filetypes=[("TVID Files", "*.tvid")])
        if file_path:
            with open(file_path, "w") as f:
                json.dump(self.video_data, f)
            messagebox.showinfo("Saved", "Video saved successfully")
    
    def apply_effect(self):
        if self.video_data:
            effect = self.effect_var.get()
            if effect in self.effects:
                self.video_data = [self.effects[effect](frame) for frame in self.video_data]
                self.show_frame()
    
    def export_video(self):
        if self.video_data:
            file_path = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 Video", "*.mp4")])
            if file_path:
                height, width = 480, 640
                out = cv2.VideoWriter(file_path, cv2.VideoWriter_fourcc(*'mp4v'), 24, (width, height))
                for frame in self.video_data:
                    img = np.array(frame, dtype=np.uint8)
                    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR) if len(img.shape) == 2 else img
                    out.write(img)
                out.release()
                messagebox.showinfo("Exported", "Video exported successfully")
    
    def apply_grayscale(self, frame):
        return cv2.cvtColor(np.array(frame, dtype=np.uint8), cv2.COLOR_BGR2GRAY).tolist()
    
    def apply_invert(self, frame):
        return (255 - np.array(frame, dtype=np.uint8)).tolist()
    
    def apply_blur(self, frame):
        return cv2.GaussianBlur(np.array(frame, dtype=np.uint8), (5, 5), 0).tolist()
    
    def show_frame(self):
        if self.video_data:
            frame = np.array(self.video_data[self.current_frame_index], dtype=np.uint8)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) if len(frame.shape) == 3 else frame
            img = tk.PhotoImage(width=640, height=480, data=frame.tobytes())
            self.canvas.create_image(0, 0, anchor=tk.NW, image=img)
            self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = TVIDEditor(root)
    root.mainloop()
