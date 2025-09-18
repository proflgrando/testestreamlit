import streamlit as st

# ==================================================
# PORTFÓLIO DE ALGORITMOS EM PYTHON
# Exemplo de app com dois temas (Streamlit)
# ==================================================

# Configurações da página
st.set_page_config(page_title="Portfólio de Algoritmos", layout="centered")

# Título principal
st.title("📚 Portfólio de Algoritmos")
st.write("Este app demonstra exemplos simples de **Python + Streamlit**.")


# ==================================================
# MENU LATERAL
# ==================================================
menu = st.sidebar.radio(
    "Escolha um tema:",
    ("Decisão e Repetição", "Recursividade")
)


# ==================================================
# TEMA 1 - DECISÃO E REPETIÇÃO
# ==================================================
if menu == "Decisão e Repetição":
    st.header("Tema 1: Decisão e Repetição")

    # Entrada do número para a tabuada
    numero = st.number_input("Digite um número para ver a tabuada:", min_value=1, step=1)

    if st.button("Gerar Tabuada"):
        st.subheader(f"Tabuada do {numero}")
        # Estrutura de repetição (for) para gerar a tabuada
        for i in range(1, 11):
            st.write(f"{numero} x {i} = {numero * i}")

    # Documentação
    with st.expander("📄 Documentação do Tema 1"):
        st.markdown("""
        **Objetivo:** Demonstrar uso de decisão e repetição.  
        - O usuário escolhe um número.  
        - Usamos um `for` para gerar a tabuada de 1 a 10.  
        - Estruturas aplicadas:  
            - **Decisão:** `if st.button(...)` para verificar clique do usuário.  
            - **Repetição:** `for` para construir a tabuada.  
        """)


# ==================================================
# TEMA 2 - RECURSIVIDADE
# ==================================================
elif menu == "Recursividade":
    st.header("Tema 2: Recursividade")

    # Função recursiva para fatorial
    def fatorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * fatorial(n - 1)

    # Entrada de número
    n = st.number_input("Digite um número inteiro:", min_value=0, step=1)

    if st.button("Calcular Fatorial"):
        resultado = fatorial(n)
        st.success(f"O fatorial de {n} é {resultado}")

    # Documentação
    with st.expander("📄 Documentação do Tema 2"):
        st.markdown("""
        **Objetivo:** Implementar e demonstrar um algoritmo recursivo.  
        - O usuário digita um número inteiro.  
        - A função `fatorial()` chama a si mesma até atingir o caso base (`n == 0 ou 1`).  
        - Conceitos aplicados:  
            - **Recursividade** (função chamando ela mesma).  
            - **Decisão** (caso base vs. caso recursivo).  
        """)
