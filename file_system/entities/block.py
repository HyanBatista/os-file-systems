import abc
import dataclasses
import uuid


@dataclasses.dataclass
class BaseBlock(abc.ABC):
    """Classe abstrata para todos os blocos.

    Atributos:
        - id (UUID): Identificador do bloco.
        - size (int): Tamanho do bloco em megabytes.
    """

    id: uuid.UUID
    size: int
