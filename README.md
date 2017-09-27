# Cryptomoji

*Encrypt your messages into emoji!*

## Usage

Cryptomoji encrypts alphabetical messages into emoji using an emoji passphrase, and can decrypt the message when given
the correct passphrase.

```bash
cryptomoji.py encrypt

cryptomoji.py decrypt
```

## Implementation

cryptomoji uses a modified [Vigenère cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher) that has been adjusted to work
to convert emoji to ASCII letters and vice versa.

|    | 🥇 | 🥈 | 🥉 |
|:--:|:--:|:--:|----|
| 🥇 |  A |  B |  C |
| 🥈 |  B |  C |  D |
| 🥉 |  C |  D |  E |

This is a sample of the Vigenère table that cryptomoji uses. The columns represent the cyphertext, while the rows represent the passphrase. If
the passphrase isn't as long as the string, the passphrase gets repeated to match the length of the plaintext.

## Installation

```bash
pip install -r requirements.txt
```

## Disclaimer

This should have to go without saying, but Vigenère ciphers have been crackable since 1863: don't use this for anything important.

## Author

Max Timkovich

## License

Cryptomoji is licensed under the MIT License, see the LICENSE file for more details.
