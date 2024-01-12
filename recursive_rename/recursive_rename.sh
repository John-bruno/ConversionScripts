#!/bin/bash
find ~/Desktop/Integration -type f -name '*_ja-JP*.md' | while read -r file; do
  new_file=$(echo "$file" | sed 's/_ja-JP//')
  mv "$file" "$new_file"
done
