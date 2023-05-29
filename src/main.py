import example


p = example.Pet("Lucy", example.Pet.Cat)
print(p.type)
print(int(p.type))
print(example.Pet.Kind.__members__)
