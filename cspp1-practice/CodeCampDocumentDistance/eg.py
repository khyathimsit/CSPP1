import copy
stop = ["is", "a", "be"]
sen = ["Raju", "is", "a", "random"]
temp = copy.deepcopy(sen)
for word in temp:
    if word in stop:
        sen.remove(word)
print(sen)