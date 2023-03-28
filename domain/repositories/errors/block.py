class BlockNotFoundError(Exception):
    def __init__(self) -> None:
        message: str = "O bloco especificado não foi achado."
        super().__init__(message)


class BlockDoesNotExistError(Exception):
    def __init__(self) -> None:
        message: str = "O bloco especificado não existe."
        super().__init__(message)
