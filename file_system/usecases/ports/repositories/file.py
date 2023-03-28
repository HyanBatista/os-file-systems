import abc
import copy
import uuid

from file_system.entities.file import BaseFile, BaseDirectory
from file_system.usecases.errors.ports.repositories.file import (
    DirectoryNotFoundError,
    DirectoryDoesNotExistError,
    FileNotFoundError,
    FileDoesNotExistError,
)


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
    def get(self, id: uuid.UUID) -> BaseFile:
        """Recupera um objeto arquivo usando seu ID.

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


class BaseDirectoryRepository(BaseFileRepository):
    abc.abstractmethod

    def add(self, directory: BaseDirectory) -> BaseDirectory:
        """Adiciona um objeto diretório no repositório.

        Args:
            directory (BaseDirectory): O objeto diretório a ser adicionado.
        """
        pass

    def remove(self, directory: BaseDirectory) -> BaseDirectory:
        """Removes a file from the repository.

        Args:
            directory (BaseDirectory): O objeto diretório a ser removido.
        """
        pass

    def get(self, id: uuid.UUID) -> BaseDirectory:
        """Recupera um objeto diretório usando seu ID.

        Args:
            directory (BaseDirectory): O objeto diretório a ser recuperado.
        """
        pass

    def update(self, directory: BaseDirectory) -> BaseDirectory:
        """Atualiza um objeto diretório.

        Args:
            directory (BaseDirectory): O objeto diretório a ser atualizado.
        """
        pass

    def list(self) -> list[BaseDirectory]:
        """Lista todos os diretórios."""
        pass


class InMemoryFileRepository(BaseFileRepository):
    def __init__(self) -> None:
        self.files: dict[uuid.UUID, BaseFile] = {}

    def add(self, file: BaseFile) -> BaseFile:
        file.id = uuid.uuid4()
        self.files[file.id] = copy.deepcopy(file)
        return copy.deepcopy(file)

    def remove(self, file: BaseFile) -> BaseFile:
        try:
            return self.files.pop(file.id)
        except KeyError:
            raise FileDoesNotExistError

    def get(self, id: uuid.UUID) -> BaseFile:
        try:
            return copy.deepcopy(self.files[id])
        except KeyError:
            raise FileNotFoundError

    def update(self, file: BaseFile) -> BaseFile:
        try:
            file_ = self.disks[file.id]
            for attribute, value in vars(file).items():
                setattr(file_, attribute, value)
            return copy.deepcopy(file_)
        except KeyError:
            raise FileDoesNotExistError


class InMemoryDirectoryRepository(BaseDirectoryRepository):
    def __init__(self) -> None:
        self.directories: dict[uuid.UUID, BaseDirectory] = {}

    def add(self, directory: BaseFile) -> BaseFile:
        directory.id = uuid.uuid4()
        self.directories[directory.id] = copy.deepcopy(directory)
        return copy.deepcopy(directory)

    def remove(self, directory: BaseFile) -> BaseFile:
        try:
            return self.directories.pop(directory.id)
        except KeyError:
            raise DirectoryDoesNotExistError

    def get(self, id: uuid.UUID) -> BaseDirectory:
        try:
            return copy.deepcopy(self.directories[id])
        except KeyError:
            raise DirectoryNotFoundError

    def update(self, directory: BaseDirectory) -> BaseDirectory:
        try:
            directory_ = self.directories[directory.id]
            for attribute, value in vars(directory).items():
                setattr(directory_, attribute, value)
            return copy.deepcopy(directory_)
        except KeyError:
            raise DirectoryDoesNotExistError

    def list(self) -> list[BaseDirectory]:
        return [copy.deepcopy(value) for _, value in self.directories.items()]
