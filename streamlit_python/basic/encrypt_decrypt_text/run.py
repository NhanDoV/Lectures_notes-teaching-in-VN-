import streamlit as st
from helper import *

# Page config
st.set_page_config(page_title="Encrypt + Decrypt text", layout="wide")

# data dictionary
data_dict = {

    "Level 0": {
        "Title": "Permutation cipher",
        "Description": "Shuffle characters using seeded pseudo-random permutation",
        "security_power": "Very weak",
        "Pros": "Simple, fast",
        "Cons": "Not cryptographically secure"
    },

    "Level 1": {
        "Title": "Substitution cipher",
        "Description": "Replace characters via secret alphabet permutation",
        "security_power": "Weak",
        "Pros": "Hides positions",
        "Cons": "Frequency analysis breaks it"
    },

    "Level 2": {
        "Title": "Vigenère cipher",
        "Description": "Polyalphabetic shift using repeating key",
        "security_power": "Weak",
        "Pros": "Better than substitution",
        "Cons": "Breakable with known plaintext"
    },

    "Level 3": {
        "Title": "XOR cipher",
        "Description": "Encrypt data using XOR with repeating key",
        "security_power": "Medium",
        "Pros": "Fast, simple",
        "Cons": "Key reuse is fatal"
    },

    "Level 4": {
        "Title": "Stream cipher (weak PRNG)",
        "Description": "XOR with pseudo-random keystream",
        "security_power": "Medium",
        "Pros": "Hides patterns",
        "Cons": "PRNG predictable"
    },

    "Level 5": {
        "Title": "One-Time Pad",
        "Description": "XOR with truly random key of equal length",
        "security_power": "Perfect (theoretical)",
        "Pros": "Provably secure",
        "Cons": "Key management impossible"
    },

    "Level 6": {
        "Title": "Password-based encryption",
        "Description": "Key derived from password",
        "security_power": "Strong",
        "Pros": "User-friendly",
        "Cons": "Weak passwords = weak security"
    },

    "Level 7": {
        "Title": "AES-GCM",
        "Description": "Authenticated symmetric encryption",
        "security_power": "Very strong",
        "Pros": "Industry standard",
        "Cons": "Key management required"
    },

    "Level 8": {
        "Title": "Hybrid encryption (RSA + AES)",
        "Description": "AES for data, RSA for key exchange",
        "security_power": "Very strong",
        "Pros": "Scales securely",
        "Cons": "More complex architecture"
    }
}

# method registry with respect to its params
METHOD_REGISTRY = {
    "Level 0": {
        "encrypt": encrypt_shuffle,
        "decrypt": decrypt_shuffle,
        "params": [
            {"name": "key", "type": "int", "label": "Random Seed"}
        ]
    },

    "Level 1": {
        "encrypt": encrypt_substitution,
        "decrypt": decrypt_substitution,
        "params": [
            {"name": "key", "type": "str", "label": "Secret Key"}
        ]
    },

    "Level 2": {
        "encrypt": encrypt_vigenere,
        "decrypt": decrypt_vigenere,
        "params": [
            {"name": "key", "type": "str", "label": "Vigenère Key"}
        ]
    },

    "Level 3": {
        "encrypt": xor_cipher,
        "decrypt": xor_cipher,
        "params": [
            {"name": "key", "type": "bytes", "label": "XOR Key"}
        ]
    },

    "Level 4": {
        "encrypt": encrypt_stream_weak,
        "decrypt": decrypt_stream_weak,
        "params": [
            {"name": "seed", "type": "int", "label": "PRNG Seed"}
        ]
    },

    "Level 5": {
        "encrypt": otp_encrypt,
        "decrypt": otp_decrypt,
        "params": [
            {"name": "key", "type": "bytes", "label": "OTP Key (same length!)"}
        ]
    },

    "Level 6": {
        "encrypt": encrypt_password_based,
        "decrypt": decrypt_password_based,
        "params": [
            {"name": "password", "type": "str", "label": "Password"}
        ]
    },

    "Level 7": {
        "encrypt": encrypt_aes_gcm,
        "decrypt": decrypt_aes_gcm,
        "params": [
            {"name": "key", "type": "bytes", "label": "AES Key (16/24/32 bytes)"}
        ]
    },
}\

c1, c2, c3 = st.columns([7, 3, 6])
with c1:
    summaries = """
                    ### 🔐 Encryption Methods — Security Overview

                    | Level | Method                          | Security |
                    |------:|---------------------------------|----------|
                    | 0     | Shuffle permutation             | ❌ |
                    | 1     | Substitution                    | ❌ |
                    | 2     | Vigenère                        | ❌ |
                    | 3     | XOR                             | ⚠️ |
                    | 4     | Stream cipher (weak PRNG)       | ⚠️ |
                    | 5     | One-Time Pad                    | 🔐 (theoretical) |
                    | 6     | Password-based crypto           | 🔐🔐 |
                    | 7     | AES-GCM                         | 🔐🔐🔐 |
                    | 8     | RSA + AES                       | 🔐🔐🔐🔐 |
                """
    st.write(summaries)

with c2:
    st.header("Selection")

    # select the complexity security level
    sel_level = st.selectbox("Chọn mức độ:", 
                              list(data_dict.keys()),
                              help = "Level càng cao bảo mật càng tốt"
                            )
    
    # select encrypt or decrypt method
    encrt_or_decrt = st.selectbox("Encrypt or Decrypt", 
                                    ["Encrypt", "Decrypt"]
                                )
    
    input_string = st.text_input("Nhập đoạn text ở đây")

    # Khai báo params
    params = {}
    method_conf = METHOD_REGISTRY[sel_level]

    for p in method_conf["params"]:
        if p["type"] == "int":
            params[p["name"]] = st.number_input(p["label"], step=1)
        elif p["type"] == "str":
            params[p["name"]] = st.text_input(p["label"])
        elif p["type"] == "bytes":
            params[p["name"]] = st.text_input(p["label"]).encode()

with c3:
    st.header("Description")
    st.write(data_dict[sel_level]["Description"])

    # Logic of encrypt / decrypt function with respect to input-params
    func = method_conf["encrypt"] if encrt_or_decrt == "Encrypt" else method_conf["decrypt"]

    if st.button("Run"):
        try:
            result = func(input_string, **params)
            st.success("Done!")
            st.code(result)
        except Exception as e:
            st.error(str(e))