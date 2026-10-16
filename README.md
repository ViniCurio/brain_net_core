# Brain Net Core

Motor de perguntas e respostas no terminal baseado em uma base de conhecimento fictícia.

## Preparação

No PowerShell, dentro desta pasta:

```powershell
python -m venv venv
.\venv\Scripts\python.exe -m pip install -r requirements.txt
```

Configure sua chave do Google AI Studio como variável de ambiente `GEMINI_API_KEY` antes de executar o programa. Não coloque a chave em `brain.py` nem envie arquivos com chaves ao GitHub.

```powershell
.\venv\Scripts\python.exe brain.py
```

Digite `sair` para encerrar. A base de conhecimento está em `base_conhecimento.txt`. O modelo do guia original (`gemini-1.5-flash`) foi desativado; este projeto usa `gemini-3.8-flash`. O SDK `google-generativeai` foi mantido para seguir a atividade, embora o Google recomende migrar para `google-genai`.

O programa envia todo o texto da base em cada pergunta. O prompt pede respostas limitadas à base, mas isso, por si só, não garante ausência de alucinações.
