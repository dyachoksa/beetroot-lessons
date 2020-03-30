def main():
    line_count = 0
    words_count = 0

    with open('text.txt') as f:
        for line in f:
            line_count += 1
            words_count += len(line.replace('a', '').replace('the', '').split())
            # temp_sts1 = line.replace('a', '')
            # temp_sts2 = temp_sts1.replace('the', '')
            # res_str += temp_sts2.strip()
        
    # words_list = res_str.split()
    # words_count = len(words_list)

    print(f'This file has {line_count} lines.')
    print(f'This file has {words_count} words.')
    # print(words_list)

if __name__ == '__main__':
    main()

# with open("file.txt","r") as f:
#     # lines = f.read().split("\n")
#     lines = f.readlines()
#     count = len(lines)
#     print(f"Количество строк = {count}")

#     wordcount = 0
#     a_count = 0
    
#     # another

#     count = 0
#     for line in lines:
#         for word in line.split():
#             if word not in ["a", "the", ".", "?", "!",]:
#                 count += 1

#         # words = line.replace("."," ").split()
#         # wordcount += len(words)
#         # a_count += words.count("a")+words.count("an")+words.count("A")+words.count("AN")

#     print(f"Количество слов = {count}")
#     # print(f"В т.ч. артиклей = {a_count}")
