from functions.get_file_content import get_file_content

def test():
    print("TEST")
    print("\n","------------------------------------------","\n")
    print(get_file_content("calculator", "main.py"))
    print("\n","------------------------------------------","\n")
    print(get_file_content("calculator", "pkg/calculator.py"))
    print("\n","------------------------------------------","\n")
    print(get_file_content("calculator", "/bin/cat"))
    print("\n","------------------------------------------","\n")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))
    print("\n","------------------------------------------","\n")
    print("TEST SUCCESS!")

if __name__ == "__main__":
    test()
