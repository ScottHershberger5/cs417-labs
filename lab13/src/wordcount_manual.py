"""Word counter using manual sys.argv parsing."""
import sys


def parse_args_manual(argv):
    """Extract filename from argv list.

    If no filename provided, print usage to stderr and exit with code 1.

    Args:
        argv: sys.argv (list of strings)

    Returns:
        str: the filename
    """
    # TODO: Check if argv has at least 2 elements (program name + filename)
    # If not, print "Usage: wordcount_manual.py <filename>" to stderr and exit(1)
    # Otherwise return argv[1]
    if len(sys.argv) >= 2:
        return sys.argv[1]
    else:
        print("Usage: wordcount_manual.py <filename>", file=sys.stderr)
        sys.exit(1)


def count_words(filepath):
    """Read a file and return the number of words.

    Words are defined by splitting on whitespace.

    Args:
        filepath: path to the text file

    Returns:
        int: total word count

    Raises:
        FileNotFoundError: prints error to stderr and exits with code 1
    """
    try:
        file = open(filepath)
        text_w_spaces = file.read()
        no_spaces = text_w_spaces.split()
        return len(no_spaces)

    except:
        print(f"Error: file '{filepath}' not found", file=sys.stderr)
        sys.exit(1)



def main():
    """Wire it together: parse args, count words, print result."""
    # TODO: Call parse_args_manual with sys.argv
    # Call count_words with the filename
    # Print "<filename>: <count> words"
    
    filename = parse_args_manual(sys.argv)
    total_word = count_words(filename)
    print(f"{filename}: {total_word} words")



if __name__ == "__main__":
    main()
