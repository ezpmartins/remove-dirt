import os
import string

def remove_special_chars_from_file(file_path):
    special_chars = [
        chr(8),  # BACKSPACE (BS)
        chr(7),  # BEL
        chr(27)  # ESC
    ]

    try:
        with open(file_path, 'rb') as file:
            content = file.read()

        cleaned_content = content
        for char in special_chars:
            cleaned_content = cleaned_content.replace(char.encode(), b'')

        with open(file_path, 'wb') as file:
            file.write(cleaned_content)
        print(f"Limpeza concluída: {file_path}")
    except Exception as e:
        print(f"Erro ao processar {file_path}: {e}")

def clean_directory(directory_path):
    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            remove_special_chars_from_file(file_path)

if __name__ == "__main__":
    directory = input("Digite o caminho da pasta para limpar os arquivos: ")
    if os.path.isdir(directory):
        clean_directory(directory)
    else:
        print("Caminho inválido. Certifique-se de fornecer uma pasta válida.")