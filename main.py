# Importa o módulo 'os' para interagir com o sistema de arquivos (listar, mover, criar pastas, etc.)
import os

# Importa apenas a função 'askdirectory' da biblioteca tkinter.filedialog
# Ela permite abrir uma janela para o usuário escolher uma pasta
from tkinter.filedialog import askdirectory  

# Abre uma janela para o usuário selecionar uma pasta e armazena o caminho escolhido na variável 'caminho'
caminho = askdirectory(title="Selecione uma pasta: ")  

# Lista todos os arquivos e pastas presentes no diretório selecionado
lista_arquivos = os.listdir(caminho)

# Exibe na tela a lista de arquivos encontrados no diretório escolhido
print(lista_arquivos)

# Dicionário que define os tipos de arquivos e suas extensões associadas
# A chave representa o nome da pasta de destino
# O valor é uma lista com as extensões de arquivos que pertencem àquela categoria
locais = {
    "imagens": [".png", ".jpg"],
    "planilhas": [".xlsx", ".csv"],
    "pdfs": [".pdf"],
}


# Percorre cada arquivo presente na lista de arquivos
for arquivo in lista_arquivos:

    # Separa o nome e a extensão do arquivo (ex: "foto.jpg" → nome = "foto", extensao = ".jpg")
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")

    # Percorre cada pasta e suas extensões associadas no dicionário 'locais'
    for pasta in locais:

        # Verifica se a extensão do arquivo atual está na lista de extensões da pasta
        if extensao in locais[pasta]:

            # Verifica se a pasta de destino ainda não existe, e se não existir, cria
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")

            # Move o arquivo para dentro da pasta correspondente com base na extensão
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")
