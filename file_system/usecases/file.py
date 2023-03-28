from file_system.entities.file import BaseDirectory, BaseFile
from file_system.usecases.ports.repositories.file import (
    BaseDirectoryRepository,
    BaseFileRepository,
)


class CreateDirectory:
    def __init__(self, repository: BaseDirectoryRepository) -> None:
        self.repository = repository

    def __call__(self, name: str) -> BaseDirectory:
        directory = BaseDirectory(name=name, size=0)
        directory = self.repository.add(directory)
        return directory


class RemoveDirectory:
    def __init__(self, repository: BaseDirectoryRepository) -> None:
        self.repository = repository

    def __call__(self, name: str) -> BaseDirectory:
        directory = self.repository.get(name)
        directory = self.repository.remove(directory)
        return directory


class ListDirectories:
    def __init__(self, repository: BaseDirectoryRepository) -> None:
        self.repository = repository

    def __call__(self) -> list[BaseDirectory]:
        return self.repository.list()


class CreateFile:
    def __init__(self, repository: BaseFileRepository) -> None:
        self.repository = repository

    def __call__(self, name: str, size: int) -> BaseFile:
        file = BaseFile(name=name, size=size)
        return file


class RemoveFile:
    def __init__(self, repository: BaseFileRepository) -> None:
        self.repository = repository

    def __call__(self, name: str) -> BaseFile:
        file = self.repository.get(name)
        file = self.repository.remove(file)
        return file
