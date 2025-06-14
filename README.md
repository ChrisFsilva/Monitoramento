<h1 align="center">Monitoramento de Dispositivos em Rede</h1>			
<br>
<h4 align="center"> 🚀 Funcional / Em melhorias 🚀 </h4>

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
O sistema é composto por três componentes principais:

#### Coleta de Dados com o PingInfoView
```bash
O programa PingInfoView (ferramenta do Windows) é configurado para monitorar dispositivos através de ping contínuo.
Ele usa o arquivo i'ps.txt para saber quais IPs e descrições pingar.
Os resultados são exportados automaticamente para um arquivo .csv (ping_data.csv), contendo status, IP, nome do host, contagem de falhas/sucessos, entre outros.
```
#### Servidor Local (Node.js)
```bash
Um servidor Node.js simples, com express e cors, roda localmente na porta 8000.
Ele serve o painel HTML (index.html) e permite acesso ao arquivo ping_data.csv.
```
#### Painel Web Dinâmico
```bash
O painel web lê o ping_data.csv a cada 2 segundos usando PapaParse.
Para cada IP, cria um painel colorido:
Verde para ping bem-sucedido - Vermelho para ping com falha
Mostra informações como IP, nome do host, descrição, falhas/sucessos e últimas datas.
```
---

## 🎨 Layout

<p align="center" style="display: flex; align-items: flex-start; justify-content: center;">
<img alt="Painel de Monitoramento By Christopher Silva" title="#monitoramento-ping" src="https://i.pinimg.com/564x/61/c2/35/61c235fdc3cb24cf9f931ef30e2d2cc2.jpg" style="width:500px";/>
</p>

Componentes Principais:
```bash
  pingInfo (extensão Windows): executa pings e gera banco de dados .csv.
  
  devices.csv: banco de dados com resultados de testes de conectividade.
  
  dashboard.html: painel web que exibe os resultados dos pings.
  
  app.js: script JavaScript que interpreta e exibe as informações do CSV.
  
  start servercors.bat: inicia um servidor local para permitir leitura de arquivos locais via navegador.
```

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
```
#### Funcionalidades
```bash

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

```
## 🛠 Tecnologias
As seguintes tecnologias foram usadas na construção do projeto:

- **[pingInfo (extensão para Windows) – ferramenta de monitoramento por ping](https://pinginfoview.com/)**
- **[JavaScript](https://www.javascript.com/)** 
- **[Servidor CORS Local – usado para carregar arquivos CSV no navegador]**

## 🦸🏻‍♂️ Autor

 <br>
  <sub><b><p>Christopher Silva</p></b></sub></a>
 <br />

[![Linkedin Badge](https://img.shields.io/badge/-Christopher%20Silva-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/chris-f-silva//)](https://www.linkedin.com/in/chris-f-silva/) 
[![Gmail Badge](https://img.shields.io/badge/-chrisspfc.silva@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:daniel.rodrigues.soarees@gmail.com)](mailto:chrisspfc.silva@gmail.com)

---

## 📝 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes. [MIT](./LICENSE)

Feito por: Christopher Silva
