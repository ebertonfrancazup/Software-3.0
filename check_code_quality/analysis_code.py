import os
import ollama

def read_files(file_paths):
    """Lê o conteúdo de uma lista de arquivos."""
    contents = {}
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            contents[file_path] = file.read()
    return contents

def evaluate_code_quality(file_contents):
    """Avalia a qualidade do código usando o modelo LLAMA 3."""
    evaluations = {}
    for file_path, content in file_contents.items():
        response = ollama.chat(model='llama3', messages=[
            {'role': 'user', 'content': f'Por favor, avalie a qualidade do seguinte código:\n\n{content}'}
        ])
        evaluations[file_path] = response['message']['content']
    return evaluations

def main():
    # Lista de arquivos a serem avaliados
    file_paths = ['basic_chat/openai_chat.py']
    
    # Ler o conteúdo dos arquivos
    file_contents = read_files(file_paths)
    
    # Avaliar a qualidade do código
    evaluations = evaluate_code_quality(file_contents)
    
    # Imprimir as avaliações
    for file_path, evaluation in evaluations.items():
        print(f"Avaliação do arquivo {file_path}:\n{evaluation}\n")

if __name__ == "__main__":
    main()