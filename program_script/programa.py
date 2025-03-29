import os
import shutil
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser


# ------------------------- Funções de Ação -------------------------'
def organizar(caminho):
    lista_das_respostas = []
    resposta_tratada = ''


    # Verificar se o caminho existe:
    if not os.path.exists(caminho):
        lista_das_respostas.append('Voce esqueceu de digitar o caminho da pasta.')
        for i in lista_das_respostas:
            resposta_tratada += i + '\n'
        texto_resposta_organizador['text'] = resposta_tratada
        return
    try:
        read_path = os.listdir(caminho)
    except Exception as e:
        lista_das_respostas.append(f'Erro ao listar arquivos: {e}\n')
        for i in lista_das_respostas:
            resposta_tratada += i + '\n'
        texto_resposta_organizador['text'] = resposta_tratada
        return

    # Verificar o caminho e listar o caminho / Verificar se a pasta está vazia:
    arquivos = []
    for item in read_path:
        try:
            way = os.path.join(caminho, item)
            if os.path.isfile(way):
                arquivos.append(item)
        except Exception as e:
            lista_das_respostas.append(f'❌ Erro ao verificar arquivo: {item} - {e}\n')
            for i in lista_das_respostas:
                resposta_tratada += i + '\n'
            texto_resposta_organizador['text'] = resposta_tratada

    if not arquivos:
        lista_das_respostas.append('⚠ Não há arquivos a serem movidos! Verifique a pasta.')
        for i in lista_das_respostas:
            resposta_tratada += i + '\n'
        texto_resposta_organizador['text'] = resposta_tratada
        return

    # Criar pasta, caso nao exista:
    meses = {
        'Janeiro': 'Jan',
        'Fevereiro': 'Fev',
        'Março': 'Mar',
        'Abril': 'Abr',
        'Maio': 'Mai',
        'Junho': 'Jun',
        'Julho': 'Jul',
        'Agosto': 'Ago',
        'Setembro': 'Set',
        'Outubro': 'Out',
        'Novembro': 'Nov',
        'Dezembro': 'Dez'
    }

    for k, v in meses.items():
        try:
            cam = os.path.join(caminho, k)
            if not os.path.exists(cam):
                os.mkdir(cam)
                lista_das_respostas.append(f'✔ Pasta de {v} criada com sucesso!')
                for i in lista_das_respostas:
                    if i not in resposta_tratada:
                        resposta_tratada += i + '\n'
                texto_resposta_organizador['text'] = resposta_tratada
            else:
                lista_das_respostas.append(f'Pasta de {v} já existe. Não precisei criar!')
                for i in lista_das_respostas:
                    if i not in resposta_tratada:
                        resposta_tratada += i + '\n'
                texto_resposta_organizador['text'] = resposta_tratada
        except Exception as e:
            lista_das_respostas.append(f'❌ Erro ao criar a pasta {v}: {e}\n')
            for i in lista_das_respostas:
                if i not in resposta_tratada:
                    resposta_tratada += i + '\n'
            texto_resposta_organizador['text'] = resposta_tratada


    # Mover arquivos para a pasta:
    for k, v in meses.items():
        contador = 0
        try:
            for item in arquivos:
                nome_arquivo = item.upper()
                if v.upper() in nome_arquivo:
                    origem = os.path.join(caminho, item)
                    destino = os.path.join(caminho, k)
                    shutil.move(origem, destino)
                    contador += 1
        except Exception as e:
            lista_das_respostas.append(f'❌ Erro ao mover a pasta de {k}: {e}')
            for i in lista_das_respostas:
                if i not in resposta_tratada:
                    resposta_tratada += i + '\n'
            texto_resposta_organizador['text'] = resposta_tratada
        if contador > 0:
            lista_das_respostas.append(f'✅ {contador} arquivos de {k} movidos com SUCESSO!')
            for i in lista_das_respostas:
                if i not in resposta_tratada:
                    resposta_tratada += i + '\n'
            texto_resposta_organizador['text'] = resposta_tratada

def main_organizar():
    caminho_organizar = e1.get()
    organizar(caminho_organizar)
    messagebox.showinfo('Resultado...', texto_resposta_organizador['text'])


