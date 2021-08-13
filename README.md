# Leetcode

`stats.awk` prints a summary of the available solutions:

```console
$ ./stats.awk *.py
┌────────────────────────────┐ ┌────────────────────────────┐
│ Difficulty                 │ │ Tags                       │
├──────────────────────┬─────┤ ├──────────────────────┬─────┤
│ easy                 │  12 │ │ monotonic stack      │   7 │
│ medium               │   9 │ │ array                │   7 │
└──────────────────────┴─────┘ │ binary tree          │   4 │
                               │ dynamic programming  │   3 │
                               │ hash table           │   2 │
                               │ set                  │   1 │
                               │ linked list          │   1 │
                               │ itertools            │   1 │
                               │ greedy               │   1 │
                               └──────────────────────┴─────┘
┌────────────────────────────┐ ┌────────────────────────────┐
│ Runtime distribution       │ │ Memory distribution        │
├────┬───────────────────────┤ ├────┬───────────────────────┤
│ 90 │ ************          │ │ 90 │ ***                   │
│ 80 │ **                    │ │ 80 │ ***                   │
│ 70 │ ****                  │ │ 70 │ ****                  │
│ 60 │ **                    │ │ 60 │ *                     │
│ 50 │ *                     │ │ 50 │ ***                   │
│ 40 │                       │ │ 40 │ **                    │
│ 30 │                       │ │ 30 │ ****                  │
│ 20 │                       │ │ 20 │ *                     │
│ 10 │                       │ │ 10 │                       │
│  0 │                       │ │  0 │                       │
└────┴───────────────────────┘ └────┴───────────────────────┘
```

`list.awk` allows to search for specific tags:

```console
$ ./list.awk tree *.py
104. Maximum Depth of Binary Tree (easy)
  [binary tree]

654. Maximum Binary Tree (medium)
  [monotonic stack, binary tree]

894. All Possible Full Binary Trees (medium)
  [dynamic programming, binary tree]

1008. Construct Binary Search Tree from Preorder Traversal (medium)
  [monotonic stack, binary tree]
```
