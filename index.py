import streamlit as st
import numpy as np
from pathlib import Path

pasta_calculadora = Path(__file__).parent.parent / 'calculadora'

with st.sidebar:
    st.title('Calculadora de CAGR')
    st.header('Cálculo de CAGR')

    st.write('CAGR: Compound Annual Growth Rate (Taxa de Crescimento Anual Composta)')

    st.write('Essa taxa mostra o quanto os valores cresceram (ou diminuíram), de maneira composta, no período analisado.')

    st.write('De maneira bem simples, a taxa calculada é “composta” pois leva em conta não somente a variação entre o valor inicial e final, mas também os valores intermediários. É o mesmo princípio do “juro sobre juros”.')

st.title('Calculadora CAGR (Taxa de Crescimento Anual Composta)')

# Criando um input para inserir valores das variáveis.
periodo = st.number_input(label='Número de Períodos', min_value=0)
valor_inical = st.number_input(label='Valor Incial', min_value=0.00, format='%0.2f')
valor_final = st.number_input('Valor Final: ', min_value=0.00, format='%0.2f')

# Inicializando a variável cagr_arred
cagr_arred = None

if st.button('Calcular'):
    if valor_inical > 0 and periodo > 0:
        cagr = (((valor_final / valor_inical) ** (1 / periodo)) - 1) * 100
        cagr_arred = round(cagr, 2)
    else:
        st.error("Valor inicial e período devem ser maiores que zero.")


if cagr_arred is not None:
    st.code(f"O resultado é {cagr_arred}%")
else:
    st.code("Digite os valores e clique em calcular.")