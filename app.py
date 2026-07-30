import streamlit as st
import datetime

# --- CONFIGURAÇÕES FÁCEIS DE EDITAR ---
# Adicione novos itens nestas listas sempre que precisar
SEGURADORAS = [
  "Aliro",
  "Allianz",
  "Azul",
  "Pier",
  "Porto",
  "Sompo",
  "Suhai",
  "Tokio",
  "Yellum",
  "Zurich"
]
TIPOS_SEGURO = ["Auto", "Residencial", "Empresarial", "Vida", "Vida em Grupo", "Equipamento", "Celular"]

st.set_page_config(page_title="Gerador de Mensagens - Financeiro", layout="centered")

st.title("Gerador de Mensagens - WhatsApp")
st.subheader("Setor: Financeiro")

# --- INTERFACE DE ENTRADA ---
nome_cliente = st.text_input("Nome do Cliente", placeholder="Digite apenas o nome (ex: Maria)")

opcoes_mensagens = [
    "Irá vencer",
    "Vence Hoje",
    "Pendente",
    "Venceu ontem",
    "Débito → Boleto",
    "Não autorizado débito no Cartão de Crédito",
    "Cliente não pagou a fatura"
]
mensagem_selecionada = st.selectbox("Selecione o modelo da mensagem:", opcoes_mensagens)

st.divider()

col1, col2 = st.columns(2)

with col1:
    seguradora = st.selectbox("Seguradora", SEGURADORAS)
    tipo_seguro = st.selectbox("Tipo do Seguro", TIPOS_SEGURO)

with col2:
    parcela = st.number_input("Número da Parcela", min_value=1, max_value=120, value=1)
    data_vencimento = st.date_input("Data de Vencimento/Ocorrência", format="DD/MM/YYYY")

data_formatada = data_vencimento.strftime("%d/%m/%Y")

# --- LÓGICA DE GERAÇÃO DAS MENSAGENS ---
mensagem_final = ""

if nome_cliente:
    if mensagem_selecionada == "Irá vencer":
        mensagem_final = f"Olá, {nome_cliente}! Boa tarde\n\nApenas para avisar que a {parcela}ª parcela do seu Seguro {tipo_seguro} {seguradora} vence em {data_formatada}.\n\nSe o pagamento já foi realizado, desconsidere esta mensagem. Caso contrário, segue em anexo o boleto para a efetuação do pagamento.\n\nTenha um ótimo dia!"
        
    elif mensagem_selecionada == "Vence Hoje":
        mensagem_final = f"Olá, {nome_cliente}! Boa tarde\n\nPassando para reforçar que a {parcela}ª parcela do seu Seguro {tipo_seguro} {seguradora} vence hoje, {data_formatada}.\n\nCaso tenha realizado o pagamento, desconsidere a mensagem. Caso contrário, segue em anexo o boleto para a efetuação do pagamento.\n\nQualquer dúvida estamos à disposição!"
        
    elif mensagem_selecionada == "Pendente":
        mensagem_final = f"Olá, {nome_cliente}! Boa tarde\n\nVerificamos que a {parcela}ª parcela do seu Seguro {tipo_seguro} {seguradora} ainda consta como pendente no sistema da seguradora.\n\nLembrando que manter as parcelas em dia é essencial para garantir a continuidade da cobertura do seguro.\n\nQualquer dúvida, estamos à disposição!"
        
    elif mensagem_selecionada == "Venceu ontem":
        mensagem_final = f"Olá, {nome_cliente}! Bom dia\n\nPassando para te avisar que a parcela do seu seguro, com vencimento em {data_formatada}, venceu ontem.\n\nCaso tenha realizado o pagamento, desconsidere a mensagem.\n\nFico à disposição!"
        
    elif mensagem_selecionada == "Débito → Boleto":
        mensagem_final = f"Olá, {nome_cliente}! Boa tarde\n\nA {seguradora} enviou um aviso importante referente ao seu Seguro {tipo_seguro}.\n\nO débito automático da {parcela}º parcela não foi autorizado pela instituição financeira, e por isso o pagamento não foi efetuado.\n\nAssim, a seguradora alterou a forma de pagamento para boleto, com vencimento em {data_formatada}, para garantir a cobertura. Neste mês, o débito em conta não será processado.\n\nQualquer dúvida, estamos à disposição para ajudar!"
        
    elif mensagem_selecionada == "Não autorizado débito no Cartão de Crédito":
        mensagem_final = f"Olá, {nome_cliente}! Bom dia\n\nA {seguradora} enviou um aviso importante referente ao seu Seguro {tipo_seguro}.\n\nA {parcela}º parcela não foi debitada no cartão, e por isso o pagamento não foi efetuado.\n\nAssim, a seguradora alterou a forma de pagamento para boleto, com vencimento em {data_formatada}.\n\nQualquer dúvida, estamos à disposição para ajudar!"
        
    elif mensagem_selecionada == "Cliente não pagou a fatura":
        mensagem_final = f"Olá, {nome_cliente}! Boa tarde\n\nA *{seguradora}* enviou um aviso importante referente ao seu Seguro {tipo_seguro}.\n\nA *{parcela}º parcela* consta como *pendente* no sistema. Para regularizar o valor em aberto é necessário efetuar o pagamento total ou mínimo da sua última fatura gerada do seu Cartão {seguradora} Bank.\n\nQualquer dúvida, estamos à disposição para ajudar!"

# --- EXIBIÇÃO ---
st.divider()
st.subheader("Mensagem Gerada:")

if mensagem_final:
    st.code(mensagem_final, language="text")
    st.info("Para copiar a mensagem, basta passar o mouse sobre o quadro acima e clicar no ícone de cópia (dois quadrados) que aparecerá no canto superior direito.")
else:
    st.warning("Por favor, digite o nome do cliente para gerar a mensagem.")