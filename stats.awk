#! /bin/awk -f
#
# Note: PROCINFO["sorted_in"] values are gawk specific.
#
# Usage: ./stats.awk file1 file2 ...


$1 ~ /difficulty:/ { diff[$2]++ }

$1 ~ /tags:/ {
  sub(/tags: /, "", $0)
  split($0, a, ", ")
  for (i in a) {
    tags[a[i]]++
  }
}

$1 ~ /runtime:/ { runtime[int($2 / 10)]++ }

$1 ~ /memory:/ { memory[int($2 / 10)]++ }

END {
  n = asorti(diff, ddiff, "@ind_str_asc")
  m = asorti(tags, dtags, "@val_num_desc")

  print "┌────────────────────────────┐ ┌────────────────────────────┐"
  print "│ Difficulty                 │ │ Tags                       │"
  print "├──────────────────────┬─────┤ ├──────────────────────┬─────┤"
  for (i = 1; i <= n; i++) {
    printf "│ %-20s │ %3d │ │ %-20s │ %3d │\n", ddiff[i], diff[ddiff[i]], dtags[i], tags[dtags[i]]
  }
  printf "└──────────────────────┴─────┘ │ %-20s │ %3d │\n", dtags[n+1], tags[dtags[n+1]]
  for (i = n+2; i <= m; i++) {
    printf "                               │ %-20s │ %3d │\n", dtags[i], tags[dtags[i]]
  }
  print "                               └──────────────────────┴─────┘"

  print "┌────────────────────────────┐ ┌────────────────────────────┐"
  print "│ Runtime distribution       │ │ Memory distribution        │"
  print "├────┬───────────────────────┤ ├────┬───────────────────────┤"
  for (i = 9; i >= 0; i--) {
    printf "│ %2i │ ", i * 10
    for (j = 0; j < 22; j++) {
      printf "%c", j < int((runtime[i] / (ARGC - 1)) * 22) ? "*" : " "
    }
    printf "│ "

    printf "│ %2i │ ", i * 10
    for (j = 0; j < 22; j++) {
      printf "%c", j < int((memory[i] / (ARGC - 1)) * 22) ? "*" : " "
    }
    printf "│\n"
  }
  print "└────┴───────────────────────┘ └────┴───────────────────────┘"
}
