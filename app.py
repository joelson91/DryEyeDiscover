import streamlit as st

# Título do aplicativo
st.title("Dry Eye Discover")
st.write("Este aplicativo consulta a tabela 'participantes' do banco de dados PostgresSQL.")

# Conectar ao banco de dados usando st.connection
try:
    conn = st.connection("postgres", type="sql")

    # Executar a query e armazenar o resultado em um DataFrame
    df = conn.query('SELECT genero as "Gênero", COUNT(*) as "Contagem" FROM participante GROUP BY genero;')

    # Exibir o DataFrame
    st.write("### Dados da Tabela 'participantes':")
    st.dataframe(df)

    # Exibir gráfico de barras
    st.bar_chart(df, x='Gênero', y='Contagem')

except Exception as e:
    st.error(f"Erro ao conectar ou consultar o banco de dados: {e}")
