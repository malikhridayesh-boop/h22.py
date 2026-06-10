def print_mirrored_triangle():
    print("--- Mirrored Triangle Project ---")
    
    try:
        rows = int(input("Enter the number of rows for your triangle: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    print("\nGenerating your mirrored triangle:\n")
    
    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        stars = "*" * i
        
        print(spaces + stars)

if __name__ == "__main__":
    print_mirrored_triangle()