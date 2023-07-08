
# words = []

# with open('arabic_dataset_classifiction.csv', encoding='utf-8') as f:
#     lines = f.readlines()
    
#     for line in lines[1:]:
#         text = line.split(',')[0].strip()
#         split = text.split(' ')
#         for word in split:
#             if len(word) != 5:
#                 continue
#             # if word[0] == 'ا' and word[1] == 'ل':
#             #     continue
#             words.append(word.strip())

# with open('output_5l.csv', mode='w', encoding='utf-8') as f:
#     for i in range(0, len(words)):
#         word = words[i]
#         f.write(word)
#         if i != words[len(words)-1]:
#             f.write('\n')

def words_start_with1(input_file, letter1, output_file):
    words = []
    with open(input_file, encoding='utf-8') as f:
        lines = f.readlines()

    for line in lines:
        word = line.strip()
        words.append(word)

    words = list(filter(lambda word: word[0] == letter1, words))

    with open(output_file, mode='w', encoding='utf-8') as f:
        for i in range(0, len(words)):
            word = words[i]
            f.write(word)
            if i != words[len(words)-1]:
                f.write(',')

def words_start_with2(input_file, letter1, letter2, output_file):
    words = []
    with open(input_file, encoding='utf-8') as f:
        lines = f.readlines()

    for line in lines:
        word = line.strip()
        words.append(word)

    words = list(filter(lambda word: word[0] == letter1 and word[1] == letter2, words))

    with open(output_file, mode='w', encoding='utf-8') as f:
        for i in range(0, len(words)):
            word = words[i]
            f.write(word)
            if i != words[len(words)-1]:
                f.write(',')


# words_start_with1('data\\5letters.csv', 'و', 'out.csv')

import pandas as pd

df = pd.read_csv('data\\5letters\\wa.csv', encoding='utf-8', header=None)
print(df.head())