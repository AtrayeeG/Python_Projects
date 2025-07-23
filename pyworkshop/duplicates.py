list1 = [1,2,3,2,4,5,4,6,7,6]
duplicates = set()
seen = set()
for num in list1:
    if num in seen:
       duplicates.add(num)
    else:
        seen.add(num)
print("All the duplicate numbers are",duplicates)