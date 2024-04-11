# Cousins in Binary Tree

Can you solve this real interview question? Cousins in Binary Tree - Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.

 

Example 1:

[https://assets.leetcode.com/uploads/2019/02/12/q1248-01.png]


Input: root = [1,2,3,4], x = 4, y = 3
Output: false


Example 2:

[https://assets.leetcode.com/uploads/2019/02/12/q1248-02.png]


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true


Example 3:

[https://assets.leetcode.com/uploads/2019/02/13/q1248-03.png]


Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false