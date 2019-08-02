from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import unpad


def aes_decrypt_phone(ciphertext, key: bytes):
    iv = b'0' * 16
    cipher = AES.new(key, AES.MODE_CBC, iv)
    message = cipher.decrypt(ciphertext)
    message = unpad(message, 16)
    return message.decode()


if __name__ == '__main__':
    encode_phone_str = 'be28dea08ee543320b1ef9e1bceb51e4'       # 返回加密手机号
    app_key = 'gywzffojtnzl0vd6kcut8fcgyud5wg49'                # 秘钥

    encode_phone = bytes.fromhex(encode_phone_str)
    phone = aes_decrypt_phone(encode_phone, app_key.encode())
    print(phone)
