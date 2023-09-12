class WrongPinException(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class NegativeAmountExceptions(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class InsufficientFundException(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class WrongPasswordException(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class AccountNotFoundException(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class diaryNotFoundException(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class entryNotFoundException(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)

# def design(fn):
#     print("******************************")
#     fn()
#     print("****************************")
#     return fn
#
# @design
# def show(self):
#     print("**********************")
#
#
