from file_system.entities.file import BaseDirectory
from file_system.usecases.file import CreateDirectory, ListDirectories


class CreateDirectoryUI:
    def __init__(self, create_directory: CreateDirectory) -> None:
        self.create_directory = create_directory

    def __call__(self) -> None:
        name = input("Digite um nome: ")

        try:
            self.create_directory(name)
            print(f"O repositório foi criado com sucesso!")
        except Exception as e:
            print(f"Falha ao criar diretório: {str(e)}")


class ShowOptionsUI:
    def __call__(self) -> None:
        print("-----------------------------------------")
        print("Operações do Sistema de Arquivos")
        print("0 - Sair")
        print("1 - Criar diretório")
        print("2 - Deletar diretório")
        print("3 - Criar arquivo")
        print("4 - Deletar arquivo")
        print("-----------------------------------------")

class ShowDirectoriesUI:
    def __init__(self, list_directories: ListDirectories):
        self.list_directories = list_directories

    def __call__(self) -> None:
        print("-----------------------------------------")
        print("Diretórios:")
        directories = self.list_directories()
        for directory in directories:
            print("***", str(directory), "***")
        print("-----------------------------------------")