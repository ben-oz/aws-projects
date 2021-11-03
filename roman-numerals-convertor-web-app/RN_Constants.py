TEXT_START = """
... This program converts decimal numbers to Roman Numerals ...
(To exit the program, please type 'exit')
"""
TEXT_ASK_INPUT = "Please enter a number between 1 and 3999, inclusively: "
TEXT_EXIT = "\nExiting the program\n...Good Bye...\n" 
TEXT_ERROR = "Not a valid input! Please enter a decimal number between 1-3999 inclusively\n"

LETTERS = {
    1000: 'M',
    500: 'D',
    100: 'C',
    50: 'L',
    10: 'X',
    5: 'V',
    1: 'I'
}

SPECIAL_NUMBERS = {
    'DCCCC': 'CM',
    'CCCC': 'CD',
    'LXXXX': 'XC',
    'XXXX': 'XL',
    'VIIII': 'IX',
    'IIII': 'IV'
}
