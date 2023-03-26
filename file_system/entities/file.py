import abc
import dataclasses


@dataclasses.dataclass
class BaseFile(abc.ABC):
    """Classe abstrata para todos os arquivos.

    Atributos:
        name (str): O nome do arquivo..
        size (int): O tamanho do arquivo em megabytes.
    """

    name: str
    size: int
