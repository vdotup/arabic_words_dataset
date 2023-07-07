
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

words = []

with open('output_5l.csv', encoding='utf-8') as f:
    lines = f.readlines()
    print(lines)
    
    for line in lines:
        word = line.strip()
        words.append(word)

start_al = words = filter(lambda word: word[0] == 'ا' and word[1] == 'ل', words)

