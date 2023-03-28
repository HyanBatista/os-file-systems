import abc
import dataclasses
from domain.entities.linked_list import BaseBlockLinkedList
from typing_extensions import Self


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
    parent: Self | None
    children: list[Self]
    blocks: BaseBlockLinkedList | None = None


@dataclasses.dataclass
class LinkedDirectory(BaseLinkedFile):
    pass


@dataclasses.dataclass
class LinkedFile(BaseLinkedFile):
    
    def __str__(self) -> str:
        return self.name


class BaseFileFactory(abc.ABC):
    @abc.abstractmethod
    def __call__(self, name: str, size: int) -> BaseFile:
        pass


class BaseLinkedFileFactory(BaseFileFactory):
    @abc.abstractmethod
    def __call__(self, name: str, size: int, parent: BaseLinkedFile, children: list[BaseLinkedFile]) -> BaseLinkedFile:
        pass


class LinkedDirectoryFactory(BaseLinkedFileFactory):
    def __call__(self, name: str, size: int, parent: BaseLinkedFile, children: list[BaseLinkedFile]) -> LinkedDirectory:
        directory = LinkedDirectory(name=name, size=size, parent=parent, children=children)
        return directory


class LinkedFileFactory(BaseLinkedFileFactory):
    def __call__(self, name: str, size: int, parent: BaseLinkedFile, children: list[BaseLinkedFile]) -> LinkedFile:
        file = LinkedFile(name=name, size=size, parent=parent, children=children)
        return file


class LinkedFileFactoryRegistry:
    def __init__(self) -> None:
        self.factories = {}

    def register_factory(self, type: str, factory: BaseLinkedFileFactory) -> None:
        self.factories[type] = factory

    def get_factory(self, type: str) -> BaseLinkedFileFactory:
        return self.factories[type]


linked_file_registry = LinkedFileFactoryRegistry()
linked_file_registry.register_factory("file", LinkedFileFactory())
linked_file_registry.register_factory("directory", LinkedDirectoryFactory())
