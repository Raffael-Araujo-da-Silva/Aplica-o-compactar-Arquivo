import zipfile
import sys

if len(sys.argv) < 3:
    file_path = r'C:\Users\Rafael\Desktop\arquivo origem'  # Substitua pelo caminho do arquivo que você deseja zipar
    zip_file = r'C:\Users\Rafael\Desktop\arquivo destino\destino.zip'  # Substitua pelo caminho onde você deseja salvar o arquivo ZIP
else:
    file_path = sys.argv[1]
    zip_file = sys.argv[2]

if file_path == "":
    print("Erro: Nenhum arquivo especificado.")
    exit(1)

if zip_file == "":
    print("Erro: Nenhum nome de arquivo ZIP especificado.")
    exit(1)

try:
    with zipfile.ZipFile(zip_file, 'w') as zipf:
        zipf.write(file_path, arcname=file_path)
    print("Compactação concluída.")
except FileNotFoundError:
    print("Erro: O arquivo especificado não existe.")
    exit(1)
except Exception as e:
    print("Erro durante a compactação:", e)
    exit(1)