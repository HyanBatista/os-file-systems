import abc
import copy
import uuid

from file_system.entities.disk import BaseDisk
from file_system.usecases.errors.repositories.disk import (
    DiskNotFoundError,
    DiskDoesNotExistError,
)


class BaseDiskRepository(abc.ABC):
    abc.abstractmethod

    def add(self, disk: BaseDisk) -> None:
        """Adiciona um objeto disco no repositório.

        Args:
            disk (BaseDisk): O objeto disco a ser adicionado.
        """
        pass

    def remove(self, disk: BaseDisk) -> None:
        """Removes a disk from the repository.

        Args:
            disk (BaseDisk): O objeto disco a ser removido.
        """
        pass

    def get(self, id: uuid.UUID) -> BaseDisk:
        """Recupera um objeto disco usando seu ID.

        Args:
            disk (BaseDisk): O objeto disco a ser recuperado.
        """
    
    def update(self, disk: BaseDisk) -> None:
        """Atualiza um objeto disco.

        Args:
            disk (BaseDisk): O objeto disco a ser atualizado.
        """
