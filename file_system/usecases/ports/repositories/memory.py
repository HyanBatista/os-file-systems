import abc
import copy
import uuid

from file_system.entities.memory import BaseMemory
from file_system.usecases.errors.repositories.memory import (
    MemoryNotFoundError,
    MemoryDoesNotExistError,
)


class BaseMemoryRepository(abc.ABC):
    abc.abstractmethod

    def add(self, memory: BaseMemory) -> None:
        """Adiciona um objeto memória no repositório.

        Args:
            memory (BaseMemory): O objeto memória a ser adicionado.
        """
        pass

    def remove(self, memory: BaseMemory) -> None:
        """Removes a memory from the repository.

        Args:
            memory (BaseMemory): O objeto memória a ser removido.
        """
        pass

    def get(self, id: uuid.UUID) -> BaseMemory:
        """Recupera um objeto memória usando seu ID.

        Args:
            memory (BaseMemory): O objeto memória a ser recuperado.
        """
    
    def update(self, memory: BaseMemory) -> None:
        """Atualiza um objeto memória.

        Args:
            memory (BaseMemory): O objeto memória a ser atualizado.
        """
