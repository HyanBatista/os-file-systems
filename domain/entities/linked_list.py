import abc
from domain.entities.block import BaseBlock


class BaseLinkedList(abc.ABC):
    @abc.abstractmethod
    def append(self):
        pass

    @abc.abstractmethod
    def prepend(self):
        pass

    @abc.abstractmethod
    def delete(self):
        pass

    @abc.abstractmethod
    def to_list(self):
        pass


class BaseBlockLinkedList(BaseLinkedList):
    @abc.abstractmethod
    def append(self, block: BaseBlock):
        pass

    @abc.abstractmethod
    def prepend(self, block: BaseBlock):
        pass

    @abc.abstractmethod
    def delete(self, block: BaseBlock):
        pass

    @abc.abstractmethod
    def to_list(self):
        pass


class BlockLinkedList(BaseBlockLinkedList):
    def __init__(self) -> None:
        self.head = None

    def append(self, block: BaseBlock):
        if self.head is None:
            self.head = block
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = block

    def prepend(self, block: BaseBlock):
        block.next = self.head
        self.head = block

    def delete(self, block: BaseBlock):
        if self.head is None:
            return

        if self.head.id == block.id:
            self.head = self.head.next
            return

        current = self.head

        while current.next is not None:
            if current.next.id == block.id:
                current.next = current.next.next
                return
            current = current.next

    def to_list(self):
        blocks = []
        current = self.head
        while current.next is not None:
            blocks.append(current.next)
            current = current.next
        return blocks
