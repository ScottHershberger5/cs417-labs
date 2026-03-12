"""Word counter using argparse."""
import argparse
from collections import Counter


def build_parser():
    """Create and return the argument parser."""
    parser = argparse.ArgumentParser(description="Word counting argument")
    parser.add_argument("filename", type=str, help="The text file to analyze")
    parser.add_argument("--ignore-case", "-i", action="store_true",
                        help="Lowercase all words before counting")
    parser.add_argument("--top", "-t", type=int, default=None,
                        help="Show top N most frequent words")
    parser.add_argument("--min-length", "-m", type=int, default=1,
                        help="Only count words with at least this many characters")
    parser.add_argument("--sort-by", "-s", choices=["freq", "alpha"], default="freq",
                        help='Sort top words by "freq" or "alpha"')
    parser.add_argument("--reverse", "-r", action="store_true",
                        help="Reverse the sort order")
    return parser


def analyze(filepath, ignore_case=False, top=None, min_length=1,
            sort_by="freq", reverse=False):
    """Analyze a text file and return a formatted result string."""
    with open(filepath, "r") as file:
        words = file.read().split()

    if ignore_case:
        words = [word.lower() for word in words]

    words = [word for word in words if len(word) >= min_length]
    total_words = len(words)

    if top is None:
        return f"{filepath}: {total_words} words"

    counts = Counter(words)

    if sort_by == "freq":
        items = counts.most_common()
    else:  # alpha
        items = sorted(counts.items(), key=lambda item: item[0])

    if reverse:
        items.reverse()

    items = items[:top]

    output = f"{filepath}: {total_words} words\n\nTop {top} words:\n"
    for word, count in items:
        output += f"  {word}: {count}\n"

    return output


def main():
    """Build parser, parse args, analyze, print result."""
    parser = build_parser()
    args = parser.parse_args()

    result = analyze(
        args.filename,
        ignore_case=args.ignore_case,
        top=args.top,
        min_length=args.min_length,
        sort_by=args.sort_by,
        reverse=args.reverse
    )
    print(result)


if __name__ == "__main__":
    main()