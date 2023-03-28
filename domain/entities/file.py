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
    blocks: BaseBlockLinkedList | None = None


@dataclasses.dataclass
class LinkedDirectory(BaseLinkedFile):
    files: list[BaseFile] | None = None


@dataclasses.dataclass
class LinkedFile(BaseLinkedFile):
    pass


class BaseFileFactory(abc.ABC):
    abc.abstractmethod

    def __call__(self, name: str, size: int) -> BaseFile:
        pass


class LinkedDirectoryFactory(BaseFileFactory):
    def __call__(self, name: str, size: int) -> LinkedDirectory:
        directory = LinkedDirectory(name, size)
        return directory


class LinkedFileFactory(BaseFileFactory):
    def __call__(self, name: str, size: int) -> LinkedFile:
        file = LinkedFile(name, size)
        return file


class FileFactoryRegistry:
    def __init__(self) -> None:
        self.factories = {}

    def register_factory(self, type: str, factory: BaseFileFactory) -> None:
        self.factories[type] = factory

    def get_factory(self, type: str) -> BaseFileFactory:
        return self.factories[type]
