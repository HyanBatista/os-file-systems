import abc
import copy
import uuid

from file_system.entities.directory import BaseBlock
from file_system.usecases.errors.repositories.directory import (
    BlockNotFoundError,
    BlockDoesNotExistError,
)


class BaseBlockRepository(abc.ABC):
    abc.abstractmethod

    def add(self, block: BaseBlock) -> None:
        """Adiciona um objeto bloco no repositório.

        Args:
            block (BaseBlock): O objeto bloco a ser adicionado.
        """
        pass

    def remove(self, block: BaseBlock) -> None:
        """Removes a block from the repository.

        Args:
            block (BaseBlock): O objeto bloco a ser removido.
        """
        pass

    def get(self, id: uuid.UUID) -> BaseBlock:
        """Recupera um objeto bloco usando seu ID.

        Args:
            block (BaseBlock): O objeto bloco a ser recuperado.
        """

    def update(self, block: BaseBlock) -> None:
        """Atualiza um objeto bloco.

        Args:
            block (BaseBlock): O objeto bloco a ser atualizado.
        """
