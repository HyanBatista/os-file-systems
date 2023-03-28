# from application.usecases.file import CreateDirectory, ListDirectories, RemoveDirectory
from application.usecases.disk import ListDisks


# class CreateDirectoryUI:
#     def __init__(self, create_directory: CreateDirectory) -> None:
#         self.create_directory = create_directory

#     def __call__(self) -> None:
#         name = input("Digite um nome: ")

#         try:
#             self.create_directory(name)
#             print(f"O repositório foi criado com sucesso!")
#         except Exception as e:
#             print(f"Falha ao criar diretório: {str(e)}")


# class RemoveDirectoryUI:
#     def __init__(self, remove_directory: RemoveDirectory) -> None:
#         self.remove_directory = remove_directory

#     def __call__(self) -> None:
#         name = input("Digite o nome do diretório: ")

#         try:
#             self.remove_directory(name)
#             print("O diretório foi removido com sucesso!")
#         except Exception as e:
#             print(f"Falha ao remover diretório: {str(e)}")


class ShowOptionsUI:
    def __call__(self) -> None:
        print("-----------------------------------------")
        print("Operações do Sistema de Arquivos")
        print("0 - Sair")
        print("1 - Criar diretório")
        print("2 - Deletar diretório")
        print("3 - Criar arquivo")
        print("4 - Deletar arquivo")
        print("5 - Listar arquivos de um diretório")
        print("-----------------------------------------")


# class ShowDirectoriesUI:
#     def __init__(self, list_directories: ListDirectories):
#         self.list_directories = list_directories

#     def __call__(self) -> None:
#         print("-----------------------------------------")
#         print("Diretórios:")
#         directories = self.list_directories()
#         for directory in directories:
#             print("***", str(directory), "***")
#         print("-----------------------------------------")


class ShowDiskInformationUI:
    def __call__(self, list_disks: ListDisks) -> None:
        print("-----------------------------------------")
        disks = list_disks()
        for disk in disks:
            print(f"[ 'ID': {disk.id}, 'Tamanho': {disk.size}, 'Fragmentado': 'disk.is_fragmented' ]")
        print("-----------------------------------------")
