from Crypto.Random import Fortuna

# Define the number of digits in the final random number
num_digits = 16

# Define the format string for the final random number
# This will create a 16-digit number with leading zeros
format_string = '{:0' + str(num_digits) + 'd}'

# Define the Fortuna generator
generator = Fortuna.new()

# Generate the random bytes using the Fortuna generator
output = generator.read(num_digits // 2)

# Convert the output to an integer
value = int.from_bytes(output, byteorder='big')

# Return the value formatted as a 16-digit number
random_number = format_string.format(value)

print(random_number)
