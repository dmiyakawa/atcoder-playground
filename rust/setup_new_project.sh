#!/bin/bash

set -e

if [ $# -ne 1 ]; then
  echo "An argument is required" 1>&2
  exit 1
fi

if [[ ! $1 =~ ^[0-9a-zA-Z_]+$ ]]; then
  echo "Illegal string format supplied (\"$1\")" 1>&2
  exit 1
fi

if [ -e "$1" ]; then
  echo "\"$1\" already exists" 1>&2
  exit 1
fi

echo "> " cargo new "$1"
cargo new "$1"

echo
echo "> " cp dot.gitignore "$1/.gitignore"
cp dot.gitignore "$1/.gitignore"

echo
echo "> " cp template.rs "$1/src/main.rs"
cp template.rs "$1/src/main.rs"

