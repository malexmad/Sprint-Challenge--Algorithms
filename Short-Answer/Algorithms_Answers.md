#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n^3) - Increasing n will make the while loop take more steps to complete because n is being cubed`(a < n * n * n)`.
But a is increasing every iteration `a = a + n * n`. I'm not sure if that is canceling out the time complexity and making
it be O(n^2) or O(n)

b)O(log n) - This algo has a for loop and while loop that makes it seem like O(n^2), but the while loop condition will 
stop once j is greater then n. On every loop j is getting multiplied by 2. Increasing n higher will have smaller effect 
of the time complexity because every j increase is getting bigger(x2)


c) O(n) - It's a recursive function that takes an integer and each pass thru of the function will subtract one bunnies. 
It will continue until bunny reaches the base case of zero. For every increase of bunnies(int) the complexity is increasing linearly. 

## Exercise II
Objective: Trying to find the highest floor where the egg will not break when dropped. Find that floor by minimizing the
lost of eggs when testing drops. 


#### Plan:
- start from the middle to test that floor
- if it breaks we know that floor and any above floors is not valid so we get rid of them, the next floor will test the 
middle of the floors below. vice versa if the opposite is true
- basically a binary search to find the floor

Runtime - O(log n) - increasing n will decrease the runtime complexity 