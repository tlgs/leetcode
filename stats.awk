#! /bin/awk -f
#
# Notes:
#   - PROCINFO is a GAWK specific feature.
#
# Usage: ./stats.awk


$1 ~ /difficulty:/ {
  difficulty[$2] += 1
}

$1 ~ /tags:/ {
  sub(/tags: /, "", $0)
  split($0, a, ", ")
  for (i in a) {
    tags[a[i]] += 1
  }
}

END {
  print "┌──────────────────────┬─────┐"
  for (k in difficulty) {
    printf "│ %-20s │ %3d │\n", k, difficulty[k]
  }
  print "└──────────────────────┴─────┘"

  PROCINFO["sorted_in"] = "@val_num_desc"

  print "┌──────────────────────┬─────┐"
  for (k in tags) {
    printf "│ %-20s │ %3d │\n", k, tags[k]
  }
  print "└──────────────────────┴─────┘"
}
