cipher1 = '4fd098298db95b7f1bc205b0a6d8ac15f1f821d72fbfa979d1c2148a24feaafdee8d3108e8ce29c3ce1291'
cipher2 = '41d9806ec1b55c78258703be87ac9e06edb7369133b1d67ac0960d8632cfb7f2e7974e0ff3c536c1871b'
plain_text_1 = "hey let's rob the bank at midnight tonight!"
plain_text_2 = ''

cipher1_bytes = bytes.fromhex(cipher1)
cipher1_decimals = []
for byte in cipher1_bytes:
    cipher1_decimals.append(byte)

plain_text_1_decimals = []
for letter in plain_text_1:
    plain_text_1_decimals.append(ord(letter))

key = [cipher1_decimals[i] ^ plain_text_1_decimals[i] for i in range(0, len(plain_text_1_decimals))]

cipher2_bytes = bytes.fromhex(cipher2)
cipher2_decimals = []
for byte in cipher2_bytes:
    cipher2_decimals.append(byte)

for i in range(0, len(cipher2_decimals)):
    plain_text_2 += chr(cipher2_decimals[i]^key[i])

print(plain_text_2)