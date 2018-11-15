farm_animals = {"sheep", "cow", "horse"}

for animal in farm_animals:
    print(animal)
print('='*40)
wild_animals = set(["lion",'wolf','elephant'])
for wild in wild_animals:
    print(wild)

farm_animals.add("goat")
wild_animals.add("aligator")
print(farm_animals)
print(wild_animals)