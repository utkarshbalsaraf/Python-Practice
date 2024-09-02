import random

# for x in range(10):
#     number = random.randint(1, 20)
#     print(number)

# tuples = ("stone", "paper", "scissor")
# option = random.choice(tuples)
# print(option)

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "K", "Q", "J", "A"]
random.shuffle(cards)
print(cards)
