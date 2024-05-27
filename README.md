# CSV-TO-SQL-DELETE
This Python script generates SQL delete commands from a CSV file based on a specified column.
```
# CSV to SQL Delete Generator

This Python script generates SQL delete commands from a CSV file based on a specified column.

## Usage

1. Install Python (if not already installed).
2. Download the script (`generate_sql_delete.py`) from this repository.
3. Run the script from the command line with the following syntax:
   ```
   python generate_sql_delete.py input_file.csv output_file.sql table_name column_name
   ```
   Replace `input_file.csv` with the path to your input CSV file, `output_file.sql` with the desired path for the output SQL file, and `column_name` with the name of the column containing the values to delete.
4. The script will generate SQL delete commands for each value in the specified column of the input file and save them to the output file.

## Example

Assuming you have an input CSV file named `input.csv` with the following content:

```
ID,Name
1,John
2,Alice
3,Bob
```

Running the script with the command:
```
python generate_sql_delete.py input.csv output.sql Name
```

will generate an output SQL file (`output.sql`) containing the following SQL delete commands:
```
DELETE FROM `TABLE` WHERE Name = 'John';
DELETE FROM `TABLE` WHERE Name = 'Alice';
DELETE FROM `TABLE` WHERE Name = 'Bob';
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
``` 

You can simply copy and paste this content into your README file. Let me know if you need further assistance!
