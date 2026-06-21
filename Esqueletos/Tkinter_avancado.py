import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("App")
        self.root.geometry("800x600")
        self._criar_widgets()

    def _criar_widgets(self):

        # ===== LABEL =====
        self.label = tk.Label(self.root, text="Info")
        self.label.pack()

        # ===== INPUT =====
        self.input = tk.Entry(self.root)
        self.input.pack()

        # ===== BOTÃO =====
        self.botao = tk.Button(self.root, text="Info", command=self._acao)
        self.botao.pack()

    def _acao(self):
        # sua lógica aqui
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
