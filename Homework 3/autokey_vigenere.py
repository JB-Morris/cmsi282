__author__ = 'Joseph'

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbering = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
plaintext = "TAKEACOPYOFYOURPOLICYTONORMAWILCOXONTHETHIRDFLOOR"
key = "QUARK"
plaintext.upper()
key.upper()
cypher = key + plaintext
result = [None]*len(plaintext)

for x in range(0, len(plaintext)):
    current_alphabet_index = alphabet.index(plaintext[x])
    current_cypher_index = alphabet.index(cypher[x])
    current_result_character_index = (current_alphabet_index + current_cypher_index)%len(alphabet)
    # print current_result_character_index
    current_result_character = alphabet[current_result_character_index]
    result[x] = current_result_character
print ''.join(result)