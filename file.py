def process_text_file(input_file="input.txt", output_file="output.txt"):
    """
    Reads a file, counts words, converts the text to uppercase,
    and writes the processed text and word count to a new file.
    """
    try:
        with open(input_file,"r",encoding="utf-8") as file:
            text=file.read().strip()

        # Count the number of words
        words = text.split()
        word_count=len(words)

        # Convert the text to uppercase
        upper_text = text.upper()


        # Write the processed text and word count to the output file
        with open(output_file,"w", encoding="utf-8") as f_out:
            f_out.write("Processed Text:\n") 
            f_out.write(upper_text)
            f_out.write("\n\nWord Count: {}\n".format(word_count))
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")

process_text_file()