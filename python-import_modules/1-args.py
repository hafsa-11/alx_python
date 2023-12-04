from sys import argv

if _name_ == "_main_":
    num_args = len(argv) - 1
    plural_s = "s" if num_args != 1 else ""
    
    print("Number of argument{}: {}{}".format(plural_s, num_args, ":" if num_args else "."))
    
    if num_args > 0:
        for i, arg in enumerate(argv[1:], start=1):
            print("{}: {}".format(i, arg))