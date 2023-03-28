import abc
import copy
import uuid

from domain.entities.block import BaseBlock
from domain.repositories.errors.block import (
    BlockNotFoundError,
    BlockDoesNotExistError,
)


class BaseBlockRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, block: BaseBlock) -> BaseBlock:
        """Adiciona um objeto bloco no repositório.

        Args:
            block (BaseBlock): O objeto bloco a ser adicionado.
        """
        pass

    @abc.abstractmethod
    def remove(self, block: BaseBlock) -> BaseBlock:
        """Removes a block from the repository.

        Args:
            block (BaseBlock): O objeto bloco a ser removido.
        """
        pass

    @abc.abstractmethod
    def get(self, id: uuid.UUID) -> BaseBlock:
        """Recupera um objeto bloco usando seu ID.

        Args:
            block (BaseBlock): O objeto bloco a ser recuperado.
        """

    @abc.abstractmethod
    def update(self, block: BaseBlock) -> BaseBlock:
        """Atualiza um objeto bloco.

        Args:
            block (BaseBlock): O objeto bloco a ser atualizado.
        """


class InMemoryBlockRepository(BaseBlockRepository):
    def __init__(self) -> None:
        self.blocks: dict[int, BaseBlock] = {}
    
    def add(self, block: BaseBlock) -> None:
        block.id = len(self.blocks) + 1
        self.blocks[block.id] = copy.deepcopy(block)
        return copy.deepcopy(self.blocks[block.id])

    def remove(self, block: BaseBlock) -> BaseBlock:
        try:
            return self.blocks.pop(block.id)
        except KeyError:
            raise BlockDoesNotExistError

    def get(self, id: uuid.UUID) -> BaseBlock:
        try:
            return copy.deepcopy(self.blocks[id])
        except KeyError:
            raise BlockNotFoundError

    def update(self, block: BaseBlock) -> BaseBlock:
        try:
            block_ = self.blocks[block.id]
            for attribute, value in vars(block).items():
                setattr(block_, attribute, value)
            return copy.deepcopy(block_)
        except KeyError:
            raise BlockDoesNotExistError
