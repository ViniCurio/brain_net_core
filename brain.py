import os
import sys

import google.generativeai as genai

sys.stdout.reconfigure(encoding="utf-8")


# 1. Conectando o Cérebro
CHAVE_API = os.getenv("GEMINI_API_KEY")
if not CHAVE_API:
    raise SystemExit("Erro: defina GEMINI_API_KEY antes de iniciar o Brain Net.")

genai.configure(api_key=CHAVE_API)
modelo = genai.GenerativeModel("gemini-3.8-flash")

print("🧠 Iniciando o Brain Net...")

# 2. Ingestão de Dados (Lendo a memória da empresa)
try:
    with open("base_conhecimento.txt", "r", encoding="utf-8") as arquivo:
        memoria_corporativa = arquivo.read()
    print("✅ Base de conhecimento carregada com sucesso!\n")
except FileNotFoundError:
    print("❌ Erro: Arquivo 'base_conhecimento.txt' não encontrado.")
    raise SystemExit(1)

# 3. Loop do Chat (O Terminal Interativo)
print("💬 Converse com o Brain Net (Digite 'sair' para encerrar)")
print("-" * 50)

while True:
    pergunta = input("\n👤 Você: ")

    if pergunta.lower() == "sair":
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
