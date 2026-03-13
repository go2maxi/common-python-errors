\# IndexError: list index out of range



\## Error



```

IndexError: list index out of range

```



This error appeared when I tried to access a list index that doesn’t actually exist.



At first it looked simple, but it reminded me again that Python lists start at \*\*0\*\*, not \*\*1\*\*.



\---



\## Reproducing the Error



```python

numbers = \[10, 20, 30]



print(numbers\[3])

```



The list only contains three elements.



Valid indexes are:



0

1

2



So index \*\*3\*\* raises the error.



\---



\## Why This Happens



The confusing part is that the \*\*length of the list is 3\*\*, but the \*\*largest valid index is 2\*\*.



```python

numbers = \[10, 20, 30]

```



Even though the list has three elements, trying to access index 3 will trigger:



```

IndexError: list index out of range

```



\---



\## A Common Loop Mistake



One situation where this happens easily is inside loops.



```python

numbers = \[10, 20, 30]



for i in range(len(numbers) + 1):

&#x20;   print(numbers\[i])

```



That `+1` is the problem.



It makes the loop try index \*\*3\*\*, which does not exist.


I tend to add +1 when I'm tired or rushing.

It's easy to push the loop one step too far without noticing.


The safer version is simply:



```python

for i in range(len(numbers)):

&#x20;   print(numbers\[i])

```



\---



\## Simple Defensive Patterns



\### Boundary check



```python

numbers = \[10, 20, 30]

index = 3



if index < len(numbers):

&#x20;   print(numbers\[index])

```



\---



\### try / except



Sometimes the index depends on dynamic input, so catching the error can be easier.



```python

numbers = \[10, 20, 30]



try:

&#x20;   print(numbers\[3])

except IndexError:

&#x20;   print("Handled safely")

```



\---



\## My Observation



I noticed this error usually appears when I \*\*assume the list is longer than it really is\*\*.



It also shows up when loops are written quickly and the index boundary is not checked carefully.



Even though zero-based indexing is basic, it’s surprisingly easy to make this mistake when the code becomes slightly more complex.



\---



\## Related Errors



TypeError: list indices must be integers or slices, not str

IndexError: tuple index out of range



