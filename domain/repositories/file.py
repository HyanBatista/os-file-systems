import abc
import copy
import uuid

from domain.entities.file import BaseFile, BaseDirectory
from domain.repositories.errors.file import (
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

    def get(self, name: str) -> BaseDirectory:
        """Recupera um objeto diretório usando seu nome.

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
        self.files: dict[str, BaseFile] = {}

    def add(self, file: BaseFile) -> BaseFile:
        self.files[file.name] = copy.deepcopy(file)
        return copy.deepcopy(file)

    def remove(self, file: BaseFile) -> BaseFile:
        try:
            return self.files.pop(file.name)
        except KeyError:
            raise FileDoesNotExistError

    def get(self, name: str) -> BaseFile:
        try:
            return copy.deepcopy(self.files[name])
        except KeyError:
            raise FileNotFoundError

    def update(self, file: BaseFile) -> BaseFile:
        try:
            file_ = self.files[file.name]
            for attribute, value in vars(file).items():
                setattr(file_, attribute, value)
            return copy.deepcopy(file_)
        except KeyError:
            raise FileDoesNotExistError


class InMemoryDirectoryRepository(BaseDirectoryRepository):
    def __init__(self) -> None:
        self.directories: dict[str, BaseDirectory] = {}

    def add(self, directory: BaseFile) -> BaseFile:
        self.directories[directory.name] = copy.deepcopy(directory)
        return copy.deepcopy(directory)

    def remove(self, directory: BaseFile) -> BaseFile:
        try:
            return self.directories.pop(directory.name)
        except KeyError:
            raise DirectoryDoesNotExistError

    def get(self, name: str) -> BaseDirectory:
        try:
            return copy.deepcopy(self.directories[name])
        except KeyError:
            raise DirectoryNotFoundError

    def update(self, directory: BaseDirectory) -> BaseDirectory:
        try:
            directory_ = self.directories[directory.name]
            for attribute, value in vars(directory).items():
                setattr(directory_, attribute, value)
            return copy.deepcopy(directory_)
        except KeyError:
            raise DirectoryDoesNotExistError

    def list(self) -> list[BaseDirectory]:
        return [copy.deepcopy(value) for _, value in self.directories.items()]
