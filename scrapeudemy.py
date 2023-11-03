import csv
from prettytable import PrettyTable

def load_courses_from_csv(filename):
    """Load courses from a CSV file."""
    courses = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            courses.append(row)
    return courses

def display_courses(courses):
    """Display courses in a neat table format using PrettyTable."""
    table = PrettyTable()
    
    # Set table headers
    table.field_names = ["ID", "Title", "URL", "Is Paid", "Price", "Professor", "Description", "Subscribers"]

    # Add rows to the table
    for course in courses:
        table.add_row(course)
    
    print(table)

def main():
    csv_filename = "udemy2.csv"
    courses = load_courses_from_csv(csv_filename)
    display_courses(courses)

if __name__ == "__main__":
    main()
