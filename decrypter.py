import os
import pyaes

# abrir o arquivo encriptografado

file_name = 'teste.txt.ransomwaretroll'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

# chave de descriptografia

key = b'testeransonwares'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

# remover o arquivo criptografado

os.remove(file_name)

# criar um novo arquivo desccriptografado

new_file = 'teste.txt'
new_file = open(new_file, 'wb')
new_file.write(decrypt_data)
new_file.close