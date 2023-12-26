# Hexadecimal values for encryption keys
KEY1 = bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
KEY2_KEY1 = bytes.fromhex('37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e')
KEY2_KEY3 = bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')
FLAG_KEY = bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')

# Combining KEY1, KEY2_KEY3 through bitwise XOR to get KEY1_KEY2_KEY3 
KEY1_KEY2_KEY3 = bytes(KEY1[i] ^ KEY2_KEY3[i] for i in range(len(KEY1)))

# Decrypting the flag by XORing KEY1_KEY2_KEY3 with the encrypted flag
decrypted_flag = bytes(KEY1_KEY2_KEY3[i] ^ FLAG_KEY[i] for i in range(len(KEY1_KEY2_KEY3)))

# Print the flag
print(decrypted_flag.decode('utf-8'))
