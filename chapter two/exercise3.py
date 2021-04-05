
# user_name,user_char = input('enter your name and a single characte ==>').split(',')


name,character = input('please enter a name and character ').split(',')

#another times
# print(f'the lenght of your name is =  {len(name)}')
# print(f'character is = {(name.lower()).count((character.lower()))}')
# (name.lower()).count((character.lower()))








# print(user_name)
# print(f'the lenth of the username is = {len(user_name)}')



# char = user_name.count(user_char)
# print(f'the character in this username is = {char}')
# print(f'character count is = {user_name.count(user_char)}')



# make case insensitive method
# print(f'character count is = {user_name.upper().count(user_char.upper())}')




#remove space problem

# name => name.strip() => name.strip().lower()
# character => character.strip() => character.strip().lower()


print(f'the length of you name is {name.strip()}')
print(f'character is = {name.strip().lower().count(character.strip().lower())}')




