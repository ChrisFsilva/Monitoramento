<h1 align="center">Monitoramento de Dispositivos em Rede</h1>			
<br>
<h4 align="center"> 🚀 Concluído 🚀 </h4>

Tabela de conteúdos
=================
<!--ts-->
   * [Sobre o projeto](#-sobre-o-projeto)
   * [Layout](#-layout)
   * [Como executar o projeto](#-como-executar-o-projeto)
     * [Pré-requisitos](#pré-requisitos)
     * [Funcionalidades](#funcionalidades)
   * [Tecnologias](#-tecnologias)
   * [Autor](#-autor)
   * [Licença](#-licença)
<!--te-->

## 💻 Sobre o projeto

**Descrição**:  
Este projeto realiza o monitoramento de dispositivos conectados à rede local por meio de testes de conectividade *ping*.  
O sistema é composto por dois componentes principais:

- A extensão **pingInfo**, instalada no sistema Windows, que realiza os pings em uma lista de dispositivos e gera um banco de dados `.csv` contendo:
  - status do último teste,
  - número total de falhas e sucessos,
  - data e hora da última ocorrência.

- Um **painel web em JavaScript**, que lê o banco de dados `.csv` e exibe os resultados com cores indicativas:
  - **verde** para dispositivos com ping bem-sucedido,
  - **vermelho** para falhas,
  - além de contadores e informações temporais.

---

## 🎨 Layout

<p align="center" style="display: flex; align-items: flex-start; justify-content: center;">
<img alt="Painel de Monitoramento By Christopher Silva" title="#monitoramento-ping" src="https://i.pinimg.com/564x/61/c2/35/61c235fdc3cb24cf9f931ef30e2d2cc2.jpg" style="width:500px";/>
</p>

Componentes Principais:

pingInfo (extensão Windows): executa pings e gera banco de dados .csv.

devices.csv: banco de dados com resultados de testes de conectividade.

dashboard.html: painel web que exibe os resultados dos pings.

app.js: script JavaScript que interpreta e exibe as informações do CSV.

start servercors.bat: inicia um servidor local para permitir leitura de arquivos locais via navegador.

markdown
Copiar
Editar

---

## 🚀 Como executar o projeto

### Pré-requisitos

- Sistema operacional: **Windows**
- Extensão **pingInfo** instalada e configurada
- Navegador moderno (Chrome, Edge, Firefox)
- Permissões para executar comandos `ping`
- Servidor local (start servercors.bat)

### Instalação:

1. Instale e configure o **pingInfo** no Windows.
2. Configure a lista de dispositivos no pingInfo para gerar o `devices.csv`.
3. Execute o servidor local com permissões de CORS:
   ```bash
   start servercors.bat
Acesse o dashboard.html via navegador (localhost).

Importante: o uso do servidor é necessário para que o navegador consiga acessar o .csv via fetch().

Funcionalidades
markdown
Copiar
Editar
Monitoramento por Ping:
  Executa testes de conectividade com dispositivos de rede definidos.

Geração de Relatórios:
  Cria um arquivo CSV com os seguintes dados:
    - Status atual
    - Número total de sucessos e falhas
    - Data e hora da última resposta válida ou falha

Visualização no Navegador:
  Um painel visual indica:
    - Status com cores (verde/vermelho)
    - Histórico por dispositivo
    - Data/hora da última atualização

Servidor Local:
  Necessário para leitura do CSV no navegador (via fetch e CORS).
🛠 Tecnologias
As seguintes tecnologias foram usadas na construção do projeto:

pingInfo (extensão para Windows) – ferramenta de monitoramento por ping

JavaScript – lógica do painel e leitura do CSV

HTML5 e CSS3 – estrutura e visual do dashboard

Servidor CORS Local – usado para carregar arquivos CSV no navegador

🦸🏻‍♂️ Autor
<sub><b>Christopher Silva</b></sub>



📝 Licença
Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes.
MIT
