import qrcode
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import os
import re
from datetime import datetime

# Pasta onde os QR Codes serão salvos
PASTA_QR = "qrcodes"
os.makedirs(PASTA_QR, exist_ok=True)

# Validação básica de URL ou texto
def entrada_valida(texto):
    if not texto.strip():
        return False
    # Regex simples para detectar URLs (opcional)
    url_regex = r"^(https?://)?[\w\-]+(\.[\w\-]+)+[/#?]?.*$"
    return re.match(url_regex, texto) or len(texto) > 3

def gerar_qr():
    texto = entrada.get()
    if not entrada_valida(texto):
        messagebox.showwarning("Entrada inválida", "Digite um texto ou link válido.")
        return

    try:
        # Nome único baseado em timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nome_arquivo = f"{PASTA_QR}/qrcode_{timestamp}.png"

        # Geração do QR Code
        qr = qrcode.make(texto)
        qr.save(nome_arquivo)

        # Exibe na interface
        img = Image.open(nome_arquivo)
        img = img.resize((200, 200))
        img_tk = ImageTk.PhotoImage(img)
        qr_label.config(image=img_tk)
        qr_label.image = img_tk

        messagebox.showinfo("Sucesso", f"QR Code salvo como:\n{nome_arquivo}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao gerar o QR Code:\n{str(e)}")

# Interface gráfica
janela = tk.Tk()
janela.title("Gerador de QR Code Seguro")
janela.geometry("320x420")

entrada = tk.Entry(janela, width=40)
entrada.pack(pady=20)

btn_gerar = tk.Button(janela, text="Gerar QR Code", command=gerar_qr)
btn_gerar.pack()

qr_label = tk.Label(janela)
qr_label.pack(pady=20)

janela.mainloop()