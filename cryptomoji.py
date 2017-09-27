#!/usr/bin/env python
import argparse
import emoji
import itertools
import random
import re
import sys

emoji_list = sorted(emoji.EMOJI_UNICODE.items())


def emoji_ord(emoji):
    """ Get emoji's index """
    for i, e in enumerate(emoji_list):
        if e[1] == emoji:
            return i


def ord_emoji(n):
    """ Get emoji from its index """
    for i, e in enumerate(emoji_list):
        if i == n:
            return e


def decrypt_char(z, p):
    c = (z + p) % 26
    return c


def encrypt_char(c, p):
    lo = -1
    hi = -1
    n = 0

    while True:
        z = 26 * n + c - p

        if lo < 0 and z > 0:
            lo = n

        if z > len(emoji_list):
            hi = n - 1
            break

        n += 1

    return 26 * random.randint(lo, hi) + c - p


def emoji_split(text):
    demoji = emoji.demojize(text)
    return [emoji.emojize(':{}:'.format(e)) for e in demoji.split(':') if e]


def encrypt(cleartext, passphrase):
    """
    cleartext (letters) - phrase to be encrypted
    passphrase (emojis) - emoji passphrase

    returns: message encrypted as emojis
    """

    cypher = ''

    for c, p in zip(cleartext, itertools.cycle(emoji_split(passphrase))):
        letter = ord(c) - 97
        emoji_val = emoji_ord(p)

        cyphermoji = encrypt_char(letter, emoji_val)
        cypher += ord_emoji(cyphermoji)[1]

    return cypher


def decrypt(cypher, passphrase):
    """
    cypher (emojis) - encrypted emoji message
    passphrase (emojis) - emoji passphrase

    returns: message in cleartext
    """

    output = ''

    for c, p in zip(emoji_split(cypher),
                    itertools.cycle(emoji_split(passphrase))):
        cyphermoji = emoji_ord(c)
        passmoji = emoji_ord(p)

        clear_char = decrypt_char(cyphermoji, passmoji)
        output += chr(clear_char + 97)

    return output


def clean_msg(text):
    text = text.lower()
    return re.sub('[^a-z]+', '', text)


parser = argparse.ArgumentParser(description='Encrypt into emojis')
parser.add_argument('command', help='encrypt or decrypt')
args = parser.parse_args(sys.argv[1:2])

if args.command == 'encrypt':
    parser = argparse.ArgumentParser(description='encrypt message')
    parser.add_argument('message',
                        help='message to encrypt (must be alphabetical)')
    parser.add_argument('passphrase',
                        help='passphrase to use (must be emojis)')
    args = parser.parse_args(sys.argv[2:])

    message = clean_msg(args.message)

    cypher = encrypt(message, args.passphrase)
    print(cypher)

elif args.command == 'decrypt':
    parser = argparse.ArgumentParser(description='decrypt message')
    parser.add_argument('message',
                        help='message to decrypt (must be emojis)')
    parser.add_argument('passphrase',
                        help='passphrase to use (must be emojis)')
    args = parser.parse_args(sys.argv[2:])

    plaintext = decrypt(args.message, args.passphrase)
    print(plaintext)

else:
    print('Unrecognized command')
    parser.print_help()
    sys.exit(1)
