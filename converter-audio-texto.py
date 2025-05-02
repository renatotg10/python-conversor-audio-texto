import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox, ttk
import whisper
import threading
import os
import time

# Lista de modelos disponíveis
modelos_disponiveis = ["tiny", "base", "small", "medium", "large"]

modelo_carregado = None  # Modelo carregado na memória

def formatar_tempo(segundos):
    return time.strftime('%H:%M:%S', time.gmtime(segundos))

def selecionar_arquivo():
    caminho_arquivo = filedialog.askopenfilename(
        title="Selecione o arquivo de áudio",
        filetypes=[("Arquivos de Áudio", "*.mp3 *.wav *.m4a *.flac")]
    )
    if caminho_arquivo:
        entrada_arquivo.set(caminho_arquivo)

def carregar_modelo(nome_modelo):
    global modelo_carregado
    try:
        saida_texto.delete("1.0", tk.END)
        saida_texto.insert(tk.END, f"Carregando modelo '{nome_modelo}', aguarde...\n")
        modelo_carregado = whisper.load_model(nome_modelo)
        saida_texto.insert(tk.END, f"Modelo '{nome_modelo}' carregado com sucesso!\n\n")
    except Exception as e:
        saida_texto.insert(tk.END, f"Erro ao carregar modelo: {str(e)}\n")

def transcrever_audio():
    caminho = entrada_arquivo.get()
    nome_modelo = combobox_modelo.get()

    if not caminho:
        messagebox.showwarning("Atenção", "Por favor, selecione um arquivo de áudio.")
        return

    if not modelo_carregado:
        carregar_modelo(nome_modelo)

    saida_texto.delete("1.0", tk.END)
    saida_texto.insert(tk.END, "Transcrevendo, aguarde...\n")

    def executar_transcricao():
        try:
            resultado = modelo_carregado.transcribe(caminho, language="pt")

            nome_base = os.path.splitext(os.path.basename(caminho))[0]
            pasta = os.path.dirname(caminho)
            caminho_txt = os.path.join(pasta, f"{nome_base}_transcricao.txt")

            with open(caminho_txt, "w", encoding="utf-8") as f:
                saida_texto.delete("1.0", tk.END)
                for segmento in resultado["segments"]:
                    inicio = formatar_tempo(segmento["start"])
                    fim = formatar_tempo(segmento["end"])
                    texto = segmento["text"].strip()
                    linha = f"[{inicio} - {fim}] {texto}"
                    saida_texto.insert(tk.END, linha + "\n")
                    f.write(linha + "\n")

            messagebox.showinfo("Transcrição concluída", f"Transcrição salva em:\n{caminho_txt}")

        except Exception as e:
            saida_texto.delete("1.0", tk.END)
            saida_texto.insert(tk.END, f"Erro: {str(e)}")

    threading.Thread(target=executar_transcricao).start()

# Interface gráfica
janela = tk.Tk()
janela.title("Conversor de Áudio para Texto - Whisper")
janela.geometry("640x450")

entrada_arquivo = tk.StringVar()

tk.Label(janela, text="Arquivo de Áudio:").pack(pady=5)
tk.Entry(janela, textvariable=entrada_arquivo, width=60).pack(padx=10)
tk.Button(janela, text="Selecionar Arquivo", command=selecionar_arquivo).pack(pady=5)

tk.Label(janela, text="Modelo Whisper:").pack(pady=5)
combobox_modelo = ttk.Combobox(janela, values=modelos_disponiveis, state="readonly")
combobox_modelo.set("small")  # modelo padrão
combobox_modelo.pack(pady=5)

tk.Button(janela, text="Transcrever Áudio", command=transcrever_audio).pack(pady=10)

saida_texto = scrolledtext.ScrolledText(janela, wrap=tk.WORD, width=75, height=15)
saida_texto.pack(padx=10, pady=5)

janela.mainloop()
