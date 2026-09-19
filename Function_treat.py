print("\n Welcome to the data analyzer and transformer program")
num = []


def input_data():
    '''Input 1D data from user.'''
    global num
    data = input("Enter data for a 1D array (separated by spaces): ")
    num = list(map(int, data.split()))
    print("Data has been stored successfully!")


# 2. Display Data
def display_summary():
    '''Display basic data summary.'''
    print("\nData summary")
    print("Total elements :", len(num))
    print("Minimum value:", min(num))
    print("Maximum value:", max(num))
    print("Sum of all values:", sum(num))

    average = sum(num) / len(num)
    print("- Average value:", round(average, 2))


# 3. Find factorial
def factorial(n):
    '''Calculate factorial using recursion.'''
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


# 4. Filter data
def filter_data():
    '''Filter values using lambda function.'''
    filter_no = int(input(
        "Enter a threshold value to filter out data above this value: "
    ))

    print("Filtered Data(Values>=", filter_no, "):")

    result = list(filter(lambda x: x >= filter_no, num))
    print(", ".join(map(str, result)))


# 5. Sorting data
def sort_data():
    '''Sort data in ascending or descending order.'''

    print("\nChoose Sorting option:")
    print("\n1. Ascending")
    print("\n2. Descending")

    choice = input("Enter your choice: ")

    if choice == "1":
        result = sorted(num)
        print("\nSorted Data in Ascending Order:")
        print(", ".join(map(str, result)))

    elif choice == "2":
        result = sorted(num, reverse=True)
        print("\nSorted Data in Descending Order:")
        print(", ".join(map(str, result)))

    else:
        print("Invalid choice")


# 6. Return Multiple Values
def statistics():
    """Return multiple statistics of the dataset."""

    minimum = min(num)
    maximum = max(num)
    total_sum = sum(num)
    average = total_sum / len(num)

    # Using *args
    values = show_values(minimum, maximum, total_sum, average)

    # Using **kwargs
    summary = show_summary(
        minimum=minimum,
        maximum=maximum,
        total_sum=total_sum,
        average=average
    )

    return values


# *args
def show_values(*args):
    """Handle multiple values using *args."""
    return args


# **kwargs
def show_summary(**kwargs):
    """Handle summary using **kwargs."""
    return kwargs


while True:

    print("\nMain Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")

    choice = input("Please enter your choice: ")

    if choice == "1":
        input_data()

    elif choice == "2":
        display_summary()

    elif choice == "3":
        n = int(input("\nEnter a number to calculate its factorial: "))
        print("\nFactorial of", n, "is:", factorial(n))

    elif choice == "4":
        filter_data()

    elif choice == "5":
        sort_data()

    elif choice == "6":
        minimum, maximum, total_sum, average = statistics()

        print("\nDataset Statistics:")
        print("- Minimum value:", minimum)
        print("- Maximum value:", maximum)
        print("- Sum of all values:", total_sum)
        print("- Average value:", round(average, 2))

    elif choice == "7":
        print("\nThank you for using the Data Analyzer and Transformer Program. Goodbye!")
        break

    else:
        print("Invalid choice!")