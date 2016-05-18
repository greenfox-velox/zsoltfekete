ag = [3, 4, 5, 6, 7]

#while
i = 0
b = len(ag)

while i < b :
    ag[i] *= 2
    i += 1
print(ag)

# for

for i in range(len(ag)):
    ag[i] *= 2
print(i)


### element double ###
ag = [3, 4, 5, 6, 7]

#while
i = 0
b = len(ag)

while i < b :
    print()
    ag += [ag[i]]
    i += 1
print(ag)

# for
i = 0
b = len(ag)

for i in range(b) :
    ag += [ag[i]]
print(ag)
