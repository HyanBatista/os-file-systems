import abc
import copy
import uuid

from domain.entities.disk import BaseDisk
from domain.repositories.errors.disk import (
    DiskNotFoundError,
    DiskDoesNotExistError,
)


class BaseDiskRepository(abc.ABC):
    abc.abstractmethod

    def add(self, disk: BaseDisk) -> None:
        """Adiciona um objeto disco no repositório.

        Args:
            disk (BaseDisk): O objeto disco a ser adicionado.
        """
        pass

    def remove(self, disk: BaseDisk) -> None:
        """Removes a disk from the repository.

        Args:
            disk (BaseDisk): O objeto disco a ser removido.
        """
        pass

    def get(self, id: uuid.UUID) -> BaseDisk:
        """Recupera um objeto disco usando seu ID.

        Args:
            disk (BaseDisk): O objeto disco a ser recuperado.
        """
    
    def update(self, disk: BaseDisk) -> None:
        """Atualiza um objeto disco.

        Args:
            disk (BaseDisk): O objeto disco a ser atualizado.
        """
    
    def list(self) -> list[BaseDisk]:
        """Lista todos os discos."""


class InMemoryDiskRepository(BaseDiskRepository):
    def __init__(self):
        self.disks: dict[uuid.UUID, BaseDisk] = {}
    
    def add(self, disk: BaseDisk) -> BaseDisk:
        disk.id = uuid.uuid4()
        self.disks[disk.id] = copy.deepcopy(disk)
        return copy.deepcopy(self.disks[disk.id])

    def remove(self, disk: BaseDisk) -> BaseDisk:
        try:
            self.disks.pop(disk.id)
        except:
            raise DiskDoesNotExistError
    
    def get(self, id: uuid.UUID) -> BaseDisk:
        try:
            return copy.deepcopy(self.disks[id])
        except KeyError:
            raise DiskNotFoundError
    
    def update(self, disk: BaseDisk) -> BaseDisk:
        try:
            disk_ = self.disks[disk.id]
            for attribute, value in vars(disk).items():
                setattr(disk_, attribute, value)
            return copy.deepcopy(disk_)
        except KeyError:
            raise DiskDoesNotExistError

    def list(self) -> list[BaseDisk]:
        return [copy.deepcopy(value) for _, value in self.disks.items()]
