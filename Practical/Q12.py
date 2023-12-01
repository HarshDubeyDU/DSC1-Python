t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)


# other half in the next line.
tuple_length = len(t1) // 2
print(t1[:tuple_length])
print(t1[tuple_length:])

# 2. Print even values
tuple_even = tuple(i for i in t1 if i % 2 == 0)
print("Even tuple values")
print(tuple_even[:])

# 3. Concatenate another tuple.
t2 = (11, 13, 15)
t1 = t1 + t2
print(t1[:])

# 4. Return maximum and minimum value from this tuple.
min = min(t1)
max = max(t1)
print("Minimum value in tuple:", min)
print("Maximum value in tuple:", max)

