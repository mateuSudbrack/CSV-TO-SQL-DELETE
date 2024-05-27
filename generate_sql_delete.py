import sys
import csv

def generate_sql_delete(input_file, output_file, column_name):
    # Open the CSV file
    with open(input_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)

        # Open the output file
        with open(output_file, 'w') as f:
            for row in reader:
                value = row[column_name]
                sql_command = f"DELETE FROM `TABLE` WHERE {column_name} = '{value}';\n"
                f.write(sql_command)

    print("SQL commands generated successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py input_file.csv output_file.sql column_name")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    column_name = sys.argv[3]

    generate_sql_delete(input_file, output_file, column_name)
