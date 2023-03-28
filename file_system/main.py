import os

from file_system import usecases
from file_system.interfaces import ui
from file_system.usecases.ports import repositories


def main():
    # Iniciar os repositórios.
    disk_repository = repositories.disk.InMemoryDiskRepository()
    file_repository = repositories.file.InMemoryFileRepository()
    directory_repository = repositories.file.InMemoryDirectoryRepository()
    block_repository = repositories.block.InMemoryBlockRepository()

    run = True
    while run:
        ui.ShowDirectoriesUI(usecases.file.ListDirectories(directory_repository))()
        print()
        ui.ShowOptionsUI()()
        option = int(input())

        if option == 0:
            run = False
        elif option == 1:
            ui.CreateDirectoryUI(usecases.file.CreateDirectory(directory_repository))()
        elif option == 2:
            ui.RemoveDirectoryUI(usecases.file.RemoveDirectory(directory_repository))()
        else:
            print("Opções inválida!")

        os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    main()
