# BIBLIOTECAS UTILIZADAS
import PyPDF2
import os

# CORRELACIONANDO A VARIAVEL QUE VAI CONTER A FERRAMENTA DE MESCLAGEM DE PDF
merger = PyPDF2.PdfMerger()

# ESPECIFICAÇÃO E ORGANIZAÇÃO DA PASTA ONDE OS PDF's A SEREM MESCLADOS FICARÃO
lista_arquivos = os.listdir("arquivos_em_pdf")
lista_arquivos.sort()

# LÓGICA BÁSICA DA MESCLAÇÃO DOS ARQUIVOS
for pdf in lista_arquivos:
    if ".pdf" in pdf:
        merger.append(f"arquivos_em_pdf/{pdf}")

# CRIAÇÃO DO ARQUIVO FINAL
merger.write("PDF Final.pdf")