from typing import TypedDict

class FirebaseLoginSuccess(TypedDict):
    kind: str
    localId: str
    email: str
    displayName: str
    idToken: str
    registered: bool
    refreshToken: str
    expiresIn: str