#!/usr/bin/python


from sentence_transformers import SentenceTransformer

import sys
import argparse
import csv

"""
Compute sentence embeddings for lines in input, writing them as .csv output.

Smaller model (English): paraphrase-MiniLM-L6-v2
Dutch: NetherlandsForensicInstitute/robbert-2022-dutch-sentence-transformers
"""

# TODO: Add language argument instead of model.

def main():
    args = parse_args()
    writer = csv.writer(sys.stdout)
    model = SentenceTransformer(args.model)
    if args.sentence:
        sentences = [args.sentence]
    else:
        sentences = sys.stdin
    for line in sentences:
        emb = model.encode(line.strip(), show_progress_bar=False)
        writer.writerow(emb)


def parse_args():
    parser = argparse.ArgumentParser(description='Script to compute word/sentence embeddings.')
    parser.add_argument('sentences', nargs='?', type=argparse.FileType('r'), default=sys.stdin, help='Sentence to process, default stdin.')
    parser.add_argument('--model', type=str, default='distiluse-base-multilingual-cased-v1', help='Embedding model to use')
    args = parser.parse_args()

    if args.sentences == '-':
        args.sentences = sys.stdin
    return args


if __name__ == '__main__':
    main()
