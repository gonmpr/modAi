from functions.get_files_info import get_files_info

def test():
    print("TEST")
    print("\n","------------------------------------------","\n")
    print(get_files_info("calculator", "."))
    print("\n","------------------------------------------","\n")
    print(get_files_info("calculator", "pkg"))
    print("\n","------------------------------------------","\n")
    print(get_files_info("calculator", "/bin"))
    print("\n","------------------------------------------","\n")
    print(get_files_info("calculator", "../"))
    print("\n","------------------------------------------","\n")
    print("TEST SUCCESS!")

if __name__ == "__main__":
    test()
