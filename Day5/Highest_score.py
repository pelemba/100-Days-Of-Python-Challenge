highest_score = 0

scores = input("Enter a list of student heights: ").split()
for n in range(0, len(scores)):
    scores[n] = int(scores[n])

for score in scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score is {highest_score}")
