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
    used: bool = False

    def __str__(self) -> str:
        return f"{str(self.id)}:{str(self.size)}"


class Block(BaseBlock):
    pass


class BaseBlockFactory(abc.ABC):
    @abc.abstractmethod
    def __call__(self, id: int, size: int) -> BaseBlock:
        pass


class BlockFactory(BaseBlockFactory):
    def __call__(self, id: int, size: int) -> Block:
        block = Block(id=id, size=size, next=None)
        return block


class BlockFactoryRegistry:
    def __init__(self):
        self.factories = {}

    def register_factory(self, type: str, factory: BaseBlockFactory) -> None:
        self.factories[type] = factory

    def get_factory(self, type: str) -> BaseBlockFactory:
        return self.factories[type]


registry = BlockFactoryRegistry()
registry.register_factory("block", BlockFactory())
