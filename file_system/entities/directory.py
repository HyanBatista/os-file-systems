import abc
import dataclasses

from file_system.entities.file import BaseFile


@dataclasses.dataclass
class BaseDirectory(abc.ABC):
    """Classe abstrata para todos os diretórios.

    Atributos:
        name (str): O nome do diretório..
        size (int): O tamanho do diretório em megabytes.
        files (list[BaseFile]): A lista dos objectos armazenados no diretório.
    """

    name: str
    size: int
    files: list[BaseFile]