def separar(pasta_origem):
    lista_das_respostas = []
    resposta_tratada = ''
            

    # Verifica se a pasta de origem existe
    if not os.path.exists(pasta_origem):
        lista_das_respostas.append(f"Você esqueceu de digitar o caminho da pasta.")
        for i in lista_das_respostas:
            resposta_tratada += i + '\n'
        texto_resposta_separador['text'] = resposta_tratada
        return

    # Lista todos os arquivos na pasta de origem
    arquivos = [f for f in os.listdir(pasta_origem) if os.path.isfile(os.path.join(pasta_origem, f))]

    if not arquivos:
        lista_das_respostas.append(f"Não há arquivos para organizar na pasta.")
        for i in lista_das_respostas:
            resposta_tratada += i + '\n'
        texto_resposta_separador['text'] = resposta_tratada
        return

    # Contador de grupos
    grupo_num = 1
    arquivos_por_grupo = 100

    # Criação dos grupos e movimentação dos arquivos
    for i in range(0, len(arquivos), arquivos_por_grupo):
        # Cria o nome da nova pasta para o grupo
        pasta_destino = os.path.join(pasta_origem, f'grupo_{grupo_num}')

        # Cria a nova pasta, se não existir
        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)

        # Arquivos que pertencem ao grupo atual
        grupo_arquivos = arquivos[i:i + arquivos_por_grupo]

        # Move os arquivos para a nova pasta
        for arquivo in grupo_arquivos:
            caminho_origem = os.path.join(pasta_origem, arquivo)
            caminho_destino = os.path.join(pasta_destino, arquivo)
            shutil.move(caminho_origem, caminho_destino)
        lista_das_respostas.append(f"Pasta {grupo_num}: {len(grupo_arquivos)} arquivos movidos!" + '\n')
        for i in lista_das_respostas:
            resposta_tratada += i + '\n'
        texto_resposta_separador['text'] = resposta_tratada

        # Incrementa o número do grupo
        grupo_num += 1

def main_serarar():
    caminho_a_separar = e2.get()
    separar(caminho_a_separar)
    messagebox.showinfo("Resultado...", texto_resposta_separador['text'])

def abrir_link(event):
    webbrowser.open("https://linktr.ee/renancalazans?fbclid=PAZXh0bgNhZW0CMTEAAaYOELlAc2qtsGpVLBnynUjQXLvMbcGCoVD9-GSxgM8nK2o5gE5VXTD-XgM_aem_mUfEcZYLJlADYNPNMl6MbQ")




# -------------------------- Funções de Mensagens: EM CONSTRUCAO --------------------------
def mensagem_em_construcao():
    messagebox.showinfo('AGUARDE', 'Funcionalidade em CONSTRUÇÃO...')



# ---------------------------- Funções de Telas ----------------------------
def tela_organizador():
    frame_separador.place_forget()
    frame_conversor.place_forget()
    frame_about.place_forget()
    frame_organizador.place(x=170, y=3, width=550, height=350)

def tela_separador():
    frame_organizador.place_forget()
    frame_conversor.place_forget()
    frame_about.place_forget()
    frame_separador.place(x=170, y=3, width=550, height=350)

def tela_conversor():
    frame_organizador.place_forget()
    frame_separador.place_forget()
    frame_about.place_forget()
    frame_conversor.place(x=170, y=3, width=550, height=350)

def tela_home():
    frame_organizador.place_forget()
    frame_separador.place_forget()
    frame_conversor.place_forget()
    frame_about.place_forget()

def tela_about():
    frame_organizador.place_forget()
    frame_separador.place_forget()
    frame_conversor.place_forget()
    frame_about.place(x=165, y=3, width=580, height=350)




# ---------------------------- Tela Principal ----------------------------
tela_inicial = Tk()
tela_inicial.title('Tratador de Arquivos - CALAZANS')
tela_inicial.geometry('800x450')
icon = PhotoImage(file="images\\rc2.png")
tela_inicial.iconphoto(True, icon)
tela_inicial.configure(
    pady=50,
    padx=15,
    bg="#2d3839",  # muda o cor de fundo
    cursor="arrow",  # muda o cursor
    relief="raised",  # estilo da borda
    bd=5)  # largura da borda)


# BOTOES LATERAIS
icon_home = Image.open('images\\home1.png')
icon_home_resized = icon_home.resize((32, 32), Image.Resampling.LANCZOS)
icon_home_tk = ImageTk.PhotoImage(icon_home_resized)
home_button = Button(tela_inicial, image=icon_home_tk, command=tela_home)
home_button.place(x=65, y=10, width=50, height=50)
home_button.configure(bg="#6e9987", relief="raised", bd=3)

organizador_button = Button(tela_inicial, text="ORGANIZADOR", command=tela_organizador, bg='#6e9987', fg='#27191c', font=('Fixedsys', 10, 'bold'))
organizador_button.place(x=15, y=100, width=150, height=30)
organizador_button.configure(relief="raised", bd=5)

separador_button = Button(tela_inicial, text='SEPARADOR', command=tela_separador, bg='#6e9987', fg='#27191c', font=('Fixedsys', 10, 'bold'))
separador_button.place(x=15, y=180, width=150, height=30)
separador_button.configure(relief="raised", bd=5)

conversor_button = Button(tela_inicial, text='CONVERSOR XML', command=tela_conversor, bg='#6e9987', fg='#27191c', font=('Fixedsys', 10, 'bold'))
conversor_button.place(x=15, y=260, width=150, height=30)
conversor_button.configure(relief="raised", bd=5)

