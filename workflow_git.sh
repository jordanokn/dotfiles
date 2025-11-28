#!/usr/bin/env bash

AUTHOR="George Knyazyan <jorj.knyazyan.15@gmail.com>"
SINCE="${1:-24 hours ago}"

git log \
  --since="$SINCE" \
  --author="$AUTHOR" \
  --pretty=format:"%s" |
  grep -oE '^[A-Z]+-[0-9]+' |
  sort |
  uniq -c |
  awk '{print $2 " (+" $1 ")"}'
