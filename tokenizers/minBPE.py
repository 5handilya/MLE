text = """Successful people tend to be persistent. New ideas often don't work at first, but they're not deterred. They keep trying and eventually find something that does."""
# text = "aaaaaaabcbcd"
tokens = text.encode("utf-8")
#print(tokens[:50])
tokens = list(map(int,tokens))
#print(tokens[:50])

def get_freqs(ids):
    freqs = {}
    for pair in zip(ids, ids[1:]):
        freqs[pair] = freqs.get(pair, 0) + 1
    return freqs 

def merge(input_seq, merge_target, merge_payload):
    output_seq = []
    i = 0
    while i < len(input_seq):
        if (i < len(input_seq) - 1) and ((input_seq[i] , input_seq[i+1]) == merge_target):
            output_seq.append(merge_payload)
            i += 2
        else:
            output_seq.append(input_seq[i])
            i += 1
    return output_seq

target_vocab_size = 300
idx = 256
num_merges = target_vocab_size - idx
ids = list(tokens)
merges = {}

for i in range(num_merges):
    freqs = get_freqs(ids)
    most_freq_pair = max(freqs, key=freqs.get)
    print(f"Most frequent pair:{most_freq_pair}")
    ids = merge(ids, most_freq_pair, idx + i)
    print(f"Merged {most_freq_pair} into {idx + i}")

# DECODE
# pre-processing var vocab that turns ints into strings
vocab = {i: bytes([i]) for i in range(idx)}
for (p0, p1), i in merges.items():
    vocab[i] = vocab[p0] + vocab[p1]
def decode(ids):
    tokens = b"".join(vocab[idx] for idx in ids)
    text = tokens.decode("utf-8", errors="replace")
    return text
def encode(text):
    tokens = list(text.encode("utf-8"))
    while True:
        stats = get_freqs(tokens)
        # get the pair that appears earliest in the merges dict
        pair = min(stats, key=lambda p: merges.get(p, float("inf"))) 
        if pair not in merges:
            break #nothing else can be merged
        idx = merges[pair]
        tokens = merge(tokens, pair, idx)
    return tokens
print(encode("hello world"))