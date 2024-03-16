def student():
    Pass = 0
    Defer = 0
    Fail = 0
    progress = 0
    trailer = 0
    retriever = 0
    exclude = 0

    print('_ ' * 60, " ""\n")
    print(' * ' * 17, "Student Version" ,' * ' * 17)

    Pass = input("Please enter your credits at pass: ")
    if not Pass.isdigit(): #https://www.w3schools.com/python/ref_string_isdigit.asp (Used to check whether all the user inputs are integers).
        print("Integer required")
    elif int(Pass) not in [0, 20, 40, 60, 80, 100, 120]: # https://www.askpython.com/python/examples/in-and-not-in-operators-in-python (Used to find user inputs are in the range)
        print("Out of range.")
    else:
        Defer = input("Please enter your credits at defer: ")
        if not Defer.isdigit():
            print("Integer required")
        elif int(Defer) not in [0, 20, 40, 60, 80, 100, 120]:
            print("Out of range.")
        else:
            Fail = input("Please enter your credits at fail: ")
            if not Fail.isdigit():
                print("Integer required")
            elif int(Fail) not in [0, 20, 40, 60, 80, 100, 120]:
                print("Out of range.")
            elif int(Pass) + int(Defer) + int(Fail) != 120:
                print("Total incorrect.")
            else:
                if int(Pass) == 120:
                    print("Progress")
                    progress = progress + 1

                elif int(Pass) >= 100:
                    print("Progress (module trailer)")
                    trailer = trailer + 1

                elif int(Pass) >= 40 and int(Fail) <= 60 or int(Defer) >= 60 and int(Fail) <= 60:
                    print("Do not progress – module retriever")
                    retriever = retriever + 1
                    
                else:
                    print("Exclude")
                    exclude = exclude + 1
                
def staff():
    valid = True
    Pass = 0
    Defer = 0
    Fail = 0
    progress = 0
    trailer = 0
    retriever = 0
    exclude = 0
    list = []

    print('_ ' * 60, " ""\n")
    print(' * ' * 15, "Staff Version" ,' * ' * 15)

    # Part 1 Histogram code in a def
    def part1():

        print('_ ' * 50, " ")
        print("Part 1:")
        print('Histogram')
        print('Progress ', progress, '   :', '* ' * progress)
        print('Trailer ', trailer, '    :', '* ' * trailer)
        print('Retriever ', retriever, '  :', '* ' * retriever)
        print('Excluded ', exclude, '   :', '* ' * exclude)
        print()
        print(progress + trailer + retriever + exclude, 'outcome in total.')
        print('_ ' * 50)

    # Part 2 List assingning for the users input
    def part2():
        print("Part 2:")
        for p in list:
            print(p)
        print('_ ' * 50)

    #Part 3 Generating the text file 
    def part3():
        print("Part 3:")
        outFile = open('Part 03 Output.txt', 'w+')  # open the txt file
        for p in list:
            outFile.write(p + '\n')
        outFile.close()

        # Print out the histogram saved in the txt file    
        fileData = open('Part 03 Output.txt', 'r')
        read = fileData.read()
        print(read)
        fileData.close()

    #Main programm of the Assignment
    while (valid):
            Pass = input("Please enter your credits at pass: ")
            if not Pass.isdigit(): #https://www.w3schools.com/python/ref_string_isdigit.asp (Used to check whether all the user inputs are integers).
                print("Integer required")
            elif int(Pass) not in [0, 20, 40, 60, 80, 100, 120]: # https://www.askpython.com/python/examples/in-and-not-in-operators-in-python (Used to find user inputs are in the range)
                print("Out of range.")
            else:
                Defer = input("Please enter your credits at defer: ")
                if not Defer.isdigit():
                    print("Integer required")
                elif int(Defer) not in [0, 20, 40, 60, 80, 100, 120]:
                    print("Out of range.")
                else:
                    Fail = input("Please enter your credits at fail: ")
                    if not Fail.isdigit():
                        print("Integer required")
                    elif int(Fail) not in [0, 20, 40, 60, 80, 100, 120]:
                        print("Out of range.")
                    elif int(Pass) + int(Defer) + int(Fail) != 120:
                        print("Total incorrect.")
                    else:
                        if int(Pass) == 120:
                            print("Progress")
                            progress = progress + 1
                            list.append(f"Progress - {Pass}, {Defer}, {Fail}")

                        elif int(Pass) >= 100:
                            print("Progress (module trailer)")
                            trailer = trailer + 1
                            list.append(f"Progress (module trailer) - {Pass}, {Defer}, {Fail}")

                        elif int(Pass) >= 40 and int(Fail) <= 60 or int(Defer) >= 60 and int(Fail) <= 60:
                            print("Do not progress – module retriever")
                            retriever = retriever + 1
                            list.append(f"Do not Progress - module retriever - {Pass}, {Defer}, {Fail}")
                        else:
                            print("Exclude")
                            exclude = exclude + 1
                            list.append(f"Exclude - {Pass}, {Defer}, {Fail}")
    
                        print('Would you like to enter another set of data ?')
                        Decision = input("Enter 'y' for yes or 'q' to quit and view results: ")   
                        print()

                        if (Decision == "y"):
                            continue
                        elif (Decision == "q"):
                            part1()
                            part2()
                            part3()
                            break

stt = input("Please enter '1' for student version or enter '2' for staff version : ")
if stt == "1":
    student()
elif stt == "2":
    staff()                 
