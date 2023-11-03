import requests

url = "https://aes.cryptohack.org/block_cipher_starter/"
r = requests.get(url + 'encrypt_flag/')
cipher_hex = r.json()["31383862633935323238383361393932636439396639623262386563383466623135306331616265313765376138656430346137363861643164313166633037"]
print(cipher_hex)

r = requests.get(url+'decrypt/'+cipher_hex)
pt = r.json()['plaintext']
print(bytes.fromhex(pt))