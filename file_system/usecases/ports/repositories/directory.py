import abc
import copy
import uuid

from file_system.entities.directory import BaseDirectory
from file_system.usecases.errors.repositories.directory import (
    DirectoryNotFoundError,
    DirectoryDoesNotExistError,
)


class BaseDirectoryRepository(abc.ABC):
    abc.abstractmethod

    def add(self, directory: BaseDirectory) -> None:
        """Adiciona um objeto diretório no repositório.

        Args:
            directory (BaseDirectory): O objeto diretório a ser adicionado.
        """
        pass

    def remove(self, directory: BaseDirectory) -> None:
        """Removes a directory from the repository.

        Args:
            directory (BaseDirectory): O objeto diretório a ser removido.
        """
        pass

    def get(self, id: uuid.UUID) -> BaseDirectory:
        """Recupera um objeto diretório usando seu ID.

        Args:
            directory (BaseDirectory): O objeto diretório a ser recuperado.
        """

    def update(self, directory: BaseDirectory) -> None:
        """Atualiza um objeto diretório.

        Args:
            directory (BaseDirectory): O objeto diretório a ser atualizado.
        """
