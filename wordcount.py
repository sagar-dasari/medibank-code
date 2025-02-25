import os
import re
from collections import Counter

def count_strings_in_directory(directory_path, file_extension):
    """
    Count unique strings in files of a specified format within the given directory and its subdirectories.
    
    Args:
        directory_path (str): The path to the directory to scan for files.
        file_extension (str): The file extension to process (e.g., '.txt', '.log').
        
    Returns:
        dict: A dictionary with words as keys and their occurrence counts as values.
    """
    string_counter = Counter()
    
    if not os.path.isdir(directory_path):
        print("Error: The specified directory does not exist.")
        return {}

    # Traverse the directory and its subdirectories
    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            
            # Process only files with the specified extension
            if file.endswith(file_extension):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read().lower()  # Convert text to lowercase for uniformity
                        
                        # Extract words using regex (matches alphanumeric words)
                        strings = re.findall(r'\b\w+\b', content)
                        
                        # Update the counter with extracted words
                        string_counter.update(strings)
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
            else:
                print(f"Skipping {file_path}: Does not match the specified file format.")

    # Keep only words that appear more than twice
    filtered_strings = {string: count for string, count in string_counter.items() if count > 2}
    return filtered_strings

def output_sorted_results(counts):
    """
    Print the sorted results of word frequencies in descending order.
    
    Args:
        counts (dict): A dictionary of words and their occurrence counts.
    """
    if not counts:
        print("No valid words found matching the criteria.")
        return
    
    # Sort words by occurrence count in descending order
    sorted_counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    
    # Output the list of unique strings with descending order of occurrences next to them
    print("Unique strings and their occurrences:")
    for string, count in sorted_counts:
        print(f"{string}: {count}")

if __name__ == "__main__":
    # Prompt user for the directory path to scan
    directory_to_search = input("Enter the directory path to scan: ")
    
    # Prompt user for the file format to process
    file_format = input("Enter the file format to process (e.g., .txt, .log): ")
    
    # Validate file format input
    if not file_format.startswith('.'):
        print("Error: Invalid file format. Please include a leading dot (e.g., .txt, .log)")
    else:
        # Count word occurrences in the directory
        string_counts = count_strings_in_directory(directory_to_search, file_format)
        
        # Display sorted results
        output_sorted_results(string_counts)
