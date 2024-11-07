#This code will take the hex string convert them to byte and apply Xor to them, and convert the flag to string
def xor_bytes(b1, b2):
    return bytes([x ^ y for x, y in zip(b1, b2)])

# Hex strings
key1_hex = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
key2_xor_key1_hex = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
key2_xor_key3_hex = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
flag_xor_key1_key3_key2_hex = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

# Convert hex to bytes
key1 = bytes.fromhex(key1_hex)
key2_xor_key1 = bytes.fromhex(key2_xor_key1_hex)
key2_xor_key3 = bytes.fromhex(key2_xor_key3_hex)
flag_xor_key1_key3_key2 = bytes.fromhex(flag_xor_key1_key3_key2_hex)

# Find KEY2
key2 = xor_bytes(key2_xor_key1, key1)

# Find KEY3
key3 = xor_bytes(key2_xor_key3, key2)

# Find FLAG
flag = xor_bytes(flag_xor_key1_key3_key2, xor_bytes(key1, xor_bytes(key2, key3)))

# Convert FLAG to string
flag_string = flag.decode('utf-8')

print(f"The flag is: {flag_string}")
