import abc
import copy
import uuid

from domain.entities.file import BaseFile, BaseLinkedFile, LinkedDirectory
from domain.entities.disk import BaseDisk
from domain.repositories.errors.file import (
    DirectoryDoesNotExistError,
    FileNotFoundError,
    FileDoesNotExistError,
)
from domain.repositories.disk import BaseDiskRepository


class BaseFileRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, file: BaseFile) -> BaseFile:
        """Adiciona um objeto arquivo no repositório.

        Args:
            file (BaseFile): O objeto arquivo a ser adicionado.
        """
        pass

    @abc.abstractmethod
    def remove(self, file: BaseFile) -> BaseFile:
        """Removes a file from the repository.

        Args:
            file (BaseFile): O objeto arquivo a ser removido.
        """
        pass

    @abc.abstractmethod
    def get(self, name: str) -> BaseFile:
        """Recupera um objeto arquivo usando seu nome.

        Args:
            file (BaseFile): O objeto arquivo a ser recuperado.
        """
        pass

    @abc.abstractmethod
    def update(self, file: BaseFile) -> BaseFile:
        """Atualiza um objeto arquivo.

        Args:
            file (BaseFile): O objeto arquivo a ser atualizado.
        """
        pass

    @abc.abstractmethod
    def list(self) -> list[BaseFile]:
        """Lista os arquivos."""
        pass


class BaseLinkedFileRepository(BaseFileRepository):
    @abc.abstractmethod
    def add(self, file: BaseLinkedFile) -> BaseLinkedFile:
        """Adiciona um objeto arquivo no repositório.

        Args:
            file (BaseLinkedFile): O objeto arquivo a ser adicionado.
        """
        pass

    @abc.abstractmethod
    def remove(self, file: BaseLinkedFile) -> BaseLinkedFile:
        """Removes a file from the repository.

        Args:
            file (BaseLinkedFile): O objeto arquivo a ser removido.
        """
        pass

    @abc.abstractmethod
    def get(self, name: str) -> BaseLinkedFile:
        """Recupera um objeto arquivo usando seu nome.

        Args:
            file (BaseLinkedFile): O objeto arquivo a ser recuperado.
        """
        pass

    @abc.abstractmethod
    def update(self, file: BaseLinkedFile) -> BaseLinkedFile:
        """Atualiza um objeto arquivo.

        Args:
            file (BaseLinkedFile): O objeto arquivo a ser atualizado.
        """
        pass

    @abc.abstractmethod
    def list(self) -> list[BaseLinkedFile]:
        """Lista os arquivos."""
        pass


class DiskLinkedFileRepository(BaseLinkedFileRepository):
    def __init__(self, disk: BaseDisk, repository: BaseDiskRepository) -> None:
        self.disk = disk
        self.repository = repository

    def add(self, file: BaseLinkedFile) -> BaseLinkedFile:
        for block in self.disk.blocks:
            if not block.used:
                file.blocks.append(block)
                block.used = True

        self.disk.files.append(file)
        self.disk = self.repository.update(self.disk)

        return copy.deepcopy(file)
    
    def list(self) -> list[BaseLinkedFile]:
        return [copy.deepcopy(file) for file in self.disk.files]

    def remove(self, file: BaseLinkedFile) -> BaseLinkedFile:
        for block in file.blocks.to_list():
            block.used = False
            block.next = None
        
        file.blocks = None
        self.disk.files = None

        self.repository.update(self.disk)

        return copy.deepcopy(file)

    def update(self, file: BaseLinkedFile) -> BaseLinkedFile:
            for file_ in self.disk.files:
                if file_.name == file.name:
                    for attribute, value in vars(file).items():
                        setattr(file_, attribute, value)
                    self.repository.update(self.disk)
                    return copy.deepcopy(file_)

            if type(file, LinkedDirectory):
                raise DirectoryDoesNotExistError
            else:
                raise FileDoesNotExistError

    def get(self, name: str) -> BaseLinkedFile:
        for file_ in self.disk.files:
            if file_.name == name:
                return copy.deepcopy(file_)
            
        raise FileNotFoundError
