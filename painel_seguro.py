
import webbrowser
import getpass

senha_correta = "theonethatgotaway"

print("Painel Seguro - Ativação")
senha = getpass.getpass("Digite a senha para acessar o painel: ")

if senha == senha_correta:
    print("✅ Acesso autorizado! Abrindo painel...")
    webbrowser.open("index.html")
else:
    print("❌ Senha incorreta. Acesso negado.")
