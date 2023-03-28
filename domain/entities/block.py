import abc
import dataclasses
from typing_extensions import Self


@dataclasses.dataclass
class BaseBlock(abc.ABC):
    """Classe abstrata para todos os blocos.

    Atributos:
        - id (UUID): Identificador do bloco.
        - size (int): Tamanho do bloco em megabytes.
    """

    id: int | None
    size: int
    next: Self | None


class Block(BaseBlock):
    pass
