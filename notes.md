In Binary search, the total time cost is O(lgn)(base 2)

In sorting(merge sort), total time cost is O(nlgn). the logn comes from sorting each list, and the n comes from merging all n items together each time we merge two sorted sublists.

for binary tree, O is lg(n + 1)



* in place functions modify data structures outside of their own function calls. they "destroy" the original input.

in place algorithms usually have O(1) space cost.
But in-place algorithms are risky.


ammortized cost of appending to dynamic arrays is O(1). This is because the time cost of each special O(n) "doubling append" doubles each time, but the number of O(1) appends you get until the next doubling also doubles.
