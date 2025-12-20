from functions.run_python_file import run_python_file

def test():
    print("\n","------------------------------------------","\n")
    print("TEST")
    print("\n","------------------------------------------","\n")
    print(run_python_file("calculator", "main.py"))
    print("\n","------------------------------------------","\n")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))
    print("\n","------------------------------------------","\n")
    print(run_python_file("calculator", "tests.py"))
    print("\n","------------------------------------------","\n")
    print(run_python_file("calculator", "../main.py"))
    print("\n","------------------------------------------","\n")
    print(run_python_file("calculator", "nonexistent.py"))
    print("\n","------------------------------------------","\n")
    print(run_python_file("calculator", "lorem.txt"))
    print("\n","------------------------------------------","\n")
    print("DONE!")
    print("\n","------------------------------------------","\n")

if __name__ == "__main__":
    test()
