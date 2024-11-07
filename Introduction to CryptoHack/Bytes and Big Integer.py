#This code will convert integer to hexadecimal and then to bytes and decode it to string
# Given integer
num = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

# Step 1: Convert the integer to a hexadecimal string
hex_string = hex(num)[2:]  # [2:] to remove the '0x' prefix

# Step 2: Convert the hexadecimal string to bytes
message_bytes = bytes.fromhex(hex_string)

# Step 3: Decode the bytes to a string
message = message_bytes.decode('utf-8')

print(f"The message is: {message}")
