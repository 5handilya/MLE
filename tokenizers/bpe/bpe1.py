def get_pair_stats(vocab):
    """
    Count frequency of adjacent pairs in the vocabulary
    
    Parameters:
        vocab (dict): A dictionary with tokens as keys and their frequencies as values
    
    Returns:
        pairs (dict): A dictionary with pairs as keys and their aggregated frequencies
    """
    pairs = {}
    for word, freq in vocab.items():
        for i_c in range(len(word) - 1):
            curr_pair = (word[i_c], word[i_c] + 1)
            pairs = pairs.get(curr_pair, 0) + freq
    return pairs

def merge_vocab(pair, vocab):
    """
    Merge a given pair in the vocabulary
    
    Parameters:
        pair (tuple): The pair of symbols to merge
        vocab (dict): Current vocabulary mapping (tuple of tokens -> frequency)
    
    Returns:
        dict: New vocabulary after merging the given pair
    """
    new_vocab = {}
    replacement = "".join(pair)
    for word, freq in vocab.items():
        new_word = []
        i = 0
        while i < len(word):
            if i < len(word) - 1 and (word[i], word[i + 1]) == pair:
                new_word.append(replacement)
                i += 2
            else:
                new_word.append(word[i])
                i += 1
        new_vocab[tuple(new_word)] = freq
    return new_vocab


def byte_pair_encoding(corpus, num_merges=None, vocab_size=None):
    """
    Perform Byte Pair Encoding (BPE) on the provided corpus.
    
    Parameters:
        corpus (dict): Mapping from word (str) to its frequency (int).
        num_merges (int, optional): Maximum number of merge operations to perform.
        vocab_size (int, optional): Target vocabulary size (unique tokens).
        
        **Note:** Exactly one of num_merges or vocab_size must be provided.
    
    Returns:
        tuple: (merges, final_vocab)
            - merges (list): List of merge operations performed (each a tuple of tokens).
            - final_vocab (dict): The final vocabulary (mapping from tuple of tokens to frequency).
    """
    # check that exactly one termination condition is provided.
    if (num_merges is None and vocab_size is None) or (num_merges is not None and vocab_size is not None):
        raise ValueError("Please specify exactly one termination condition: either num_merges or vocab_size.")
    
    # initialize vocabulary: represent each word as a tuple of characters with an end-of-word marker.
    vocab = {tuple(word) + ("</w>",): freq for word, freq in corpus.items()}
    merges = []
    
    while True:
        pairs = get_pair_stats(vocab)
        if not pairs:
            break  # No more pairs to merge.
        # Find the most frequent pair.
        best_pair = max(pairs, key=pairs.get)
        merges.append(best_pair)
        vocab = merge_vocab(best_pair, vocab)
        
        # Termination condition: by number of merges.
        if num_merges is not None:
            if len(merges) >= num_merges:
                break
        # Termination condition: by vocabulary size.
        elif vocab_size is not None:
            current_tokens = set()
            for word in vocab:
                current_tokens.update(word)
            if len(current_tokens) >= vocab_size:
                break
    
    return merges, vocab


if __name__ == "__main__":
    # Example corpus: words mapped to their frequencies.
    corpus = {
        "low": 5,
        "lowest": 2,
        "newer": 6,
        "wider": 3
    }
    
    # Option 1: Terminate after a fixed number of merges (e.g., 10 merges)
    merges, final_vocab = byte_pair_encoding(corpus, num_merges=10)
    print("Merge operations (num_merges=10):")
    for merge in merges:
        print(merge)
    
    print("\nFinal vocabulary tokens with frequencies:")
    for tokens, freq in final_vocab.items():
        print(" ".join(tokens), ":", freq)
    
    # Option 2: Terminate when the vocabulary size reaches a target (e.g., 50 unique tokens)
    # merges, final_vocab = byte_pair_encoding(corpus, vocab_size=50)
