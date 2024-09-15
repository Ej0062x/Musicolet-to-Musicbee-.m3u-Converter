import os
import tkinter as tk
from tkinter import filedialog, messagebox

class M3UProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("M3U File Processor")

        # Create UI elements
        self.label = tk.Label(root, text="Select a directory to process M3U files:")
        self.label.pack(pady=10)

        self.browse_button = tk.Button(root, text="Browse", command=self.browse_directory)
        self.browse_button.pack(pady=5)

        self.status_text = tk.Text(root, height=15, width=80)
        self.status_text.pack(pady=10)

    def browse_directory(self):
        # Open a directory selection dialog
        directory = filedialog.askdirectory()
        if directory:
            self.process_directory(directory)

    def process_directory(self, directory):
        try:
            for filename in os.listdir(directory):
                if filename.lower().endswith('.m3u'):
                    file_path = os.path.join(directory, filename)
                    self.process_file(file_path)
            messagebox.showinfo("Success", "Processing complete.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def process_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()

            # Remove lines containing "#EXT" and replace text
            processed_lines = [
                line.replace("ENTERMUSICOLETPATHHERE", r"ENTERWINDOWSPATHHERE")
                for line in lines if not line.startswith("#EXT")
            ]

            # Create new file path with "-Win" appended
            base, ext = os.path.splitext(file_path)
            new_file_path = f"{base}-Win{ext}"

            with open(new_file_path, 'w') as file:
                file.writelines(processed_lines)

            self.status_text.insert(tk.END, f"Processed file: {os.path.basename(file_path)}\n")
            self.status_text.yview(tk.END)
        except Exception as e:
            self.status_text.insert(tk.END, f"Error processing file {os.path.basename(file_path)}: {str(e)}\n")
            self.status_text.yview(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = M3UProcessorApp(root)
    root.mainloop()
