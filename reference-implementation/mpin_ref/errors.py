class MPINError(Exception):
    """Base error for the reference implementation."""


class AuthorityError(MPINError):
    pass


class SessionError(MPINError):
    pass


class FriendFolderError(MPINError):
    pass


class ValidationError(MPINError):
    pass
