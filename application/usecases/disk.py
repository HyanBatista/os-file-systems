from domain.entities.disk import BaseDisk
from domain.entities.block import BaseBlock, registry as block_registry
from domain.repositories.disk import BaseDiskRepository


class CreateDisk:
    def __init__(self, repository: BaseDiskRepository) -> None:
        self.repository = repository

    def __call__(self, block_type: str, block_size: int, number_blocks: int) -> BaseDisk:
        blocks = self._create_blocks(block_type, block_size, number_blocks)
        disk = self._create_disk(blocks)
        self.repository.add(disk)
        return disk

    def _create_disk(self, blocks: list[BaseBlock]) -> BaseDisk:
        """Create the disk.

        Args:
            blocks (list[BaseBlock]): Lista dos blocos do disco.
        """

        disk = BaseDisk(size=(len(blocks) * blocks[0].size), blocks=blocks)
        return disk

    def _create_blocks(
        self, block_type: str, block_size: int, number_blocks: int
    ) -> list[BaseBlock]:
        """Creates the disk blocks.

        Args:
            block_type (str): O tipo do bloco.
            block_size (int): O tamanho do bloco em megabytes.
            number_blocks (int): O número de blocos.
        """

        blocks = []
        factory = block_registry.get_factory(block_type)
        for _ in range(number_blocks):
            block = factory(id=(len(blocks) + 1), size=block_size)
            blocks.append(block)
        return blocks


class ListDisks:
    def __init__(self, repository: BaseDiskRepository) -> None:
        self.repository = repository

    def __call__(self) -> list[BaseDisk]:
        return self.repository.list()
