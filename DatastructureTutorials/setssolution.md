Solution for Union:
```python
for i in bag1:
    bag3.add(i)
for j in bag2:
    bag3.add(j)
print("Union = {}".format(bag3))
```
Solution for Intersection:
```python
for i in bag1:
     for j in bag2:
         if j == i:
             bag3.add(i)
print(f"Intersection = {bag3}")   
```