#! /bin/awk -f
#
# Usage: ./list.awk QUERY file1 file2 ...


BEGIN {
  query = ARGV[1]
  delete ARGV[1]
}

FNR == 1 { problem = substr($0, 4) }

$1 ~ /difficulty:/ { difficulty = $2}

$1 ~ /tags:/ && $0 ~ query {
  sub(/tags: /, "", $0)
  printf "%s (%s)\n  [%s]\n\n", problem, difficulty, $0
}
