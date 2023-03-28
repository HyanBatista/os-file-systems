import abc
import dataclasses
from domain.entities.linked_list import BaseBlockLinkedList


@dataclasses.dataclass
class BaseFile(abc.ABC):
    """Classe abstrata para todos os arquivos.

    Atributos:
        id (UUID): identificador do arquivo.
        name (str): O nome do arquivo.
        size (int): O tamanho do arquivo em megabytes.
    """

    name: str
    size: int

    def __str__(self) -> str:
        return self.name


@dataclasses.dataclass
class BaseLinkedFile(BaseFile):
    blocks: BaseBlockLinkedList


@dataclasses.dataclass
class BaseDirectory(BaseFile):
    files: list[BaseFile] | None = None


@dataclasses.dataclass
class LinkedDirectory(BaseDirectory, BaseLinkedFile):
    pass


@dataclasses.dataclass
class LinkedFile(BaseLinkedFile):
    pass
