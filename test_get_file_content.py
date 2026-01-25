from functions.get_file_content import get_file_content
from config import CHAR_LIMIT

print("Result for lorem.txt:")
content = get_file_content("calculator", "lorem.txt")
assert len(content) >= CHAR_LIMIT
assert f'truncated at {CHAR_LIMIT} characters' in content
print(content)
print()

print("Result for main.py:")
print(get_file_content("calculator", "main.py"))
print()

print("Result for pkg/calculator.py:")
print(get_file_content("calculator", "pkg/calculator.py"))
print()

print("Result for /bin/cat:")
print(get_file_content("calculator", "/bin/cat"))
print()

print("Result for pkg/does_not_exist.py:")
print(get_file_content("calculator", "pkg/does_not_exist.py"))
print()