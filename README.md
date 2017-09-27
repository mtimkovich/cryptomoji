# Encroji

Encrypt your messages into emoji.

## Usage

Encroji takes ASCII letters as a message to encrypt as well as an emoji passphrase, and outputs an emoji cyphertext.

It can decrypt the message if provided the proper emoji passphrase.

```
encroji.py encrypt

encroji.py decrypt
```

## Implementation

Encroji uses a modified [Vigenère cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher) that has been adjusted to work
to convert emoji to ASCII letters, and vice versa.

|    | 🥇 | 🥈 | 🥉 |
|:--:|:--:|:--:|----|
| 🥇 |  A |  B |  C |
| 🥈 |  B |  C |  D |
| 🥉 |  C |  D |  E |

Is a sample of the Vigenère table that Encroji uses. The columns represent the cyphertext, while the rows represent the passphrase. If
the passphrase isn't as long as the string, the passphrase gets repeated to match the length of the cleartext.

## Installation

```
pip install -r requirements.txt
```

## Disclaimer

This should have to go without saying, but Vigenère ciphers have been able to be cracked since 1863: don't use this for anything important.

## Author

Max Timkovich

## License

Encroji is licensed under the MIT License, see the LICENSE file for more details.
