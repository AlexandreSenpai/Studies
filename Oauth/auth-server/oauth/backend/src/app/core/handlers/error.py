class Error(Exception):
    def __init__(self, 
                 message: str,
                 code: str = 'UNKNOWN',
                 status: int = 500) -> None:
        self.message = message
        self.code = code
        self.status = status

class InvalidResource(Error):
    def __init__(self, 
                 message: str = "Request made with an invalid resource.",
                 code: str = 'INVALID_RESOURCE',
                 status: int = 400) -> None:
        self.message = message
        self.code = code
        self.status = status

class Forbidden(Error):
    def __init__(self, 
                 message: str = "Access Forbidden",
                 code: str = "FORBIDDEN",
                 status=403) -> None:
        super().__init__(message=message,
                         code=code,
                         status=status)

class InvalidCredentials(Error):
    def __init__(self, 
                 message: str = "Invalid credentials",
                 code: str = "INVALID_CREDENTIALS",
                 status=401) -> None:
        super().__init__(message=message,
                         code=code,
                         status=status)

class BadRequest(Error):
    def __init__(self, 
                 message: str = "This request is invalid",
                 code: str = "BAD_REQUEST",
                 status=400) -> None:
        super().__init__(message=message,
                         code=code,
                         status=status)

class Unknown(Error):
    def __init__(self, 
                 message: str = "An unknown error occurred",
                 code: str = "UNKNOWN",
                 status=500) -> None:
        super().__init__(message=message,
                         code=code,
                         status=status)
        
class DatabaseUnavailable(Error):
    def __init__(self,
                 message: str = "The application database is unavailable.",
                 code: str = "DATABASE_ERROR",
                 status=500) -> None:
        super().__init__(message=message,
                         code=code,
                         status=status)
        
class ResourceNotFound(Error):
    def __init__(self,
                message: str = "The application was not able to find an important resource.",
                code: str = "RESOURCE_NOT_FOUND",
                status=404) -> None:
        super().__init__(message=message,
                            code=code,
                            status=status)