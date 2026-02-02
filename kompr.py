# Compare any two CSV files. Currently it only works for one row. V1.0 / MrAkihiro 

import csv

# Function to load a CSV file (first column)
def load_csv(filename):
    data = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row:  # Ignore empty rows
                data.append(row[0].strip())
    return data

# Function to compare two lists (case-insensitive)
def compare_lists(list_a, list_b):
    a_lower = {item.lower(): item for item in list_a}
    b_lower = {item.lower(): item for item in list_b}

    only_in_a = [a_lower[k] for k in a_lower if k not in b_lower]
    only_in_b = [b_lower[k] for k in b_lower if k not in a_lower]

    return only_in_a, only_in_b

# Function to write differences to a CSV file
def write_csv(only_in_a, only_in_b, filename='differences.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['In A but not in B', 'In B but not in A'])
        max_len = max(len(only_in_a), len(only_in_b))
        for i in range(max_len):
            a_item = only_in_a[i] if i < len(only_in_a) else ''
            b_item = only_in_b[i] if i < len(only_in_b) else ''
            writer.writerow([a_item, b_item])

def main():
    # Load CSV files
    file_a = 'fruits_a.csv'
    file_b = 'fruits_b.csv'
    
    list_a = load_csv(file_a)
    list_b = load_csv(file_b)
    
    # Compare lists
    only_in_a, only_in_b = compare_lists(list_a, list_b)
    
    # Print results to terminal
    print("In A but not in B:")
    for item in only_in_a:
        print(f"  {item}")
    
    print("\nIn B but not in A:")
    for item in only_in_b:
        print(f"  {item}")
    
    # Write differences to CSV
    write_csv(only_in_a, only_in_b)
    print("\nDifferences have been saved to 'differences.csv'.")

if __name__ == "__main__":
    main()
