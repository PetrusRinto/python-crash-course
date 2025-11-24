# Patrick 24.11.2025.
# 10-1 Learning Python.

from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()
print(contents)

lp_list = contents.splitlines()
for line in lp_list:
    print(line)