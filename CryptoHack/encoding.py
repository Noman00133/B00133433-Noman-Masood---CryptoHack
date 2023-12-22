from pwn import * 
import json
import codecs, base64
from Crypto.Util.number import long_to_bytes

# Connecting to the remote server
r = remote('socket.cryptohack.org', 13377, level = 'debug')

# Receive JSON data from the server
def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

#Send JSON data to the server
def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


# Decode encoded strings related to the encoding type
def decode(encoded_string, encoded_type):
    if encoded_type == "base64":
        return bytes(base64.b64decode(encoded_string)).decode("utf-8")

    elif encoded_type == "hex":
        return bytes(bytes.fromhex(encoded_string)).decode("utf-8")

    elif encoded_type == "rot13":
        return codecs.decode(encoded_string, "rot13")

    elif encoded_type == "utf-8":
        return ''.join(chr(i) for i in encoded_string)

    else:
        return bytes(long_to_bytes(int(encoded_string, 16))).decode("utf-8")


# Go through 100 communication cycles with the server.
for i in range(100):
    print(i)

    # Receive the encoded data from the server
    received = json_recv()
    print("Received type: ", received["type"])
    encoded_type = received["type"]

    print("Received encoded value: ", received["encoded"])
    encoded_string = received["encoded"]


    # Decode the received encoded string
    to_send = {
    "decoded": decode(encoded_string, encoded_type)
}
    # Sending the decoded value to the server
    json_send(to_send)

print(json_recv())

