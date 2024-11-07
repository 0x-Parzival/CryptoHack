# Hex encoded string that needs to be decoded
string = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

# Convert the hex string to a list of ordinal (integer) values
string_ord = [o for o in bytes.fromhex(string)]

# Iterate through all possible single-byte keys (0-255)
for order in range(256):
    # XOR each byte of the original message with the current key
    possible_flag_ord = [order ^ o for o in string_ord]
    
    # Convert the resulting list of ordinal values back to a string
    possible_flag = "".join(chr(o) for o in possible_flag_ord)
    
    # Check if the decoded string starts with "crypto"
    if possible_flag.startswith("crypto"):
        # If it does, we have found the correct key and decoded message
        flag = possible_flag
        break

# Print the decoded flag
print("Flag:")
print(flag)
