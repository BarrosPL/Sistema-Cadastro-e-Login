import PySimpleGUI as sg


#Lista de Usuario e senhas.
usuarioc=''
senhac = ''


#Janelas e Layout.

def janela_cadastro():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Insira o seu nome:')],
        [sg.Input(key='nome')],
        [sg.Text('Insira a sua Senha:')],
        [sg.Input(key='senha')],
        [sg.Button('Cadastrar'), sg.Button('Finalizar')],
    ]
    return sg.Window('Cadastro', layout= layout, finalize=True)

def janela_login():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Nome:')],
        [sg.Input(key='nome')],
        [sg.Text('Senha:')],
        [sg.Input(key='senha')],
        [sg.Button('Login')],
    ]
    return sg.Window('Login', layout= layout, finalize=True)

#Janela Inicial.

janelac, janelal = janela_cadastro(), None

#Verificando Eventos.
while True:
    window, event, values = sg.read_all_windows()
    #Quando fechar a janela.
    if window == janelac and event == sg.WIN_CLOSED:
        break
    #Ir a Janela de Login.
    if window ==janelac and event == 'Finalizar':
        janelal = janela_login()
        janelac.hide()
    if window ==janelac and event == 'Cadastrar':
        usuarioc = values['nome']
        senhac = values['senha']
        sg.popup('Cadastro Realizado Com Sucesso, Clique em Finalizar para Prosseguir ao Login!!')  
    if window == janelal and event == sg.WIN_CLOSED:
        break
    if window == janelal and event == 'Login':
        usuario = values['nome']
        senha = values['senha']
        if usuario == usuarioc and senha == senhac:
             sg.popup('Login Realizado com Sucesso!') 
             janelal.hide()
        else:
            sg.popup('Usuario ou Senha Incorreto!')      




    




        