#here we have to convert there numbers to character to their ASCII value, use this python code
# Given integer array
ascii_values = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]# enter your required values

# Convert to ASCII characters
ascii_characters = ''.join(chr(value) for value in ascii_values)

# Print the flag
print(f"The flag is: {ascii_characters}")
