import random 

word = input("Enter your word here: ")

# print("".join(random.sample(word, len(word))))
# print("".join(random.sample(word, len(word)))) 
# print("".join(random.sample(word, len(word)))) 
# print("".join(random.sample(word, len(word)))) 
# print("".join(random.sample(word, len(word)))) 

# i = 0
# while i < 5:
#     print("".join(random.sample(word, len(word))))
#     i += 1

for _ in range(5):
    print("".join(random.sample(word, len(word))))
