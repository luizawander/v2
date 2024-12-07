import os
import pandas as pd
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage

# Diretório do script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Caminho absoluto para o arquivo de prompt
prompt_path = os.path.join(script_dir, "prompt_0.txt")

# Função para carregar o Prompt do Arquivo
def load_prompt(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Arquivo de prompt não encontrado: {file_path}")
    print("Carregando prompt:", file_path)
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

# Carregar o Prompt Estruturado
structured_prompt = load_prompt(prompt_path)

# Modelo de linguagem
chat_model = ChatOpenAI(
    model="gpt-4",
    temperature=0,


# Caminho absoluto para o arquivo Excel
adaptabrasil_filepath = os.path.join(script_dir, "Base de Riscos do Adapta Brasil.xlsx")

# Função para carregar dados do AdaptaBrasil
def load_adaptabrasil_data(filepath):
    """Carrega os dados climáticos do AdaptaBrasil"""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Arquivo não encontrado: {filepath}")
    print("Carregando arquivo Excel:", filepath)
    df = pd.read_excel(filepath)
    return df

# Verificação de existência do arquivo Excel
if not os.path.exists(adaptabrasil_filepath):
    print(f"Erro: Arquivo Excel não encontrado no caminho: {adaptabrasil_filepath}")
    adaptabrasil_data = None
else:
    adaptabrasil_data = load_adaptabrasil_data(adaptabrasil_filepath)

# Função para rodar o chatbot
def run_resiliencIA():
    print("Iniciando ResiliêncIA. Digite 'sair' para encerrar a conversa.")
    print("ResiliêncIA: Olá! Sou ResiliêncIA, seu assistente para criar um Plano Local de Ação Climática. Para começar, informe o nome do município e estado.")

    history = [
        AIMessage(content="Olá! Sou ResiliêncIA, seu assistente para criar um Plano Local de Ação Climática. Para começar, informe o nome do município e estado.")
    ]

    while True:
        user_input = input("Você: ")
        if user_input.lower() == "sair":
            print("ResiliêncIA: Obrigado por usar a ferramenta. Até logo!")
            break

        history.append(HumanMessage(content=user_input))
        response = chat_model.invoke(history)
        history.append(AIMessage(content=response.content))
        print(f"ResiliêncIA: {response.content}")

if __name__ == "__main__":
    if adaptabrasil_data is not None:
        run_resiliencIA()
