from functions.write_file import write_file

def test():
    print("Result for lorem.txt:")
    content = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(content)
    print()

    print("Result for pkg/morelorem.txt:")
    content = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(content)
    print()

    print("Result for /tmp/temp.txt:")
    content = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(content)
    print()

if __name__ == "__main__":
    test()