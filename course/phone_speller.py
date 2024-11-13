

# INPUT : 0645458796
# OUTPUT : Zero Six ...


digits_mapping = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}
phone_number = input('Veuillez entrer un numéro de téléphone : ')
result = ''
for digit in phone_number:
    result = result + digits_mapping.get(digit, '[Character not mapped]') + " "

print(result.strip())
