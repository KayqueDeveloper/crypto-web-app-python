
# Função para gerar a chave repetida com o tamanho do texto
def gerar_chave(texto, chave):
    chave_repetida = []
    chave_tamanho = len(chave)
    
    for i in range(len(texto)):
        chave_repetida.append(chave[i % chave_tamanho])
    
    return ''.join(chave_repetida)

#Explicação:

# Objetivo: A função gerar_chave cria uma chave estendida que tem o mesmo comprimento do texto original, repetindo a palavra-chave várias vezes.

#  - Chave_repetida = []: Cria uma lista vazia que será preenchida com as letras da chave repetidas.

#  - Len(chave): Obtém o tamanho da chave.

#  - For i in range(len(texto)): Esse loop itera sobre cada caractere do texto original.

#  - Chave[i % chave_tamanho]: O operador % (módulo) encontra o "resto" da divisão, permitindo que a chave "gire" e se repita.

#  - ''.join(chave_repetida): Concatena a lista chave_repetida em uma única string.



# Função de criptografia com Cifra de Vigenère
def cifra_vigenere(texto, chave):
    chave_ajustada = gerar_chave(texto, chave)
    criptografado = []
    
    for i in range(len(texto)):
        letra_texto = texto[i]
        letra_chave = chave_ajustada[i]
        
        # Apenas criptografar letras
        if letra_texto.isupper():
            valor = (ord(letra_texto) + ord(letra_chave.upper()) - 2 * ord('A')) % 26
            criptografado.append(chr(valor + ord('A')))
        elif letra_texto.islower():
            valor = (ord(letra_texto) + ord(letra_chave.lower()) - 2 * ord('a')) % 26
            criptografado.append(chr(valor + ord('a')))
        else:
            criptografado.append(letra_texto)  # Manter espaços e caracteres especiais
    
    return ''.join(criptografado)

# Explicação:

# Objetivo: Esta função implementa a Cifra de Vigenère, que criptografa o texto com base em uma palavra-chave.

# - chave_ajustada = gerar_chave(texto, chave): Usa a função anterior para gerar uma chave repetida que tenha o mesmo tamanho do texto.

#  -criptografado = []: Lista vazia para armazenar as letras criptografadas.

#  - for i in range(len(texto)): Itera por cada letra do texto.

#  - letra_texto = texto[i]: Pega cada letra do texto.

#  - letra_chave = chave_ajustada[i]: Pega a letra correspondente da chave repetida.

#   Se a letra for maiúscula:
#    - ord(letra_texto): Converte a letra em seu código ASCII (número que representa cada caractere).
#    - ord(letra_chave.upper()): Converte a letra da chave para código ASCII (se for minúscula, converte para maiúscula).
#    - Cálculo valor: O valor resultante é o deslocamento das letras dentro do alfabeto. Fazemos uma subtração dupla de ord('A') (valor ASCII da letra 'A') para alinhar os valores no intervalo de 0 a 25.
#    - chr(valor + ord('A')): Converte o número resultante de volta em um caractere.
#  - Se a letra for minúscula, o processo é similar, mas usando ord('a') para alinhar as letras minúsculas.
#  - Se não for uma letra (exemplo: espaços ou pontuação), apenas adicionamos diretamente à lista.
#  - return ''.join(criptografado): Junta a lista de letras criptografadas em uma string final.


# Função de descriptografia com Cifra de Vigenère
def decifra_vigenere(texto, chave):
    chave_ajustada = gerar_chave(texto, chave)
    descriptografado = []
    
    for i in range(len(texto)):
        letra_texto = texto[i]
        letra_chave = chave_ajustada[i]
        
        # Apenas descriptografar letras
        if letra_texto.isupper():
            valor = (ord(letra_texto) - ord(letra_chave.upper()) + 26) % 26
            descriptografado.append(chr(valor + ord('A')))
        elif letra_texto.islower():
            valor = (ord(letra_texto) - ord(letra_chave.lower()) + 26) % 26
            descriptografado.append(chr(valor + ord('a')))
        else:
            descriptografado.append(letra_texto)  # Manter espaços e caracteres especiais
    
    return ''.join(descriptografado)

# Explicação:

# A função de descriptografia funciona de maneira semelhante à de criptografia, mas ao invés de somar os valores ASCII, fazemos a subtração da letra da chave.
# + 26: Isso garante que o valor sempre será positivo, mesmo quando a subtração der um número negativo (evita underflow).


# Função para embaralhar blocos de um texto
def permutar_blocos(texto, tamanho_bloco):
    texto_permutado = []
    
    for i in range(0, len(texto), tamanho_bloco):
        bloco = texto[i:i + tamanho_bloco]
        texto_permutado.append(bloco[::-1])  # Inverte a ordem do bloco
    
    return ''.join(texto_permutado)

# Explicação:

# Objetivo: A função permutar_blocos pega o texto cifrado e o "embaralha" invertendo grupos de letras (blocos) de tamanho fixo.
#  - for i in range(0, len(texto), tamanho_bloco): Este loop percorre o texto em intervalos (blocos) definidos por tamanho_bloco.
#  - bloco = texto[i:i + tamanho_bloco]: Extrai um bloco do texto.
#  - bloco[::-1]: Inverte o bloco usando a sintaxe de slicing do Python (que lê a string de trás para frente).
#  - return ''.join(texto_permutado): Junta todos os blocos invertidos em uma única string.



# Função para reverter a permutação de blocos
def reverter_blocos(texto, tamanho_bloco):
    texto_revertido = []
    
    for i in range(0, len(texto), tamanho_bloco):
        bloco = texto[i:i + tamanho_bloco]
        texto_revertido.append(bloco[::-1])  # Desfaz a inversão do bloco
    
    return ''.join(texto_revertido)

# Explicação:

# A função reverte o processo de permutação, ou seja, ela "desembaralha" os blocos do texto voltando à ordem original.
# O processo é exatamente o mesmo que na permutação, apenas aplicado novamente.


# Teste
texto = "Segredo Importante"
chave = "chave"
print(f"Texto original: {texto}")
criptografado = cifra_vigenere(texto, chave)
print(f"Texto criptografado: {criptografado}")
print(f"Texto descriptografado: {decifra_vigenere(criptografado, chave)}")

# Teste com permutação de blocos
tamanho_bloco = 3
criptografado_permutado = permutar_blocos(criptografado, tamanho_bloco)
print(f"Texto criptografado com permutação de blocos: {criptografado_permutado}")

descriptografado_permutado = reverter_blocos(criptografado_permutado, tamanho_bloco)
print(f"Texto revertido da permutação de blocos: {descriptografado_permutado}")
print(f"Texto final descriptografado: {decifra_vigenere(descriptografado_permutado, chave)}")

