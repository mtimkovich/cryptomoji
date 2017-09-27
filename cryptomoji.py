#!/usr/bin/env python3
import argparse
import emoji
import itertools
import random

emoji_list = sorted(emoji.EMOJI_UNICODE.items())


def emoji_ord(emoji):
    for i, e in enumerate(emoji_list):
        if e[1] == emoji:
            return i


def ord_emoji(n):
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

    z = 26 * random.randint(lo, hi) + c - p
    return z


def encrypt(cleartext, passphrase):
    """
    cleartext (letters) - phrase to be encrypted
    passphrase (emojis) - emoji passphrase

    returns: message encrypted as emojis
    """

    cypher = ''

    for c, p in zip(cleartext, itertools.cycle(passphrase)):
        letter = ord(c) - 97
        emoji = emoji_ord(p)

        print(letter, emoji)

        cyphermoji = encrypt_char(letter, emoji)
        cypher += ord_emoji(cyphermoji)[1]

    return cypher


def decrypt(cypher, passphrase):
    """
    cypher (emojis) - encrypted emoji message
    passphrase (emojis) - emoji passphrase

    returns: message in cleartext
    """

    output = ''

    demoji = emoji.demojize(cypher)
    cypher_emojis = [':{}:'.format(e) for e in demoji.split(':') if e]

    for c, p in zip(cypher_emojis, itertools.cycle(passphrase)):
        cyphermoji = emoji_ord(emoji.emojize(c))
        passmoji = emoji_ord(p)

        print(cyphermoji, passmoji)

        clear_char = decrypt_char(cyphermoji, passmoji)
        output += chr(clear_char + 97)

    return output


# parser = argparse.ArgumentParser(description='Encrypt into emojis')

cypher = encrypt('hello', '🤔')
print(cypher)

print()

clear = decrypt(cypher, '🤔')
print(clear)
