import os
import arithmetic

class Encryptor:
    def __init__(self,password:str):
        msg=self.string_to_int(password)

    def string_to_int(text: str) :
        return int.from_bytes(text.encode('utf-8'), byteorder='big')

    def int_to_string(number: int) :
        length = (number.bit_length() + 7) // 8
        return number.to_bytes(length, byteorder='big').decode('utf-8')
