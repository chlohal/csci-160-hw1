## Question 1

### In-Class Binary Search:

```python
bs(Arr, element):
	mid_index := floor(|Arr| / 2)
	x := Arr[mid_index]
	if x = element:
		return mid_index
	if x < element:
		return bs(Arr[ mid_index : |Arr| ], element)
	if x > element:
		return bs(Arr[ 1 : mid_index], element)
```

Bugs in this algorithm include:
- There is no negative base case (i.e. the value **must** be in the array, or the algorithm will never terminate)
- The index returned is an index **into a slice** of the original array. For example, for `bs([1, 2, 3, 4, 5, 6], 2)`, the algorithm will call `bs([1, 2, 3], 2)` to search the left half, but it will then return `1` because `([1, 2, 3])[1] == 2`.
- The first index (`0`) is never searched because the left-side slice starts at `1` 

### Our Binary Search:

```python
our_bs(Arr, element, istart, istop):
	if istart >= istop:
		the element is not in the array
	mid_index := floor((istart + istop) / 2)
	x := Arr[mid_index]
	if x = element:
		return mid_index
	if x < element:
		return our_bs(Arr, element, midpoint + 1, istop)
	if x > element:
		return our_bs(Arr, element, istart, midpoint)
```

This algorithm runs in $O(\log n)$ because each recursive iteration cuts the decision space in half. Either $\text{istart} := \text{midpoint + 1}$ or $\text{istop} := \text{midpoint}$ -- either way, the range between `istart` and `istop` is decreased by a factor of $\frac{1}{2}$



## Question 2

```python
def our_bs(arr, target, istart, istop):
    # Element is not in the array -> False
    if istart >= istop:
        return False
    
    # Assigning the midpoint to the average of the start and stop indices
    midpoint = (istart + istop) // 2
    
    # Assigning the value of the element at the midpoint to x
    x = arr[midpoint]
    
    # This is exactly the pseudo code with variable names changed to fit the rest of the code
    if x == target:
        return midpoint
    if x < target:
        return our_bs(arr, target, midpoint + 1, istop)
    if x > target:
        return our_bs(arr, target, istart, midpoint)
```

![](./plot.png) 

## Question 3 

Write down the math to explain why the following code takes $O(n)$ run time.

```
for i = 0 to log(n):
	for j = 1 to n/(2^i):
		Do some constant work
```

---

$$
\begin{gather}
d(n) = \sum_{i=0}^{\log(n)} \sum_{j=1}^{\frac{n}{2^{i}}} 1 \\
d(n) = \sum_{i=0}^{\log(n)} \frac{n}{2^{i}} \\
d(n) = \sum_{i=0}^{\log(n)} n2^{-i} \\
d(n) = \sum_{i=0}^{\log(n)} n (0.5)^{i} \\
\text{Since } n 0.5^{i} \text{ is a geometric series} \\
\text{with a closed form of } \frac{n}{1 - 0.5}, \\
\lim_{ n \to \infty } \frac{d(n)}{n} = \frac{\frac{n}{1 - 0.5}}{n} = 1 \therefore \\
\text{the tighest bound on runtime is }O(n)
\end{gather}
$$
