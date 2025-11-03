import random
import string
import pyperclip  # pip install pyperclip

def gerar_senha(tamanho=12):
    """Gera uma senha segura com letras, números e símbolos."""
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def main():
    print("🔐 GERADOR DE SENHAS SEGURAS 🔐\n")

    try:
        tamanho = int(input("Digite o tamanho da senha (ex: 12): "))
    except ValueError:
        print("⚠️ Tamanho inválido! Usando 12 por padrão.")
        tamanho = 12

    senha = gerar_senha(tamanho)
    print(f"\n✅ Sua senha gerada: {senha}\n")

    # Copiar automaticamente para a área de transferência
    try:
        pyperclip.copy(senha)
        print("📋 Senha copiada para a área de transferência!")
    except Exception:
        print("⚠️ Não foi possível copiar automaticamente.")

if __name__ == "__main__":
    main()
