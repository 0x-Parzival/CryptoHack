# Hex string
#this code will convert the hex code to thier ascii characters
hex_string = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

# Convert hex string to bytes
decoded_bytes = bytes.fromhex(hex_string)

# Convert bytes to string
decoded_string = decoded_bytes.decode('utf-8')

print(f"The flag is: {decoded_string}")
