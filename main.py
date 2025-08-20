
def file_read_write_challenge(input_file, output_file):
    try:
        with open(input_file, "r") as infile:
            content = infile.read()

        modified_content = content.upper()

        with open(output_file, "w") as outfile:
            outfile.write(modified_content)

        print(f"Successfully created {output_file} with modified content.")

    except FileNotFoundError:
        print(f" << Error >> The file '{input_file}' does not exist.")
    except PermissionError:
        print(f" << Error >>: You don't have permission to read '{input_file}'.")
    except Exception as e:
        print(f"Unexpected error: {e}")


def error_handling_lab():
    filename = input("Enter the filename you want to read: ")

    try:
        with open(filename, "r") as f:
            print("File content:\n")
            print(f.read())

    except FileNotFoundError:
        print(f"<< Error >>: File '{filename}' not found.")
    except PermissionError:
        print(f"<< Error >>: You don't have permission to access '{filename}'.")
    except Exception as e:
        print(f"nexpected error: {e}")


if __name__ == "__main__":
    file_read_write_challenge("input.txt", "output.txt")

    error_handling_lab()
