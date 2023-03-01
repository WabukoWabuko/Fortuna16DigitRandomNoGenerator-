from Crypto.Random import Fortuna

# number of digits in the final random number
digits_num = 16

# format string for the final random number
# This will create a 16-digit number with leading zeros
format_string = '{:0' + str(digits_num) + 'd}'

# Fortuna generator is defined.
Generator = Fortuna.new()

# Generation of Random bytes by the use of Fortuna Generator.
output = Generator.read(digits_num // 2)

# Convert the output to an integer
value = int.from_bytes(output, byteorder='big')

# Returns a formatted 16-digit number
random_number = format_string.format(value)

print(random_number)
