# sembed #

Simple command-line wrapper around [sentence transformers](https://sbert.net/index.html).

## Install ##

`pip install git+https://github.com/mwestera/sembed`

This will make the command `sembed` available in your shell.

## Usage ##

```bash
$ sembed "The quick brown fox jumped over the lazy dog."
```

Slightly faster model (English only) -- see [available models](https://sbert.net/docs/sentence_transformer/pretrained_models.html) -- though many others in the Huggingface model zoo will probably work fine too:

```bash
$ sembed "The quick brown fox jumped over the lazy dog." --model paraphrase-MiniLM-L6-v2
```

Feeding it a file with multiple sentences (one per line), and writing to a .csv file:

```bash
$ sembed < sentences.txt > embeddings.csv
```