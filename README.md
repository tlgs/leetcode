# Leetcode

`stats.awk` prints a summary of the available solutions:

```console
$ ./stats.awk *.py
┌──────────────────────┬─────┐
│ easy                 │  12 │
│ medium               │   6 │
└──────────────────────┴─────┘
┌──────────────────────┬─────┐
│ array                │   7 │
│ monotonic stack      │   6 │
│ binary tree          │   4 │
│ hash table           │   2 │
│ dynamic programming  │   2 │
│ set                  │   1 │
│ linked list          │   1 │
│ itertools            │   1 │
└──────────────────────┴─────┘
```

`list.awk` allows to search for specific tags:

```console
$ ./list.awk tree *.py
654. Maximum Binary Tree
  [monotonic stack, binary tree]

1008. Construct Binary Search Tree from Preorder Traversal
  [monotonic stack, binary tree]
```
