import sys
from urllib.parse import quote

def encode_url(input_filename, output_filename, replacement):
    try:
        with open(input_filename, 'r') as input_file:
            content = input_file.read()

            # Applying URL encoding to the replacement text
            encoded_replacement = quote(replacement)

            # Replace the placeholder
            updated_content = content.replace('<REPLACE HERE>', encoded_replacement)

        # Writing to the output file
        with open(output_filename, 'w') as output_file:
            output_file.write(updated_content)

        print(f'Successfully replaced placeholder in {input_filename} and saved to {output_filename}.')

    except FileNotFoundError:
        print(f'File {input_filename} not found.')
    except Exception as e:
        print(f'An error occurred: {str(e)}')

# Main program
if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: python msc_dropper.py <input_filename> <output_filename> <replacement>')
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    replacement = sys.argv[3]

    # Applying URL encoding to the replacement text and writing to the output file
    encode_url(input_filename, output_filename, replacement)
