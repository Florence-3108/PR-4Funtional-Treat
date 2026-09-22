print("Welcome to the Data Analyzer and Transformer Program")

data = []
data_type = ""
dataset_summary = {}

def input_data():
    """Take 1D or 2D list input from the user."""

    global data_type

    print("\nChoose Data type:")
    print("1. 1D List")
    print("2. 2D List")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        values = input("\nEnter data for a 1D array (seperated by spaces): ")
        data = list(map(int, values.split()))
        data_type = "1D"

    elif choice == 2:
        rows = int(input("\nEnter number of rows: "))
        cols = int(input("Enter number of columns: "))

        data = []

        for i in range(rows):
            row = list(map(int, input("\nEnter values for row " + str(i + 1) + ": ").split()))
            data.append(row)

            data_type = "2D"

    else:
        print("Invalid Choice.")
        return []
        
    print("\nData has been stored successfully!")
    return data

def get_values(data):
    """Convert 1D or 2D Data into a single list od values."""

    if data_type == "1D":
        return data
    else: 
        values = []

        for row in data:
            for value in row:
                values.append(value)
        return values
        

def summary(data):
    """Display basic data summary using built-in functions."""

    values = get_values(data)

    print("\nData Summary: ")
    print("- Total elements: ", len(values))
    print("- Minimum value: ", min(values))
    print("- Maximum value: ", max(values))
    print("- Sum of all value: ", sum(values))
    print("- Average value: ", round(sum(values) / len(values), 2))

def factorial(n):
    """Calculate Factorial using recurrsion."""

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

def filter_data(data, threshold):
    """Filter Values above or equal to a given threshold."""

    values = get_values(data)

    filtered = list(filter(lambda x: x >= threshold, values))

    return filtered

def sort_data(data, choice):
    """Sorting 1D and 2D data in Ascending or Descending order."""

    if data_type == "1D":
        new_data = data.copy()

        if choice == 1:
            new_data.sort()
        else:
            new_data.sort(reverse=True)
        return new_data

    else:
        if choice == 1:
            new_data = sorted(data)
        else: 
            new_data = sorted(data, reverse=True)
        return new_data

def statistics(*args, **kwargs):
    """Calculate and return multiple statistics using *args and *kwargs."""

    minimum = min(args)
    maximum = max(args)
    total = sum(args)
    average = total / len(args)

    print("\n" + kwargs.get("title", "statistics"))

    return minimum, maximum, total, average

def update_global_summary(data):
    """Store dataset in a summary global variable."""

    global dataset_summary
    values = get_values(data)

    dataset_summary = {
        "Total" : len(values),
        "Minimum" : min(values),
        "Maximum" : max(values),
        "Sum" : sum(values),
        "Average" : round(sum(values) / len(values), 2),
    }

def display_2d(data):
    for row in data:
        for values in row:
            print(values, end="\t")
        print()

while True:

    print("\n Main Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in functions)")
    print("3. Calculate Factorial (Recurrsion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return multple values)")
    print("7. Exit Program")

    choice = int(input("Please enter your choice: "))

    if choice == 1:

        data = input_data()

        if len(data) > 0:
            update_global_summary(data)

    elif choice == 2:

        if len(data) == 0:
            print("\nPlease enter data.")
        else:
            summary(data)

    elif choice == 3:

        number = int(input("\nEnter a number to calculate its factorial: "))

        if number < 0:
            print("Factorial is not possible for negative numbers.")
        else:
            result = factorial(number)
            print(f"Factorial of {number} is: {result}")

    elif choice == 4:

        if len(data) == 0:
            print("\nPlease enter data.")
        else:
            threshold = int(input("\nEnter a threshold value to filter out data above this value: "))
            filtered = filter_data(data, threshold)

            print("\nFiltered Data (values >= " + str(threshold) + "): ")
            print(*filtered, sep=", ") 

    elif choice == 5:

        if len(data) == 0:
            print("\nPlease enter data.")
        else:
            print("\nChoose sorting option: ")
            print("1. Ascending")
            print("2. Decending")

            sort_choice = int(input("Enter your choice: "))

            if sort_choice == 1 or sort_choice == 2:
                sorted_data = sort_data(data, sort_choice)

                if data_type == "1D":
                    if sort_choice == 1:
                        print("\nSorted Data in Ascending order:")
                    else:
                        print("\nSorted data in Decending order: ")

                    print(", ".join(map(str, sorted_data)))

                else:
                    if sort_choice == 1:
                        print("\n2D Data Sorted in Ascending order: ")
                    else: 
                        print("\n2D Data Sorted in Descending order: ")

                    display_2d(sorted_data)

            else:
                print("Invalid sorting choice.")

    elif choice == 6:

        if len(data) == 0:
            print("\nPlease enter data.")
        else:
            values = get_values(data)

            minimun, maximum, total, average = statistics(*values, title="Dataset Statistics: ")
            print("- Minimum value: ", minimun)
            print("- Maximum value: ", maximum)
            print("- Sum of all value: ", total)
            print("- Average value: ", round(average, 2))

    elif choice == 7:
        print("\nThank you for using the Data Analyzer and Transformer Program. Goodbye!")
        break

    else:
        print("\nInvalid choice. Please try again.")