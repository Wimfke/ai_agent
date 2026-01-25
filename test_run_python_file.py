from functions.run_python_file import run_python_file

def test():
    print("Result for main.py:")
    content = run_python_file("calculator", "main.py")
    print(content)
    print()

    print('Result for main.py, ["3 + 5"]:')
    content = run_python_file("calculator", "main.py", ["3 + 5"])
    print(content)
    print()

    print('Result for tests.py:')
    content = run_python_file("calculator", "tests.py")
    print(content)
    print()

    print('Result for ../main.py:')
    content = run_python_file("calculator", "../main.py")
    print(content)
    print()

    print('Result for nonexistent.py:')
    content = run_python_file("calculator", "nonexistent.py")
    print(content)
    print()

    print('Result for lorem.txt:')
    content = run_python_file("calculator", "lorem.txt")
    print(content)
    print()


if __name__ == "__main__":
    test()