import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("App")
        self.root.geometry("800x600")
        self._criar_widgets()

    def _criar_widgets(self):
        # seus widgets aqui
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
