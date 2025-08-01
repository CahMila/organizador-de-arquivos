# Organizador de Arquivos por Extensão 📂

![Organizador de Arquivos](caminho/para/sua-imagem.png)

Este projeto em Python organiza automaticamente arquivos de uma pasta selecionada pelo usuário, movendo-os para subpastas de acordo com suas extensões (como imagens, planilhas e PDFs).

## 💡 Funcionalidade

O programa:

- Abre uma janela para que o usuário escolha uma pasta;
- Lê todos os arquivos presentes na pasta;
- Verifica a extensão de cada arquivo;
- Move os arquivos para subpastas com base em suas extensões:
  - `.jpg`, `.png` → pasta `imagens`
  - `.xlsx`, `.csv` → pasta `planilhas`
  - `.pdf` → pasta `pdfs`

## 🛠️ Tecnologias Utilizadas

- Python 3
- Biblioteca `os` (padrão do Python)
- Biblioteca `tkinter` (interface gráfica para seleção da pasta)

## ▶️ Como Usar

1. Certifique-se de ter o Python instalado em seu computador.
2. Clone este repositório ou baixe os arquivos.
3. Execute o script Python:

```bash
python organizador.py
