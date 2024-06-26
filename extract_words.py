
def get_examples(file_path):
    # Initialize an empty list to hold the extracted data
    data = []

    # Open the file for reading
    with open(file_path, 'r', encoding='utf-8') as file:
        # Iterate over each line in the file
        for line in file:
            # Strip whitespace from the beginning and end of the line
            line = line.strip()
            
            # Split the line into word and example parts
            parts = line.split(' - ')
            
            # Check if the line was correctly formatted
            if len(parts) == 2:
                # Extract the word and example, removing quotes from the example
                # the word part is ignored for now
                word, example = parts[0], parts[1].strip('"')

                # Append a tuple of word and example to the data list
                data.append(example)

    return data
