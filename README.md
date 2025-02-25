# Medibank Code Challange

# Overview
Sort through a list of files in a folder structure

This script scans a specified directory and its subdirectories for text files (.txt), extracts words, 
and counts their occurrences. It then displays words that appear more than twice, sorted in descending order.

# Requirements:
- Python 3.x

## Usage:
1. Run the script: `python wordcount.py`
2. Enter the directory path when prompted.
3. Enter the file format (e.g., `.txt`, `.log`) when prompted.
4. The script will process all files with the specified extension in the directory and subdirectories. 
5. The word frequencies will be displayed in descending order.

## Functions:
- `count_strings_in_directory(directory_path)`: Counts words in files with the specified format and returns a dictionary of words with their occurrences.
- `output_sorted_results(counts)`: Sorts and prints words with their occurrence counts.

### Example Output:
```
hello: 10
world: 8
python: 5
```

### Notes:
- The script converts text to lowercase for case-insensitive counting.
- Only words (alphanumeric strings) are considered.
- Words occurring more than twice are included in the output.
- The script handles errors when files cannot be read or directories are invalid.
