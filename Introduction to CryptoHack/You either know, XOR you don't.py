from itertools import cycle

# Hex string that needs to be decoded
encoded = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')

# The known start of the flag
flag_start = 'crypto{'

# Decrypt the first part of the encoded message to find part of the key
key = [encoded[i] ^ ord(c) for i, c in enumerate(flag_start)]
print('Decrypted key part:', ''.join(chr(i) for i in key))

# We need to add the character 'y' to complete the key, making it "myXORkey"
key.append(ord('y'))
print('Complete key:', ''.join(chr(i) for i in key))

# Decrypt the entire encoded message using the complete key
# cycle(key) is used to repeat the key for the length of the encoded message
solution = ''.join(chr(k ^ e) for k, e in zip(cycle(key), encoded))
print('Solution:', solution)
