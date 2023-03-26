import abc
import dataclasses
import uuid

from file_system.entities.block import BaseBlock


@dataclasses.dataclass
class BaseDisk(abc.ABC):
    """Classe abstrata para todos os discos.

    Atributos:
        - id (UUID): Identificador do disco.
        - size (int): Tamanho total do disco principal em megabytes.
        - blocks (list[BaseBlock]): Lista dos blocos de disco contidos na disco.
    """

    id: uuid.UUID
    size: int
    blocks: list[BaseBlock]
