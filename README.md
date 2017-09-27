# Cryptomoji

*Encrypt your messages as emoji!*

🐶⛏👩🏼‍⚖️🏇🏿⛎👋🏻🇲🇱🔟🖼🚼💁🏾‍♀️👳🏾

## Usage

Cryptomoji encrypts alphabetical messages into emoji using an emoji passphrase, and can decrypt the message when given
the correct passphrase.

### Encrypt

```
cryptomoji.py encrypt message passphrase

encrypt message

positional arguments:
    message     message to encrypt (must be alphabetical)
    passphrase  passphrase to use (must be emojis)
```

### Decrypt

```
cryptomoji.py decrypt message passphrase

decrypt message

positional arguments:
    message     message to decrypt (must be emojis)
    passphrase  passphrase to use (must be emojis)
```

I highly recommend using quotes around your emoji sentences because as you might expect, the command line doesn't handle emojis very well.

## Implementation

Cryptomoji uses a modified [Vigenère cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher) that has been adjusted
to convert emoji to letters and vice versa.

|    | 🥇 | 🥈 | 🥉 |
|:--:|:--:|:--:|----|
| 🥇 |  A |  B |  C |
| 🥈 |  B |  C |  D |
| 🥉 |  C |  D |  E |

This is a sample of the Vigenère table that Cryptomoji uses. The columns represent the cyphertext, while the rows represent the passphrase. If
the passphrase is shorter than the message, the passphrase gets repeated to match the length of the message.

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
