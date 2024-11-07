import hashlib

# RSA parameters (for demonstration, replace d and N with actual private key values)
d = <your_private_exponent>
N = <your_modulus>

# The message to sign
message = "crypto{Immut4ble_m3ssag1ng}"

# Step 1: Hash the message using SHA-256
hash_obj = hashlib.sha256(message.encode())
hashed_message = hash_obj.hexdigest()

# Step 2: Convert the hash (in hexadecimal) to an integer
hashed_int = int(hashed_message, 16)

# Step 3: Compute the signature (S = H(m)^d mod N)
signature = pow(hashed_int, d, N)

print("Signature (as integer):", signature)
