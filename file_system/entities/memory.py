import abc
import dataclasses
import uuid


@dataclasses.dataclass
class BaseMemoryBlock(abc.ABC):
    """Classe abstrata para todos os blocos de memória.

    Atributos:
        - id (UUID): Identificador do bloco de memória.
        - size (int): Tamanho do block de memória em megabytes.
    """

    id: uuid.UUID
    size: int


@dataclasses.dataclass
class BaseMemory(abc.ABC):
    """Classe abstrata para todas as memórias.

    Atributos:
        - id (UUID): Identificador da Memória.
        - size (int): Tamanho total da memória principal em megabytes.
        - blocks (list[BaseMemoryBlock]): Lista dos blocos de memória contidos na memória.
    """

    id: uuid.UUID
    size: int
    blocks: list[BaseMemoryBlock]
