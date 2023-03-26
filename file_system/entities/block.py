import abc
import dataclasses
import uuid


@dataclasses.dataclass
class BaseBlock(abc.ABC):
    """Classe abstrata para todos os blocos de memória.

    Atributos:
        - id (UUID): Identificador do bloco de memória.
        - size (int): Tamanho do block de memória em megabytes.
    """

    id: uuid.UUID
    size: int
