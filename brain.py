import google.generativeai as genai
import os

# 1. Conectando o Cérebro (Cole sua chave da API do Google AI Studio aqui)
CHAVE_API = "SUA_CHAVE_AQUI"
genai.configure(api_key=CHAVE_API)
modelo = genai.GenerativeModel('gemini-3.8-flash')

print("🧠 Iniciando o Brain Net...")

# 2. Ingestão de Dados (Lendo a memória da empresa)
try:
    with open("base_conhecimento.txt", "r", encoding="utf-8") as arquivo:
        memoria_corporativa = arquivo.read()
    print("✅ Base de conhecimento carregada com sucesso!\n")
except FileNotFoundError:
    print("❌ Erro: Arquivo 'base_conhecimento.txt' não encontrado.")
    exit()

# 3. Loop do Chat (O Terminal Interativo)
print("💬 Converse com o Brain Net (Digite 'sair' para encerrar)")
print("-" * 50)

while True:
    pergunta = input("\n👤 Você: ")

    if pergunta.lower() == 'sair':
        print("Desligando o Brain Net...")
        break

    # 4. O Motor RAG (Juntando a Memória com a Pergunta)
    prompt_estruturado = f"""
    Você é o Brain Net, a inteligência artificial corporativa da empresa.
    Responda a pergunta do usuário baseando-se ESTRITAMENTE na Memória Corporativa abaixo.
    Se a resposta não estiver na memória, diga: 'Não possuo essa informação nos meus registros.'
    Nunca invente dados (zero alucinação).

    --- MEMÓRIA CORPORATIVA ---
    {memoria_corporativa}
    ---------------------------

    Pergunta do Usuário: {pergunta}
    """

    # 5. Processamento e Resposta
    resposta = modelo.generate_content(prompt_estruturado)
    print(f"🤖 Brain Net: {resposta.text}")
