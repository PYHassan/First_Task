"""Python program to convert an integer to a roman numeral"""
class Convert_Algorithm:
    def int_to_Roman(self, num):
        # Create a lookup list containing tuples in the form of (roman value, integer).
        lookup = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I'),
        ]
        res = ''
        # For loop to iterate over the values in lookup.
        for (n, roman) in lookup:
            # Use divmod() to update num with the remainder, adding the roman numeral representation to the result.
            (d, num) = divmod(num, n)
            res += roman * d
        return res

# Test the script
print(Convert_Algorithm().int_to_Roman(1))
print(Convert_Algorithm().int_to_Roman(500))
print(Convert_Algorithm().int_to_Roman(755))
print(Convert_Algorithm().int_to_Roman(1200))
print(Convert_Algorithm().int_to_Roman(3456))

# Test Results
# I
# D
# DCCLV
# MCC
# MMMCDLVI
