
# ChatZap

**Chatzap** é um projeto de chat em tempo real desenvolvido em Python utilizando o framework [Flet](https://flet.dev/). Ele permite que os usuários interajam em um ambiente simples e intuitivo, com funcionalidades básicas de envio de mensagens e visualização em tempo real.

---

## 🚀 Funcionalidades

- **Início simples:** Um botão para iniciar o chat, com um popup para entrada do nome do usuário.
- **Interface intuitiva:**
  - Campo de texto para o nome do usuário.
  - Botão de entrada para carregar o chat.
- **Mensagens em tempo real:**
  - Visualização das mensagens enviadas por todos os usuários.
  - Campo de texto para digitar mensagens.
  - Botão para enviar mensagens.
- **Experiência interativa:**
  - Nome do usuário incluído em todas as mensagens enviadas.
  - Atualização em tempo real do chat para todos os participantes.

---

## 📋 Pré-requisitos

Antes de começar, você precisará ter o Python instalado e o pacote `flet` configurado em sua máquina.

### Instalação do Flet
Execute o seguinte comando para instalar o Flet:

```
pip install flet
```

## ⚙️ Como executar o projeto
1. Clone o repositório ou copie o código para um arquivo Python (chatzap.py).
2. Certifique-se de que o Flet está instalado em seu ambiente.
3. Execute o aplicativo com o comando:
```
python chatzap.py
```
4. O navegador será aberto automaticamente, exibindo a interface do chat.

## 🖥️ Interface do Usuário

### Tela Inicial
- Exibe o título **ChatZap**.
- Um botão **Iniciar Chat** para começar.

### Popup de Boas-Vindas
- Apresenta a mensagem **"Bem-vindo ao ChatZap"**.
- Um campo para digitar o nome do usuário.
- Botão **Entrar no Chat**.

### Tela do Chat
- Exibe mensagens enviadas por outros participantes.
- Campo para digitar mensagens.
- Botão **Enviar** para compartilhar mensagens.

## 🛠️ Estrutura do Código

### Principais Componentes
1. **Título:** Exibe o nome do aplicativo.
2. **Popup:** Coleta o nome do usuário antes de entrar no chat.
3. **Túnel de Mensagens:** Sistema de publicação e assinatura para envio de mensagens entre usuários.
4. **Campo de Mensagem e Botão:** Interface para o envio de mensagens.
5. **Chat:** Área onde as mensagens são exibidas em tempo real.

## 📜 Fluxo de Execução
1. O usuário clica em **Iniciar Chat**.
2. Um popup é exibido solicitando o nome do usuário.
3. Após digitar o nome e clicar em **Entrar no Chat**, o popup fecha, e o chat é carregado.
4. O usuário pode visualizar mensagens anteriores, digitar novas mensagens e enviá-las.
5. Todas as mensagens são transmitidas em tempo real para todos os participantes do chat.

## 📚 Tecnologias Utilizadas
- **Python:** Linguagem principal.
- **Flet:** Framework para criar interfaces gráficas em Python.

