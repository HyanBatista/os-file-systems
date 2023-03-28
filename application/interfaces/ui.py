# from application.usecases.file import CreateDirectory, ListDirectories, RemoveDirectory
from application.usecases.file import (
    CreateLinkedFile,
    ListLinkedFiles,
    RemoveLinkedFile,
)
from application.usecases.disk import ListDisks
from domain.entities.file import LinkedDirectory, LinkedFile
from domain.entities.linked_list import BlockLinkedList


class CreateLinkedDirectoryUI:
    def __init__(self, create_linked_file: CreateLinkedFile) -> None:
        self.create_linked_file = create_linked_file

    def __call__(self) -> None:
        name = input("Digite um nome: ")
        blocks = BlockLinkedList()
        size = 0
        type = "directory"

        try:
            self.create_linked_file(
                name=name, size=size, type=type, blocks=blocks, parent=[], children=[]
            )
            print(f"O repositório foi criado com sucesso!")
        except Exception as e:
            print(f"Falha ao criar diretório: {str(e)}")


class RemoveLinkedDirectoryUI:
    def __init__(self, remove_linked_file: RemoveLinkedFile) -> None:
        self.remove_linked_file = remove_linked_file

    def __call__(self) -> None:
        name = input("Digite o nome do diretório: ")

        try:
            self.remove_linked_file(name)
            print("O diretório foi removido com sucesso!")
        except Exception as e:
            print(f"Falha ao remover diretório: {str(e)}")


class RemoveLinkedFileUI:
    def __init__(self, remove_linked_file: RemoveLinkedFile) -> None:
        self.remove_linked_file = remove_linked_file
    
    def __call__(self) -> None:
        name = input("Digite o nome do arquivo: ")

        try:
            self.remove_linked_file(name)
            print("O arquivo foi removido com sucesso!")
        except Exception as e:
            print(f"Falha ao remover arquivo: {str(e)}")


class CreateLinkedFileUI:
    def __init__(self, create_linked_file: CreateLinkedFile) -> None:
        self.create_linked_file = create_linked_file

    def __call__(self) -> None:
        name = input("Digite o nome do arquivo: ")
        size = int(input("Digite o seu tamanho (megabytes): "))
        directory = input("Em qual diretório deseja criar o arquivo? ")
        type = "file"
        blocks = BlockLinkedList()

        try:
            self.create_linked_file(
                name=name,
                size=size,
                type=type,
                blocks=blocks,
                parent=directory,
                children=[],
            )
            print("O arquivo foi criado com sucesso!")
        except Exception as e:
            print(f"Falha ao criar o arquivo: {str(e)}")


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
    def __init__(self, list_linked_files: ListLinkedFiles):
        self.list_linked_files = list_linked_files

    def __call__(self) -> None:
        print("-----------------------------------------")
        print("Sistema de Arquivos:\n")
        files = self.list_linked_files()
        for file in files:
            if isinstance(file, LinkedDirectory):
                print(f"{file.name}/")
                for child in file.children:
                    print(f"|__{child.name}")
        print("-----------------------------------------")


class ShowDiskInformationUI:
    def __call__(self, list_disks: ListDisks) -> None:
        print("-----------------------------------------")
        disks = list_disks()
        for disk in disks:
            print(
                f"[ 'ID': {disk.id}, 'Tamanho': {disk.size}, 'Fragmentado': 'disk.is_fragmented' ]"
            )
        print("-----------------------------------------")
