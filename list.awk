#! /bin/awk -f
#
# Usage: ./list.awk QUERY file1 file2 ...


BEGIN {
  if (NR == 0) {
    query = ARGV[1]
    delete ARGV[1]
  }
}

FNR == 1 { problem = substr($0, 4) }

$1 ~ /tags:/ && $0 ~ query {
  sub(/tags: /, "", $0)
  printf "%s\n  [%s]\n\n", problem, $0
}