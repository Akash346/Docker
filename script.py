import os
import socket
from collections import Counter

# Define the file paths
file1_path = "/home/data/IF.txt"
file2_path = "/home/data/AlwaysRememberUsThisWay.txt"
output_path = "/home/data/output/result.txt"

# Ensure the output directory exists
try:
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    print("Output directory created successfully")
except Exception as e:
    print(f"Error creating directory: {e}")

# Function to read a file and return word counts
def read_and_count_words(file_path, handle_contractions=False):
    with open(file_path, 'r') as file:
        text = file.read().lower()
        if handle_contractions:
            # Handle contractions by splitting them
            words = text.replace("'", " ").split()
        else:
            words = text.split()
        word_count = Counter(words)
    return word_count

# Process both files
if_word_count = read_and_count_words(file1_path)
always_word_count = read_and_count_words(file2_path, handle_contractions=True)

# Calculate the total word counts
total_words_if = sum(if_word_count.values())
total_words_always = sum(always_word_count.values())
grand_total_words = total_words_if + total_words_always

# Get the top 3 most frequent words in each file
top3_if = if_word_count.most_common(3)
top3_always = always_word_count.most_common(3)

# Get the IP address of the machine running the container
ip_address = socket.gethostbyname(socket.gethostname())

# Write the results to the output file
try:
    with open(output_path, 'w') as output_file:
        output_file.write(f"Total words in IF.txt: {total_words_if}\n")
        output_file.write(f"Total words in AlwaysRememberUsThisWay.txt: {total_words_always}\n")
        output_file.write(f"Grand total of words across both files: {grand_total_words}\n")
        output_file.write(f"Top 3 words in IF.txt: {top3_if}\n")
        output_file.write(f"Top 3 words in AlwaysRememberUsThisWay.txt (with contractions handled): {top3_always}\n")
        output_file.write(f"Container IP address: {ip_address}\n")
    print("Results written to result.txt successfully")
except Exception as e:
    print(f"Error writing to file: {e}")

# Print the results to the console
with open(output_path, 'r') as result_file:
    print(result_file.read())
