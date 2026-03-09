"""
Vigenère Cipher:
https://privacycanada.net/classical-encryption/vigenere-cipher/

The code below uses the printable characters seen here:
https://www.ascii-code.com/
"""


def repeat_to_length(s, wanted):
    return (s * (wanted//len(s) + 1))[:wanted]


def encode(text, key):
    text_list = list(text)
    key_list = repeat_to_length(key, len(text_list))
    
    for i in range(len(text_list)):
        text_list[i] = chr((( (ord(text_list[i]) - 32) + ord(key_list[i]) ) % 127) + 32)

    return ''.join(text_list)


def decode(text, key):
    text_list = list(text)
    key_list = repeat_to_length(key, len(text_list))
    
    for i in range(len(text_list)):
        text_list[i] = chr((( (ord(text_list[i]) - 32) - ord(key_list[i]) ) % 127) + 32)

    return ''.join(text_list)


if __name__ == "__main__":

    key = "fun"

    original_text = "The Onion~Knight (shh...) rides at dawn!!"
    print(f"Original: {original_text}")

    encoded = encode(original_text, key)
    print(f"Encoded: {encoded}")

    decoded = decode(encoded, key)
    print(f"Decoded: {decoded}")