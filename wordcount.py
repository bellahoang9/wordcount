# # put your code here.
file = open('test.txt')

def word_count(file):
    total_word_count = {}
    

    for line in file:
        line = line.rstrip()
        words = line.split(' ')

        for word in words:
            word = word.strip(',.?')
            word = word.lower()
            total_word_count[word] = total_word_count.get(word, 0) + 1
    
    # for word, count in sorted(total_word_count.items()):
        # reversed = total_word_count[1], total_word_count[0]
        # reversed_dict = total_word_count.setdefault(count, list()).append(word)
        # print(f'{word} {count}')
    reversed_dict = reversed(total_word_count)
    for key, value in sorted(reversed_dict):
        print(key, value)

    file.close()

def reversed(dict):
    reversed_dict = {}
    for x, y in dict.items():
        reversed_dict[y] = x
        reversed_dict[x] = y
    print(reversed_dict)
    return reversed_dict

word_count(file)