import abc
import dataclasses


@dataclasses.dataclass
class BaseMemoryBlock(abc.ABC):
    """Classe abstrata para todos os blocos de memória.

    Atributos:
        - size (int): Tamanho do block de memória em megabytes.
    """
    size: int

@dataclasses.dataclass
class BaseMemory(abc.ABC):
    """Classe abstrata para todas as memórias.

    Atributos:
        - size (int): Tamanho total da memória principal em megabytes.
        - blocks (list[BaseMemoryBlock]): Lista dos blocos de memória contidos na memória.
    """
    size: int
    blocks: list[BaseMemoryBlock]
