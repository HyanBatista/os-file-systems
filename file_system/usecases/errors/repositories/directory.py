class DirectoryNotFoundError(Exception):
    def __init__(self) -> None:
        message: str = "O diretório especificado não foi achado."
        super().__init__(message)


class DirectoryDoesNotExistError(Exception):
    def __init__(self) -> None:
        message: str = "O diretório especificado não existe."
