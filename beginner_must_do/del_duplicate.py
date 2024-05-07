a = [3, 2, 1, 6, 3, 8, 0, 1, 2, 2, 4, 4]
print("before:", a)
def delete_duplicate(a):
    for i in range(len(a)-1):
        j = i + 1
        for j in range(j, len(a)):
            if a[i] == a[j]:
                a.remove(a[j])

print("after:", a)
