import os

from application import usecases
from application.interfaces import ui
from domain import repositories


def main():
    # Criar discco.
    disk_repository = repositories.disk.InMemoryDiskRepository()
    disk = usecases.disk.CreateDisk(disk_repository)(block_type="block", block_size=200, number_blocks=14)

    # Iniciar repositório dos arquivos.
    file_repository = repositories.file.DiskLinkedFileRepository(disk, disk_repository)

    run = True
    while run:
        ui.ShowDiskInformationUI()(usecases.disk.ListDisks(disk_repository))
        print()
        ui.ShowDirectoriesUI(usecases.file.ListLinkedFiles(file_repository))()
        print()
        ui.ShowOptionsUI()()
        option = int(input())

        if option == 0:
            run = False
        elif option == 1:
            pass
            ui.CreateLinkedDirectoryUI(usecases.file.CreateLinkedFile(file_repository))()
        elif option == 2:
            # ui.RemoveDirectoryUI(usecases.file.RemoveDirectory(file_repository))()
            pass
        else:
            print("Opções inválida!")
        
        input("Aperte Enter para continuar...")
        os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    main()
