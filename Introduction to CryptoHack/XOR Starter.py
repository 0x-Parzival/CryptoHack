#this will convert the integer to string using XOR
def xor_string_with_int(input_string, xor_int):
    # Create a list to hold the XORed characters
    xor_result = []

    # XOR each character with the given integer and convert back to a character
    for char in input_string:
        xor_char = chr(ord(char) ^ xor_int)
        xor_result.append(xor_char)

    # Join the list of characters into a new string
    new_string = ''.join(xor_result)
    return new_string

# Given string
input_string = "label"
xor_int = 13

# Get the new XORed string
new_string = xor_string_with_int(input_string, xor_int)

# Print the result in the required format
flag = f"crypto{{{new_string}}}"
print(f"The flag is: {flag}")
