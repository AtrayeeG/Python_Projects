items = [1, 2, 3, 4, 5, 1, 5, 3, 3]
repeated = []
def repeat(list):
    for num in list:
        if list.count(num) == 2:
            repeated.append(num)
    return repeated
print("Repeated" , repeat(items))
print("Repeated" , repeat(items))

state | name | age
KL | foo | 45
KL | fooz | 56
KA | bar | 50
KA | barz | 25
MH | foobar | 65
MH | baz | 50

select * from people
where max(age) 