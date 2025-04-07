# Dashboard de Vendas de Video Games

O objetivo da criação desse Dashboard é apresenta alguns tópicos de vendas relacionado aos jogos lançados entre 1980 a 2020

# Pré-Requisitos

## 1 Editor de Codigo fonte e Python

* É necessario um editor de código fonte (exp: vscode) que tenha suporte para o Python

## 2 Instalações

* pip install streamlit
* pip install pandas
* pip install plotly

## 3 Biblíotecas

* Streamlit
* plotly.express
* pandas

## 4 Permissões

Abra o Powershell (ou outro gerenciador de sistemas) como administrador e permita que ele faça alterações, por meio desse código:

* Set-ExecutionPolicy RemoteSigned

## 5 Acessar Dashboard

Logo apos realizar as instalações e permissões, para acessar o dashboard é necessário colocar esses codigos no terminar:

* cd caminho/até/a/pasta/trab_dashboard (caso ainda não esteja na pasta trab_dashboard no terminal)
* .venv/Scripts/activate (aparecerá (.venv) em verde no terminal)
* streamlit run main.py

# Estrutura do Projeto

A pasta .venv serve para criar um ambiente virtual que contera os scripts para isso e o arquivo main.py é oque possui os codigos
que serão executados para pelos scripts de .venv para mostrar o dashboard

# Topicos Abordados

Alguns topicos apresentados nesse documento são:

* Vendas Globais de Generos de Jogos por Ano
* Participação de Cada Genero de Jogos nas Vendas Globais
* 10 Empresas que Mais Venderam jogos
* Os Melhores Jgos de Cada Gênero
* Distribuição das Vendas por Cada Região
* Distribuição das Vendas por Cada Plataforma
* Vendas Globais por Plataforma em Determinado Ano
* Comparação da Vendas entre NA e EUA por Gênero em Determinado Ano
* Os 5 Melhores Jogos em Determinado Ano

# Funcionalidades

Funcionalidades disponibilizadas para os usuarios:

* Personalização da aparência do dashboard
* Manipulação da visualização dos graficos apresentados (exp: zoom, move e etc)
* Visualização dos dados utilizados para a formação dos graficos
* Barra de navegação entre os graficos
* Filtragem dos gêneros de jogos nas vendas globais por ano
* Sidebar para selecionar diferentes analises
* Filtragem dos dados para um determinado ano

# Guia de Uso

* O dashboard possui uma barra de navegação que é posivel alternar entre os graficos pressionando nos nomes presentes dentro dela
* O grafico de "Vendas Globais por Ano" possui uma caixa logo a baixo da barra de navegação para selecionar o gênero de jogo que deseja analisar
* A esquerda da janela possui uma barra lateral que pode expandir e retrair a partir da seta no canto superior direito da barra
* Dentro da barra lateral possui uma caixa que é possivel alternar entre as paginas do dashboard
* Na pagina secundario possui uma caixa de seleção logo a baixo do titulo para selecionar um ano e filtrar os dados dos graficos

# Contato e Suporte

Gmail:
# paulo24070023@aluno.cesupa.br
# rafael24070092@aluno.cesupa.br
