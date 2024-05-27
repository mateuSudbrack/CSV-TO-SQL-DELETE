import sys
import csv

def generate_sql_delete(input_file, output_file, table_name, column_name):
    # Open the CSV file
    with open(input_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)

        # Open the output file
        with open(output_file, 'w') as f:
            # Iterate through each row in the CSV file
            for row in reader:
                # Extract the value from the specified column
                value = row[column_name]
                # Generate the SQL delete command
                sql_command = f"DELETE FROM `{table_name}` WHERE {column_name} = '{value}';\n"
                # Write the SQL command to the output file
                f.write(sql_command)

    print("SQL commands generated successfully.")

if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: python script.py input_file.csv output_file.sql table_name column_name")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    table_name = sys.argv[3]
    column_name = sys.argv[4]

    generate_sql_delete(input_file, output_file, table_name, column_name)
