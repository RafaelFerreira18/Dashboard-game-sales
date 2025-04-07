import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Dashboard de Vendas de Video Games 🎮")

df = pd.read_csv("vgsales.csv")
df.fillna(df["Year"].mean(), inplace=True)
df.dropna(subset=["Publisher"], inplace=True)
df["Year"] = df["Year"].astype(int)

#Criando a sidebar
if 'page' not in st.session_state:
    st.session_state.page = "Página Principal"

with st.sidebar.expander("Navegar"):
    if st.button("Página Principal"):
        st.session_state.page = "Página Principal"
    if st.button("Página Secundária"):
        st.session_state.page = "Página Secundária"

if st.session_state.page == "Página Principal":
    #Inicializando as Abas

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Vendas Globais por Ano", "Vendas Globais por Gênero", "Top 10 Empresas", "Melhores de Cada Gênero", "Vendas por Região", "Vendas por Plataforma"])

    #Grafico 1

    with tab1:
        generos = df["Genre"].unique()
        genero_selecionado = st.selectbox("", sorted(generos))
        df_filtrado = df[df["Genre"] == genero_selecionado]
        sales_by_year = df_filtrado.groupby("Year")["Global_Sales"].sum().reset_index()
        fig = px.bar(sales_by_year, x="Year", y="Global_Sales")

        st.subheader(f"Vendas Globais de {genero_selecionado} por Ano")
        st.plotly_chart(fig)

    #Grafico 2

    genre_sales = df.groupby("Genre")["Global_Sales"].sum().reset_index().sort_values("Global_Sales", ascending=False)
    fig2 = px.bar(genre_sales, x="Global_Sales", y="Genre", orientation="h")
    fig2.update_layout(yaxis={'categoryorder': 'total ascending', 'title': 'Gênero'}, xaxis_title='Vendas Globais')

    with tab2:
        st.subheader("Participação dos Gêneros nas Vendas Globais")
        st.plotly_chart(fig2)

    #Grafico 3

    top_10_publishers = df.groupby('Publisher').sum().sort_values('Global_Sales', ascending=False).head(10)
    top10Fig = px.bar(top_10_publishers, x=top_10_publishers['Global_Sales'], y=top_10_publishers.index, orientation="h")
    top10Fig.update_layout(yaxis={'categoryorder': 'total ascending', 'title': 'Empresa'}, xaxis_title='Vendas Globais')

    with tab3:
        st.subheader("Top 10 Empresas de Jogos por Vendas Globais")
        st.plotly_chart(top10Fig)

    #Grafico 4

    best_games = df.loc[df.groupby('Genre')['Global_Sales'].idxmax()]
    best_games = best_games[['Name', 'Genre', 'Global_Sales']]
    best_games = best_games.sort_values('Global_Sales', ascending=False)
    best_games_fig = px.bar(best_games, x='Global_Sales', y='Name', color='Genre', orientation='h')
    best_games_fig.update_layout(yaxis={'categoryorder': 'total ascending', 'title': 'Jogo'}, xaxis_title='Vendas Globais')

    with tab4:
        st.subheader("Os melhores jogos de cada gênero")
        st.plotly_chart(best_games_fig)

    #Grafico 5

    region_sales = df.groupby("Genre")[["NA_Sales", "EU_Sales", "JP_Sales"]].sum().reset_index()
    region_sales = region_sales.melt(id_vars="Genre", var_name="Region", value_name="Sales")
    region_sales_fig = px.bar(region_sales, x="Sales", y="Genre", color="Region")
    region_sales_fig.update_layout(yaxis={'categoryorder': 'total ascending', 'title': 'Gênero'}, xaxis_title='Vendas')

    with tab5:
        st.subheader("Distribuição de Vendas por Região")
        st.plotly_chart(region_sales_fig)

    #Grafico 6

    platform_sales = df.groupby("Platform")["Global_Sales"].sum().reset_index()
    platform_sales = platform_sales.sort_values("Global_Sales", ascending=False)
    platform_sales_fig = px.bar(platform_sales.head(10), x="Global_Sales", y="Platform", orientation="h")
    platform_sales_fig.update_layout(yaxis={'categoryorder': 'total ascending', 'title': 'Plataforma'}, xaxis_title='Vendas Globais')

    with tab6:
        st.subheader("Distribuição de Vendas por Plataforma")
        st.plotly_chart(platform_sales_fig)

elif st.session_state.page == "Página Secundária":

    #Filtragem por ano selecionado
    anos = df["Year"].unique()

    st.subheader("Escolha Um Ano Para Analise")
    anoSelecionado = st.selectbox("", sorted(anos))
    ano_Filtrado = df[df["Year"] == anoSelecionado]

    #Grafico 1

    graf1 = px.bar(ano_Filtrado, x="Platform", y="Global_Sales", color="Platform")
    st.subheader(f"Vendas Globais por Plataforma em {anoSelecionado}")
    st.plotly_chart(graf1, use_container_width=True)
    #Grafico 2

    graf2 = px.scatter(ano_Filtrado, x="NA_Sales", y="EU_Sales", size="Global_Sales", color="Genre", hover_data=["Name"])
    st.subheader(f"Comparação de Vendas (NA x EU) por Gênero em {anoSelecionado}")
    st.plotly_chart(graf2, use_container_width=True)

    #Grafico 3

    top_jogos = ano_Filtrado.sort_values("Global_Sales", ascending=False).head(5)
    graf3 = px.bar(top_jogos, x="Global_Sales", y="Name", orientation="h", color="Name", labels={"Global_Sales": "Vendas Globais", "Name": "Nome do Jogo"})
    st.subheader(f"Os 5 melhores jogos de {anoSelecionado}")
    st.plotly_chart(graf3, use_container_width=True)
