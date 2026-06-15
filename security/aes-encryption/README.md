# AES from Scratch

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-matrix%20ops-013243?logo=numpy&logoColor=white)](https://numpy.org/)
![Scope](https://img.shields.io/badge/scope-educational-blue)

A from-scratch implementation of the **Advanced Encryption Standard (AES)** round
transformations and key schedule — written to *understand how AES actually works*
under the hood, byte by byte, rather than to call a library.

> **Educational only.** This is a learning exercise. Never roll your own crypto
> for real systems — use a vetted library like [`cryptography`](https://cryptography.io/).
> This implementation covers a single demonstration round, not the full 10-round
> cipher, and is not constant-time or otherwise hardened.

## What's implemented

AES treats a 128-bit block as a 4×4 matrix of bytes (the *state*) and scrambles
it through a sequence of reversible transformations. Each one is built here from
first principles:

| Step | What it does | File |
|------|--------------|------|
| **AddRoundKey** | XORs the state with a round subkey | [`src/aes/helpers.py`](src/aes/helpers.py) |
| **SubBytes** | Non-linear byte substitution via the AES S-box | [`src/aes/subBytes.py`](src/aes/subBytes.py) |
| **ShiftRows** | Cyclically shifts the rows of the state | [`src/aes/shiftRows.py`](src/aes/shiftRows.py) |
| **MixColumns** | Mixes each column via multiplication in GF(2⁸) | [`src/aes/mixColumns.py`](src/aes/mixColumns.py) |
| **Key schedule** | Expands the cipher key into round subkeys (RotWord, SubWord, Rcon) | [`src/aes_key_schedule.py`](src/aes_key_schedule.py) |

The trickiest part is **MixColumns**, which requires multiplying bytes as
polynomials in the Galois field GF(2⁸) — implemented by hand in `gf_mul`.

## Running it

```bash
pip install -r requirements.txt

# 1) Step-by-step trace of one AES round (writes data/result.txt)
PYTHONPATH=src python src/main.py

# 2) Encrypt a message from the command line
PYTHONPATH=src python src/aes_encrypt.py "Hello World AES!"
# -> Ciphertext: c609f6eed54be68f7c9fd5e8efe3f298
```

`PYTHONPATH=src` puts the `aes` and `utils` packages on the import path while
keeping the `data/` paths relative to the project root.

## Project layout

```
aes-encryption/
├── src/
│   ├── main.py              # narrated walk through one full round
│   ├── aes_encrypt.py       # CLI: encrypt a message block by block
│   ├── aes_key_schedule.py  # key expansion (RotWord, SubWord, Rcon, S-box)
│   ├── aes/                 # the four round transformations
│   └── utils/               # I/O and ASCII/hex conversion helpers
├── data/                    # sample plaintext, subkeys, and outputs
└── docs/report.pdf          # detailed write-up of the implementation
```

## Notes

See [`docs/report.pdf`](docs/report.pdf) for a deeper walk-through of the state
transformations and the subkey schedule, with worked examples.

*Originally a university security assignment, cleaned up and documented. A small
numpy-2.x overflow bug in the GF(2⁸) multiply was fixed so it runs on modern
NumPy.*
