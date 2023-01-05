from collections import deque

def create_flowers_letters_sum (flowers):
    flower_sum_letter = dict()
    for item in flowers:
        flower_sum_letter[item] = len(item)
    return flower_sum_letter


flowers = ["rose", "tulip", "lotus", "daffodil"]
flowers_letter_sum = create_flowers_letters_sum(flowers)
vowels_collection = input().split(' ')
consonants_collection = input().split(' ')
queue = deque(vowels_collection)
flower_is_not_found = True
while queue and consonants_collection:
    current_vowel = queue.popleft()
    current_consonants = consonants_collection.pop()

    for flower in flowers_letter_sum:
        if current_vowel in flower:
            flowers_letter_sum[flower] -= flower.count(current_vowel)
        if current_consonants in flower:
            flowers_letter_sum[flower] -= flower.count(current_consonants)
        if flowers_letter_sum[flower] == 0:
            print(f'Word found: {flower}')
            if queue:
                print(f'Vowels left: {" ".join(queue)}')
            if consonants_collection:
                print(f'Consonants left: {" ".join(consonants_collection)}')
            flower_is_not_found = False
            break
    if not flower_is_not_found:
        break
if flower_is_not_found:
    print('Cannot find any word!')
    if queue:
        print(f'Vowels left: {" ".join(queue)}')
    if consonants_collection:
        print(f'Consonants left: {" ".join(consonants_collection)}')















