import random
import string
import os
from hashlib import sha256

# ======================== LEVEL 0. Permutation cipher =================================== #
def encrypt_shuffle(s, key):
    idx = list(range(len(s)))
    random.seed(key)
    random.shuffle(idx)
    return ''.join(s[i] for i in idx), idx


def decrypt_shuffle(cipher, idx):
    res = [''] * len(cipher)
    for i, j in enumerate(idx):
        res[j] = cipher[i]
    return ''.join(res)


# ======================= LEVEL 1. Substitution cipher ===================================== #
def encrypt_substitution(s, key):
    random.seed(key)
    alphabet = string.printable
    shuffled = list(alphabet)
    random.shuffle(shuffled)
    table = dict(zip(alphabet, shuffled))
    return ''.join(table[c] for c in s)


def decrypt_substitution(cipher, key):
    random.seed(key)
    alphabet = string.printable
    shuffled = list(alphabet)
    random.shuffle(shuffled)
    table = dict(zip(shuffled, alphabet))
    return ''.join(table[c] for c in cipher)


# ======================== LEVEL 2. Vigenère cipher ======================================= #
def encrypt_vigenere(s, key):
    return ''.join(
        chr((ord(c) + ord(key[i % len(key)])) % 256)
        for i, c in enumerate(s)
    )


def decrypt_vigenere(c, key):
    return ''.join(
        chr((ord(ch) - ord(key[i % len(key)])) % 256)
        for i, ch in enumerate(c)
    )


# ======================== LEVEL 3. XOR cipher ============================================= #
def xor_cipher(data: bytes, key: bytes) -> bytes:
    return bytes(d ^ key[i % len(key)] for i, d in enumerate(data))


# ======================== LEVEL 4. XOR + weak PRNG ======================================== #
def encrypt_stream_weak(data: bytes, seed: int) -> bytes:
    rnd = random.Random(seed)
    return bytes(b ^ rnd.getrandbits(8) for b in data)


def decrypt_stream_weak(cipher: bytes, seed: int) -> bytes:
    return encrypt_stream_weak(cipher, seed)


# ======================== LEVEL 5. One-Time Pad =========================================== #
def otp_encrypt(data: bytes, key: bytes) -> bytes:
    assert len(data) == len(key)
    return bytes(d ^ k for d, k in zip(data, key))


def otp_decrypt(cipher: bytes, key: bytes) -> bytes:
    return otp_encrypt(cipher, key)


# ======================== LEVEL 6. Password-based XOR (toy KDF) =========================== #
def derive_key_from_password(password: str, length: int) -> bytes:
    digest = sha256(password.encode()).digest()
    return (digest * (length // len(digest) + 1))[:length]


def encrypt_password_based(data: bytes, password: str) -> bytes:
    key = derive_key_from_password(password, len(data))
    return xor_cipher(data, key)


def decrypt_password_based(cipher: bytes, password: str) -> bytes:
    return encrypt_password_based(cipher, password)


# ======================== LEVEL 7. AES-GCM (real crypto) ================================= #
# Requires: pip install cryptography
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def encrypt_aes_gcm(data: bytes, key: bytes) -> bytes:
    aes = AESGCM(key)
    nonce = os.urandom(12)
    return nonce + aes.encrypt(nonce, data, None)


def decrypt_aes_gcm(cipher: bytes, key: bytes) -> bytes:
    nonce, ct = cipher[:12], cipher[12:]
    aes = AESGCM(key)
    return aes.decrypt(nonce, ct, None)


# ======================== LEVEL 8. Hybrid idea (AES + RSA placeholder) =================== #
"""
    Level 8 is conceptual here:
    - Generate random AES key
    - Encrypt data with AES
    - Encrypt AES key with RSA public key
    (Implementation usually separated into key & message layers)
"""