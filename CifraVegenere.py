import tkinter as tk
from tkinter import messagebox

def gerar_chave(texto, chave):
    chave_repetida = []
    chave_tamanho = len(chave)
    
    for i in range(len(texto)):
        chave_repetida.append(chave[i % chave_tamanho])
    
    return ''.join(chave_repetida)


def cifra_vigenere(texto, chave):
    chave_ajustada = gerar_chave(texto, chave)
    criptografado = []
    
    for i in range(len(texto)):
        letra_texto = texto[i]
        letra_chave = chave_ajustada[i]
        
        if letra_texto.isupper():
            valor = (ord(letra_texto) + ord(letra_chave.upper()) - 2 * ord('A')) % 26
            criptografado.append(chr(valor + ord('A')))
        elif letra_texto.islower():
            valor = (ord(letra_texto) + ord(letra_chave.lower()) - 2 * ord('a')) % 26
            criptografado.append(chr(valor + ord('a')))
        else:
            criptografado.append(letra_texto)
    
    return ''.join(criptografado)

def decifra_vigenere(texto, chave):
    chave_ajustada = gerar_chave(texto, chave)
    descriptografado = []
    
    for i in range(len(texto)):
        letra_texto = texto[i]
        letra_chave = chave_ajustada[i]
        
        if letra_texto.isupper():
            valor = (ord(letra_texto) - ord(letra_chave.upper()) + 26) % 26
            descriptografado.append(chr(valor + ord('A')))
        elif letra_texto.islower():
            valor = (ord(letra_texto) - ord(letra_chave.lower()) + 26) % 26
            descriptografado.append(chr(valor + ord('a')))
        else:
            descriptografado.append(letra_texto) 
    
    return ''.join(descriptografado)

def permutar_blocos(texto, tamanho_bloco):
    texto_permutado = []
    
    for i in range(0, len(texto), tamanho_bloco):
        bloco = texto[i:i + tamanho_bloco]
        texto_permutado.append(bloco[::-1])
    
    return ''.join(texto_permutado)

def reverter_blocos(texto, tamanho_bloco):
    texto_revertido = []
    
    for i in range(0, len(texto), tamanho_bloco):
        bloco = texto[i:i + tamanho_bloco]
        texto_revertido.append(bloco[::-1])
    
    return ''.join(texto_revertido)

# Função para criptografar o texto
def criptografar():
    texto = entrada_texto.get()
    chave = entrada_chave.get()
    
    if not texto or not chave:
        messagebox.showwarning("Erro", "Por favor, insira o texto e a chave.")
        return
    
    criptografado = cifra_vigenere(texto, chave)
    criptografado_permutado = permutar_blocos(criptografado, 2)
    saida_texto.config(state='normal')
    saida_texto.delete(1.0, tk.END)  # Limpa a saída anterior
    saida_texto.insert(tk.END, criptografado_permutado)
    saida_texto.config(state='disabled')

# Função para descriptografar o texto
def descriptografar():
    texto = entrada_texto.get()
    chave = entrada_chave.get()
    
    if not texto or not chave:
        messagebox.showwarning("Erro", "Por favor, insira o texto e a chave.")
        return
    
    revertido = reverter_blocos(texto, 2)
    descriptografado = decifra_vigenere(revertido, chave)
    saida_texto.config(state='normal')
    saida_texto.delete(1.0, tk.END)  # Limpa a saída anterior
    saida_texto.insert(tk.END, descriptografado)
    saida_texto.config(state='disabled')

# Função para limpar os campos
def limpar():
    entrada_texto.delete(0, tk.END)
    entrada_chave.delete(0, tk.END)
    saida_texto.config(state='normal')
    saida_texto.delete(1.0, tk.END)
    saida_texto.config(state='disabled')

# Criação da janela principal
root = tk.Tk()
root.title("Sistema de Criptografia - Vigenère com Permutação de Blocos")

# Texto original
tk.Label(root, text="Texto:").grid(row=0, column=0)
entrada_texto = tk.Entry(root, width=40)
entrada_texto.grid(row=0, column=1, columnspan=2)

# Chave de criptografia
tk.Label(root, text="Chave:").grid(row=1, column=0)
entrada_chave = tk.Entry(root, width=40)
entrada_chave.grid(row=1, column=1, columnspan=2)

# Botões
botao_criptografar = tk.Button(root, text="Criptografar", command=criptografar)
botao_criptografar.grid(row=3, column=0)

botao_descriptografar = tk.Button(root, text="Descriptografar", command=descriptografar)
botao_descriptografar.grid(row=3, column=1)

botao_limpar = tk.Button(root, text="Limpar", command=limpar)
botao_limpar.grid(row=3, column=2)

# Saída do texto criptografado/descriptografado
tk.Label(root, text="Resultado:").grid(row=4, column=0)
saida_texto = tk.Text(root, height=5, width=40, state='disabled')
saida_texto.grid(row=4, column=1, columnspan=2)

# Iniciar o loop da interface gráfica
root.mainloop()
