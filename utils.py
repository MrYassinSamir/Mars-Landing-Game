import time

def Write(text):
    for i in text:
        time.sleep(0.1)
        print(i, end='', flush=True)
    print("\n")

def get_float_input(prompt, min_val, max_val):
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"\nPlease enter a value between {min_val} and {max_val}.\n")
        except ValueError:
            print("\nInvalid input! Enter a number.\n")
