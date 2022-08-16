import random


WIN_RATE = 0.3
NUMBER_OF_DRAWS = 10

draws = []
win_draws = int(NUMBER_OF_DRAWS * WIN_RATE)
loss_draws = NUMBER_OF_DRAWS - win_draws

print(f"win = {win_draws} / loss = {loss_draws}")

for i in range(win_draws):
    draws.append(1)

for i in range(loss_draws):
    draws.append(0)

random.seed()
random.shuffle(draws)

print(draws)
