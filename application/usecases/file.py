from domain.entities.file import BaseLinkedFile, linked_file_registry
from domain.entities.linked_list import BaseBlockLinkedList
from domain.repositories.file import (
    BaseFileRepository,
)


class CreateLinkedFile:
    def __init__(self, repository: BaseFileRepository) -> None:
        self.repository = repository

    def __call__(
        self,
        name: str,
        size: int,
        type: str,
        blocks: BaseBlockLinkedList,
        parent: BaseLinkedFile = [],
        children: list[BaseLinkedFile] = [],
    ) -> BaseLinkedFile:
        factory = linked_file_registry.get_factory(type)

        file = factory(name=name, size=size, parent=None, children=children)
        file.blocks = blocks
        self.repository.add(file)

        if parent:
            parent_ = self.repository.get(parent)
            file.parent = parent_
            parent_.children.append(file)
            self.repository.update(parent_)

        return file


class ListLinkedFiles:
    def __init__(self, repository: BaseFileRepository) -> None:
        self.repository = repository

    def __call__(self) -> list[BaseLinkedFile]:
        return self.repository.list()


class RemoveLinkedFile:
    def __init__(self, repository: BaseFileRepository) -> None:
        self.repository = repository

    def __call__(self, name: str) -> BaseLinkedFile:
        file = self.repository.get(name)
        file = self.repository.remove(file)
        return file
