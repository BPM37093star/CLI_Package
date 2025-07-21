# Student Name: Zheng Pei
# Matriculation Number: 24-747-818

from levenshtein_base import levenshtein
import argparse
import sys

def parse_args():
    """
    Parse command line arguments.
    """

    parser = argparse.ArgumentParser(description="Calculate Levenshtein distance between two files.")
    
   
    parser.add_argument("--file1", type=str, required=True, help="Path to the first file.")
    parser.add_argument("--file2", type=str, required=True, help="Path to the second file.")
    
    
    parser.add_argument("--weights", type=int, nargs=3, default=[1, 1, 1], 
                        metavar=("INSERT", "DELETE", "REPLACE"),
                        help="Weights for insertion, deletion, and substitution operations. Default is [1, 1, 1].")
    

    parser.add_argument("--tokenize", action='store_true', 
                        help="If provided, calculate the Levenshtein distance on token level (default is character level).")
    
    args = parser.parse_args()
    if any(weight < 0 for weight in args.weights):
        raise ValueError("Weights should not be negative.")   
    
    return args

def read_and_tokenize(file_path):
    """
    Read a file and tokenize its content into words.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            words = []
            for word in content.split():
                word = word.strip()
                if word:
                    words.append(word)
            return words
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error reading '{file_path}': {e}", file=sys.stderr)
        sys.exit(1)

def compare_word_by_word(words1, words2, weights):
    """
    Compare two lists of words and calculate the Levenshtein distance for each pair.
    """
    max_len = max(len(words1), len(words2))
    words1 += [''] * (max_len - len(words1))
    words2 += [''] * (max_len - len(words2))

    for w1, w2 in zip(words1, words2):
        distance = levenshtein(w1, w2, 
                               insertion_cost=weights[0],
                               deletion_cost=weights[1],
                               substitution_cost=weights[2])
        print(f"{w1 or '<empty>'}\t{w2 or '<empty>'}\t{distance}")

    
def main():
    """
    Main function to handle command line arguments and execute the comparison.
    """
    try:
        args = parse_args()
        words1 = read_and_tokenize(args.file1)
        words2 = read_and_tokenize(args.file2)
        compare_word_by_word(words1, words2, args.weights)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    
if __name__ == "__main__":
    main()