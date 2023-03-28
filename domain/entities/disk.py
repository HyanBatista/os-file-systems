import abc
import dataclasses
import uuid

from domain.entities.block import BaseBlock


@dataclasses.dataclass
class BaseDisk(abc.ABC):
    """Classe abstrata para todos os discos.

    Atributos:
        - id (UUID): Identificador do disco.
        - size (int): Tamanho total do disco principal em megabytes.
        - blocks (list[BaseBlock]): Lista dos blocos de disco contidos na disco.
    """

    size: int
    id: uuid.UUID | None = None
    blocks: list[BaseBlock] | None = None


class Disk(BaseDisk):
    pass
