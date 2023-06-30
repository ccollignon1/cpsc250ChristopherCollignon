string1=input()
letter=string1[0]
phrase=string1[2:]

num_letter=phrase.count(letter)
if num_letter==1:
    print(num_letter,letter )
else:
    print(num_letter,letter + "'s")