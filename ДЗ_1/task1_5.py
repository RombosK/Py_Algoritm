# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
print('Ведите 2 любые прописные буквы английского алфавита: ')
char1 = input('char1 = ').upper()
char2 = input('char2 = ').upper()

pos_char1 = ord(char1) - 64
pos_char2 = ord(char2) - 64
distance = abs(pos_char1 - pos_char2) - 1
print(f'Буква "{char1}" {pos_char1}-я  позиция в алфавите')
print(f'Буква "{char2}" {pos_char2}-я позиция в алфавите')
print(f'Между буквами {distance} букв')