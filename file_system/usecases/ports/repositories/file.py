import abc
import copy
import uuid

from file_system.entities.file import BaseFile
from file_system.usecases.errors.repositories.file import (
    FileNotFoundError,
    FileDoesNotExistError,
)


class BaseFileRepository(abc.ABC):
    abc.abstractmethod

    def add(self, file: BaseFile) -> None:
        """Adiciona um objeto arquivo no repositório.

        Args:
            file (BaseFile): O objeto arquivo a ser adicionado.
        """
        pass

    def remove(self, file: BaseFile) -> None:
        """Removes a file from the repository.

        Args:
            file (BaseFile): O objeto arquivo a ser removido.
        """
        pass

    def get(self, id: uuid.UUID) -> BaseFile:
        """Recupera um objeto arquivo usando seu ID.

        Args:
            file (BaseFile): O objeto arquivo a ser recuperado.
        """
    
    def update(self, file: BaseFile) -> None:
        """Atualiza um objeto arquivo.

        Args:
            file (BaseFile): O objeto arquivo a ser atualizado.
        """
