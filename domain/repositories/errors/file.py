class FileNotFoundError(Exception):
    def __init__(self) -> None:
        message: str = "O arquivo especificado não foi achado."
        super().__init__(message)


class FileDoesNotExistError(Exception):
    def __init__(self) -> None:
        message: str = "O arquivo especificado não existe."
        super().__init__(message)


class DirectoryNotFoundError(FileNotFoundError):
    def __init__(self) -> None:
        message: str = "O diretório especificado não foi achado."
        super().__init__(message)


class DirectoryDoesNotExistError(FileDoesNotExistError):
    def __init__(self) -> None:
        message: str = "O diretório especificado não existe."
        super().__init__(message)
