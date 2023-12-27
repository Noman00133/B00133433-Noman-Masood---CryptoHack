# Convert the hex-encoded sting to bytes
ciphertext = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')

# Go through each possible value for the XOR key, from 0 to 255.
for i in range(256) :
    # xor all of the ciphertexts bytes with key "i", and put the outcome into a string.
    result = "".join(chr(byte ^ i) for byte in ciphertext)
    
    # check if the result string contains "crypto{"
    if('crypto{' in result):
        # if so, it will print the result
        print(result)