# define a frase
frase = ('Little fly, Thy summer’s play My thoughtless hand Has brushed away. Am not I A fly like thee? Or art not thou A man like me?')

# faz a divisao da frase em palavras e cria nova lista words_list
words_list = frase.split()
print(words_list)


# Determinar o comprimento da lista nova
print("** a NOVA lista tem", len(words_list), "elementos **, ou seja: \n", words_list, '\n')

# pesquisar lista 'words_list' e converter palavras com 3 e 7 letras

for word in words_list:
    if len(word) <= 3:
        item = item.lower()
    print(item)
#     elif len(item) >= 7:
#         # y = str(item.upper())
#         print(item)

#         words_list(word) = words_list(word).lower()
#     elif len(i) >= 7:
#       words_list(i).upper
# print(words_list)

print("")
print("")

#!método 1
for index, word in enumerate(words_list):
    if len(word) <= 3:
        words_list[index] = word.lower()
    elif len(word) >= 7:
        words_list[index] = word.upper()
print("com o método1" + str(words_list))

print("")
print("")
#!método2
new_list = []
for word in words_list:
    if len(word) <= 3:
        new_list.append(word.lower())
    elif len(word) >= 7:
        new_list.append(word.upper())
    else:
        new_list.append(word)
print("com o método2" + str(new_list))






def word_mixer():
    words_list_sort = words_list.sort()

word_mixer()
