from domain.entities.file import BaseLinkedFile
from domain.entities.linked_list import BaseBlockLinkedList
from domain.repositories.file import (
    BaseFileRepository,
)

class CreateLinkedFile:
    def __init__(self, repository: BaseFileRepository) -> None:
        self.repository = repository

    def __call__(self, name, size, type, blocks: BaseBlockLinkedList) -> BaseLinkedFile:
        
        file = BaseLinkedFile(name, size, blocks)
