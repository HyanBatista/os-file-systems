import abc
import dataclasses
import uuid

from file_system.entities.block import BaseBlock


@dataclasses.dataclass
class BaseMemory(abc.ABC):
    """Classe abstrata para todas as memórias.

    Atributos:
        - id (UUID): Identificador da Memória.
        - size (int): Tamanho total da memória principal em megabytes.
        - blocks (list[BaseBlock]): Lista dos blocos de memória contidos na memória.
    """

    id: uuid.UUID
    size: int
    blocks: list[BaseBlock]
