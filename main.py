import sys
from stats import get_book_text
from stats import get_character_stats
from stats import sort_dict

sys.argv

if len(sys.argv) > 1:
    filepath = " ".join(sys.argv[1:])
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    get_book_text(filepath)
    character_stats = get_character_stats(filepath)
    sort_dict(character_stats)


main()
