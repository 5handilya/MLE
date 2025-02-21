from bpe1 import BPETokenizer

with open('corpus.txt', 'r') as file:
    file_contents = file.read()

training_sample_text_1 = [
    file_contents,
    "The quick brown fox jumps over the lazy dog",
    "Pack my box with five dozen liquor jugs",
    "How vexingly quick daft zebras jump","pan panapan"
    "The five boxing wizards jump quickly" 
]
def demo_bpe(test_text):
    
    test_text = "The quick brown fox" if test_text is None else test_text
    print(f"\nTest encoding/decoding of: \"{test_text}\"")
    
    encoded = tokenizer.encode(test_text)
    print(f"Encoded: {encoded}")
    
    decoded = tokenizer.decode(encoded)
    print(f"Decoded: '{decoded}'")
    
    # Basic stats
    char_length = len(test_text)
    token_length = len(encoded)
    print(f"\nSequence length comparison: \"{test_text}\"")
    print(f"Character-level: {char_length} units")
    print(f"BPE-level: {token_length} units")
    print(f"Compression ratio: {char_length/token_length:.2f}x")

if __name__ == "__main__":
    # Training
    tokenizer = BPETokenizer(target_vocab_size=1000)
    print("Training BPE tokenizer...")
    tokenizer.train(training_sample_text_1)
    
    print("\nFinal vocabulary:")
    for id_, token in tokenizer.vocab.items():
        print(f"ID: {id_} | Token: {bytes(token)}")
    
    print("\nMerge rules learned:")
    for (pair), new_token in tokenizer.merge_rules.items():
        print(f"'{pair}' -> '{new_token}'")
    
    # Interactive testing
    print("Welcome to this BPE tokenizer demo. Input text to check encoding, decoding, and some stats: \n")
    while True:
        demo_bpe(input().strip())
