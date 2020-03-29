import conversion
import equations


def main():
    conversion.setup_conversion()
    equations.add_variables()
    equations.add_equations()

    print("Hello, welcome to Physo!/n")
    cont = True
    while cont:
        print("Please select an option:")
        print("a: add variable")
        print("q: quit Physo")
        user = input("/n")
        if user == "a":
            variable = input("What variable of the physics problem is this?/n")
            # check to see if variable is in system

            value = input("What is its value?/n")

        elif user == "q":
            cont = False
        else:
            print("Please try again!/n")
    exit()


if __name__ == '__main__':
    main()
