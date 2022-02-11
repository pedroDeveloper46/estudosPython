algo = input('Digite algo ')

print('Esse valor é do tipo {}'.format(type(algo)))

isNumeric = algo.isnumeric()
print('É número? {}'.format(isNumeric))

isAlpha = algo.isalpha()
print('É letra? {}'.format(isAlpha))

isAlnum = algo.isalnum()
print('É Alfanúmerico? {}'.format(isAlnum))

isUpper = algo.isupper()
print('Está em maiusculo? {}'.format(isUpper))

isLower = algo.islower()
print('Está tudo em minusculo? {}'.format(isLower))

isSpace = algo.isspace()
print('É um espaço? {}'.format(isSpace))