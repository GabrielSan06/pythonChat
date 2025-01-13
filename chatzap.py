# RESUMO DO QUE TERÁ NO SITE
# Título: ChatZap
# Botão de iniciar chat
    # popup
    # Título: "Bem vindo ao ChatZap"
    # Campo de texto -> "Escreva seu nome no chat"
    # Botão: "entrar no chat"
        # Sumir com o título "ChatZap"
        # Sumir com o botão "Iniciar chat"
        # Fechar o popoup
        # Carregar o chat
            # Mensagens que já foram enviadas
            # Campo: "Digite sua mensagem"
            # Botão de enviar

# Importação do flet
import flet as ft

# Criando função principal do aplicativo/site
def main(pagina):
    #Criação de todas as funcionalidades

    #Criação do elemento
    titulo = ft.Text("ChatZap")


    titulo_janela = ft.Text("Bem vindo ao ChatZap")
    campo_nome_usuario = ft.TextField(label= "Escreva seu nome no chat") # TextField = Campo de texto (onde será inserido algo)
    
    chat = ft.Column()

    # Enviando a menssagem para todos os usuários no túnel de mensagem
    def enviar_mensagem_tunel(mensagem):
        texto_chat = ft.Text(mensagem)
        chat.controls.append(texto_chat) # append = adicionar no final da lista
        pagina.update()

    # criando o túnel de mensagem
    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        # Armazenando a entrada do usuario em variáveis
        texto_mensagem = campo_mensagem.value
        nome_usuario = campo_nome_usuario.value
        mensagem = (f"{nome_usuario}: {texto_mensagem}")
        pagina.pubsub.send.all(mensagem) # Enviando mensagem para todos os usuários
        campo_mensagem.value = ""
        texto_entrar_chat = ft.Text(f"{campo_nome_usuario} entrou no chat")
        chat.controls.append(texto_entrar_chat) 
        pagina.update()

    campo_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)
    botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    
    # Colocando os elementos em uma linha após o envio de uma mensagem 
    linha_mensagem = ft.Row([campo_mensagem, botao_enviar_mensagem])

    def entrar_chat(evento): 
        pagina.remove(titulo)
        pagina.remove(botao_iniciar)
        janela.open = False
        pagina.add(chat)
        pagina.add(linha_mensagem)
        pagina.add(botao_enviar_mensagem)
        pagina.update()

    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)
    # PopUP
    janela = ft.AlertDialog(title=titulo_janela, content=campo_nome_usuario, actions=[botao_entrar])


    def iniciar_chat(evento):
        # Carregando a janela dentro da página e habilitando-a 
        pagina.dialog = janela
        janela.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=iniciar_chat)


    # Adicição do elemento a página
    pagina.add(titulo)
    pagina.add(botao_iniciar)

# Rodando o aplicativo/site
ft.app(main, view=ft.WEB_BROWSER)