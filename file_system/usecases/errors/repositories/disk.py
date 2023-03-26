class DiskNotFoundError(Exception):
    def __init__(self) -> None:
        message: str = "A memória especificado não foi achado."
        super().__init__(message)


class DiskDoesNotExistError(Exception):
    def __init__(self) -> None:
        message: str = "A memória especificado não existe."
        super().__init__(message)
