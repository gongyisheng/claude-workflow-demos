"""Security / cryptography dependencies.

One function per dependency: cryptography, pyjwt (jwt), passlib, bcrypt,
paramiko.
"""

from cryptography.fernet import Fernet
import jwt
from passlib.hash import pbkdf2_sha256
import bcrypt
import paramiko


def fernet_roundtrip(message: str) -> str:
    """cryptography: encrypt then decrypt a message with Fernet."""
    key = Fernet.generate_key()
    f = Fernet(key)
    token = f.encrypt(message.encode())
    return f.decrypt(token).decode()


def encode_jwt(payload: dict, secret: str = "secret") -> str:
    """pyjwt: encode a payload into a signed JWT."""
    return jwt.encode(payload, secret, algorithm="HS256")


def hash_password_passlib(password: str) -> str:
    """passlib: hash a password with PBKDF2-SHA256."""
    return pbkdf2_sha256.hash(password)


def hash_password_bcrypt(password: str) -> bytes:
    """bcrypt: hash a password with bcrypt."""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def build_ssh_client() -> "paramiko.SSHClient":
    """paramiko: build an SSH client (no connection made)."""
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    return client
