contemporary_file_name = "contemporary_file.txt"

class Operation:
    """It means operation"""

    def __init__(self):
        self.origin = 0

    def store_numbers(self):
        number_list = []
        message = f"\nEnter numbers,but do not enter other words."
        message += f"\nEnter 'q' to stop number."
        print(message)
        while True:
            item = input("Now enter you numbers:")
            if item == 'q':
                break
            else:
                number_list.append(str(item))
        with open(contemporary_file_name, 'w') as file:
            for i in number_list:
                file.write(str(i) + "\n")
        long = len(number_list)
        print(f"You have entered {long} numbers:")
        print(number_list)

    def count_arithmetic_mean(self):
        with open(contemporary_file_name, 'r') as file:
            lines = []
            for line in file:
                lines.append(line)
            s = 0
            long = len(lines)
            text = [line.strip("\n") for line in lines]
            for line in text:
                s += int(line)
            value = s / long
        print(f"You have entered {long} numbers.")
        print("This is the sum fo your numbers:")
        print(s)
        print("\nThis is the arithmetic mean of your numbers:")
        print(value)

    def count_geometric_mean(self):
        with open(contemporary_file_name, 'r') as file:
            lines = []
            for line in file:
                lines.append(line)
            text = [line.strip("\n") for line in lines]
            s = 1
            for line in text:
                s = s * float(line)
            m = int(len(lines))
            k = s ** (1/m)
        long = len(lines)
        print(f"You have entered {long} numbers.")
        print("This is the product of your numbers:")
        print(s)
        print("\nThis is the geometric mean of your numbers:")
        print(k)

   











