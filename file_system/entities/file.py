import abc
import dataclasses
import uuid


@dataclasses.dataclass
class BaseFile(abc.ABC):
    """Classe abstrata para todos os arquivos.

    Atributos:
        id (UUID): identificador do arquivo.
        name (str): O nome do arquivo..
        size (int): O tamanho do arquivo em megabytes.
    """

    id: uuid.UUID
    name: str
    size: int