about_button = Button(tela_inicial, text='about', command=tela_about, bg='#27191c', fg='#e0e4ce', font=('Fixedsys', 6, 'italic'))
about_button.place(x=50, y=320, width=80, height=25)
about_button.configure(relief="groove", bd=3)

# TEXTOS DE INSTRUÇÕES
instruction0 = Label(tela_inicial,
    text='              TELA INICIAL              ',
    bg="#2d3839",
    font=('Courier', 18, 'bold', 'underline'),
    fg='#e0e4ce')
instruction0.place(x=218, y=3, width=500, height=30)

instruction1 = Label(tela_inicial,
                    text='Instruções de uso do programa:',
                    bg="#2d3839",
                    font=('Corbel Light', 13),
                    fg='#e0e4ce')
instruction1.place(x=343, y=42, width=250, height=30)

instruction2 = Label(tela_inicial,
                    text='''
Analisa os nomes dos arquivos e os move automaticamente para pastas organizadas por mês, com base na informação contida no nome do arquivo. 
Ex: Arquivos com "JAN" serão movidos para a pasta "Janeiro", arquivos com "FEV" para "Fevereiro", e assim por diante.


Separa arquivos em pastas agrupando-os de 100 em 100.
Ex: Se na pasta selecionada houver 365 arquivos, serão criadas 4 pastas: três com 100 arquivos e uma com 65 arquivos.


Converte XML em PDF: localiza os arquivos XML e gera automaticamente suas versões em PDF, agilizando o processo de visualização e impressão das notas.''',
                    bg="#2d3839",
                    font=('Arabic Transparent', 10),
                    wraplength=500,
                    justify="left",
                    fg='#e0e4ce')
instruction2.place(x=200, y=76, width=525, height=220)


# SETAS
imagem_seta1 = PhotoImage(file='images\\seta.png')
label_imagem1 = Label(tela_inicial, image=imagem_seta1, bg='#2d3839')
label_imagem1.place(x=176, y=100, width=28, height=28)

imagem_seta2 = PhotoImage(file='images\\seta.png')
label_imagem2 = Label(tela_inicial, image=imagem_seta2, bg='#2d3839')
label_imagem2.place(x=176, y=180, width=28, height=28)

imagem_seta3 = PhotoImage(file='images\\seta.png')
label_imagem3 = Label(tela_inicial, image=imagem_seta3, bg='#2d3839')
label_imagem3.place(x=176, y=260, width=28, height=28)


# ---------------------------- Tela ORGANIZADOR ----------------------------
frame_organizador = Frame(tela_inicial, bg='#2d3839')
# # TEXTTOS DE INSTRUÇÕES
instruction0 = Label(frame_organizador,
    text='ORGANIZADOR DE ARQUIVOS',
    bg="#2d3839",
    font=('Courier', 18, 'bold', 'underline'),
    fg='#e0e4ce')
instruction0.place(x=140, y=3, width=320, height=30)

instruction1 = Label(frame_organizador,
                     text='Digite um caminho para organizar os arquivos por mês:',
                     bg="#2d3839",
                     font=('Corbel Light', 13),
                     fg='#e0e4ce')
instruction1.place(x=105, y=80, width=380, height=20)

instruction2 = Label(frame_organizador,
                     text='''
    COMO USAR?
    Deseja organizar os arquivos por mês? 
    Este programa cria pastas de Janeiro a Dezembro e move
    os arquivos para a pasta correspondente com base no mês.

    EXEMPLO:
    Arquivos com "JAN" serão movidos para a pasta "Janeiro".''',
                     bg="#2d3839",
                     font=('Courier', 8),
                     fg='#e0e4ce')
instruction2.place(x=47, y=175, width=450, height=110)

# ENTRADA DE DADOS
e1 = Entry(frame_organizador, width=50)
e1.place(x=67, y=105, width=450, height=20)

# BOTAO ORGANIZAR
button = Button(frame_organizador,
                text="ORGANIZAR",
                command=main_organizar,
                font=("Fixedsys", 12, 'bold'),
                bg='#6e9987')
button.place(x=238, y=135, width=100, height=25)

# RESPOSTA AO USUARIO
texto_resposta_organizador = Label(tela_inicial, text='')




# ---------------------------- Tela SEPARADOR ----------------------------
frame_separador = Frame(tela_inicial, bg='#2d3839')
# # TEXTTOS DE INSTRUÇÕES
instruction0 = Label(frame_separador,
    text='SEPARADOR DE ARQUIVOS',
    bg="#2d3839",
    font=('Courier', 18, 'bold', 'underline'),
    fg='#e0e4ce')
instruction0.place(x=140, y=3, width=320, height=30)

