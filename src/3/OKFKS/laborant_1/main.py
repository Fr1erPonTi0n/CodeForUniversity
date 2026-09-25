from hashlib import sha256

data = ["e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"]


def hashlib_sha_256(line: bytes) -> str:
    return sha256(line).hexdigest()


def _right_rotate(val, amount):
    # Циклически сдвигает 32-битное число вправо
    return ((val >> amount) | (val << (32 - amount))) & 0xFFFFFFFF


def my_sha_256(line: bytes) -> str:
    # Инициализация констант (первые 32 бита дробных частей квадратных корней первых 64 простых чисел)
    k = [
        0x428A2F98, 0x71374491, 0xB5C0FBCF, 0xE9B5DBA5, 0x3956C25B, 0x59F111F1, 0x923F82A4, 0xAB1C5ED5,
        0xD807AA98, 0x12835B01, 0x243185BE, 0x550C7DC3, 0x72BE5D74, 0x80DEB1FE, 0x9BDC06A7, 0xC19BF174,
        0xE49B69C1, 0xEFBE4786, 0x0FC19DC6, 0x240CA1CC, 0x2DE92C6F, 0x4A7484AA, 0x5CB0A9DC, 0x76F988DA,
        0x983E5152, 0xA831C66D, 0xB00327C8, 0xBF597FC7, 0xC6E00BF3, 0xD5A79147, 0x06CA6351, 0x14292967,
        0x27B70A85, 0x2E1B2138, 0x4D2C6DFC, 0x53380D13, 0x650A7354, 0x766A0ABB, 0x81C2C92E, 0x92722C85,
        0xA2BFE8A1, 0xA81A664B, 0xC24B8B70, 0xC76C51A3, 0xD192E819, 0xD6990624, 0xF40E3585, 0x106AA070,
        0x19A4C116, 0x1E376C08, 0x2748774C, 0x34B0BCB5, 0x391C0CB3, 0x4ED8AA4A, 0x5B9CCA4F, 0x682E6FF3,
        0x748F82EE, 0x78A5636F, 0x84C87814, 0x8CC70208, 0x90BEFFFA, 0xA4506CEB, 0xBEF9A3F7, 0xC67178F2
    ]

    # Инициализация хеш-значений (первые 32 бита дробных частей квадратных корней первых 8 простых чисел)
    h = [
        0x6A09E667, 0xBB67AE85, 0x3C6EF372, 0xA54FF53A,
        0x510E527F, 0x9B05688C, 0x1F83D9AB, 0x5BE0CD19
    ]

    # 1. Дополнительное сообщение (Padding)
    bit_length = len(line) * 8
    line += b'\x80'
    while (len(line) * 8 + 64) % 512 != 0:
        line += b'\x00'
    line += bit_length.to_bytes(8, 'big')

    # 2. Обработка сообщения блоками по 512 бит (64 бита)
    for i in range(0, len(line), 64):
        chunk = line[i:i + 64]
        w = list(chunk[j:j + 4] for j in range(0, 64, 4))
        w = [int.from_bytes(word, 'big') for word in w]

        for j in range(16, 64):
            s0 = _right_rotate(w[j - 15], 7) ^ _right_rotate(w[j - 15], 18) ^ (w[j - 15] >> 3)
            s1 = _right_rotate(w[j - 2], 17) ^ _right_rotate(w[j - 2], 19) ^ (w[j - 2] >> 10)
            w.append((w[j - 16] + s0 + w[j - 7] + s1) & 0xFFFFFFFF)

        a, b, c, d, e, f, g, h_val = h

        for j in range(64):
            s1 = _right_rotate(e, 6) ^ _right_rotate(e, 11) ^ _right_rotate(e, 25)
            ch = (e & f) ^ (~e & g)
            temp1 = (h_val + s1 + ch + k[j] + w[j]) & 0xFFFFFFFF
            s0 = _right_rotate(a, 2) ^ _right_rotate(a, 13) ^ _right_rotate(a, 22)
            maj = (a & b) ^ (a & c) ^ (b & c)
            temp2 = (s0 + maj) & 0xFFFFFFFF

            h_val = g
            g = f
            f = e
            e = (d + temp1) & 0xFFFFFFFF
            d = c
            c = b
            b = a
            a = (temp1 + temp2) & 0xFFFFFFFF

        h[0] = (h[0] + a) & 0xFFFFFFFF
        h[1] = (h[1] + b) & 0xFFFFFFFF
        h[2] = (h[2] + c) & 0xFFFFFFFF
        h[3] = (h[3] + d) & 0xFFFFFFFF
        h[4] = (h[4] + e) & 0xFFFFFFFF
        h[5] = (h[5] + f) & 0xFFFFFFFF
        h[6] = (h[6] + g) & 0xFFFFFFFF
        h[7] = (h[7] + h_val) & 0xFFFFFFFF

    return ''.join(f'{val:08x}' for val in h)


if __name__ == "__main__":
    test_messages = [
        b"",
        b"abc",
        b"Proizvol sydbui",
    ]

    for i, message in enumerate(test_messages):
        hashlib_result = hashlib_sha_256(message)
        my_result = my_sha_256(message)

        print(f"Сообщение: {message.decode('utf-8')!r}")
        print(f"SHA-256 hashlib: {hashlib_result}")
        print(f"SHA-256 моя реализация: {my_result}")
        if i < len(data):
            print(f"Совпадает ли hashlib с data: {i < len(data) and hashlib_result == data[i]}")
            print(f"Совпадает ли моя реализация с data: {i < len(data) and my_result == data[i]}")
        print(f"Совпадают: {hashlib_result == my_result}")
        print()