instruction1 = Label(frame_separador,
                     text='Digite um caminho para separar os arquivos de 100 em 100:',
                     bg="#2d3839",
                     font=('Corbel Light', 13),
                     fg='#e0e4ce')
instruction1.place(x=105, y=80, width=400, height=20)

instruction2 = Label(frame_separador,
                     text='''
    COMO USAR?
    Deseja separar arquivos de 100 em 100? 
    Este programa cria grupos de pastas de 100 arquivos.

    EXEMPLO:
    Se na pasta houver 365 arquivos será criado 4 pastas.
    Três pastas com 100 arquivos e uma pasta com 65 arquivos.''',
                     bg="#2d3839",
                     font=('Courier', 8),
                     fg='#e0e4ce')
instruction2.place(x=47, y=175, width=450, height=110)

# ENTRADA DE DADOS
e2 = Entry(frame_separador, width=50)
e2.place(x=67, y=105, width=450, height=20)

# BOTAO SEPARAR
button = Button(frame_separador,
                text="SEPARAR",
                command=main_serarar,
                font=("Fixedsys", 12, 'bold'),
                bg='#6e9987')
button.place(x=238, y=135, width=100, height=25)

# RESPOSTA AO USUARIO
texto_resposta_separador = Label(tela_inicial, text='')




# ---------------------------- Tela CONVERSOR ----------------------------
frame_conversor = Frame(tela_inicial, bg='#2d3839')
#TEXTTOS DE INSTRUÇÕES
instruction0 = Label(frame_conversor,
    text='CONVERSOR DE XML EM PDF',
    bg="#2d3839",
    font=('Courier', 18, 'bold', 'underline'),
    fg='#e0e4ce')
instruction0.place(x=140, y=3, width=320, height=30)

instruction1 = Label(frame_conversor,
                     text="Digite um caminho onde estão os xml's:",
                     bg="#2d3839",
                     font=('Corbel Light', 13),
                     fg='#e0e4ce')
instruction1.place(x=105, y=80, width=380, height=20)

instruction2 = Label(frame_conversor,
                     text='''
    COMO USAR?
    Deseja comverter XML em Danfe? 
    Este programa converte arquivos XML em PDF.

    EXEMPLO:
    Um arquivos com extensão XML será convertido para PDF.''',
                     bg="#2d3839",
                     font=('Courier', 8),
                     fg='#e0e4ce')
instruction2.place(x=47, y=175, width=450, height=110)

# ENTRADA DE DADOS
e3 = Entry(frame_conversor, width=50)
e3.place(x=67, y=105, width=450, height=20)

# BOTAO CONVERTER
button = Button(frame_conversor,
                text="CONVERTER",
                command=mensagem_em_construcao,
                font=("Fixedsys", 12, 'bold'),
                bg='#6e9987')
button.place(x=238, y=135, width=100, height=25)




# ---------------------------- Tela ABOUT ----------------------------
frame_about = Frame(tela_inicial, bg='#2d3839')
#TEXTOS DE INSTRUÇÕES
imagem_eu = Image.open('images\\eu.png')
imagem_redimensionada = imagem_eu.resize((200, 262))
imagem_convertida = ImageTk.PhotoImage(imagem_redimensionada)
label_imagem = Label(frame_about, image=imagem_convertida, bg='#2d3839')
label_imagem.place(x=350, y=20, width=200, height=320)

nome = Label(frame_about,
    text='    Renan Calazans',
    bg="#2d3839",
    font=('Courier', 18, 'bold', 'underline'),
    fg='#e0e4ce')
nome.place(x=175, y=3, width=500, height=30)

texto_sobre_mim = Label(frame_about,
                     text='''
                     • Contador & Programador •

                     Unindo tecnologia e contabilidade
                     para soluções eficientes

                     
                     Entre em contato:
                     📞 (81) 98549-0395
                     📧 renancalazans98@gmail.com''',
                     bg="#2d3839",
                     font=('Corbel Light', 15),
                     fg='#e0e4ce',
                     justify='center')
texto_sobre_mim.place(x=-35, y=5, width=350, height=285)

clique_aqui_saibamais = Label(frame_about,
                     text='Clique aqui para saber mais',
                     bg="#2d3839",
                     font=('Corbel Light', 11, 'bold'),
                     fg='#6e9987',
                     justify='center',
                     cursor="hand2")
clique_aqui_saibamais.place(x=85, y=290, width=200, height=18)
clique_aqui_saibamais.bind("<Button-1>", abrir_link)



# ---------------------------- Rodapé e Loop ----------------------------
# ASSINATURA
signature = Label(tela_inicial, text='Renan Calazans ©', font=("Monotype Corsiva", 13), bg="#2d3839", fg='#ddeadd')
signature.place(relx=0.93, rely=1.132, anchor='s')

# RODAR A TELA
tela_inicial.mainloop()
