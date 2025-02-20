def get_stats(vocab):
    pairs = {}
    for pair in zip(ids, ids[1:]):
        pairs[pair] = pairs.get(pair, 0) + 1
    return pairs

def merge(input_ids, repl_target, new_id):
    new_input_ids = []
    for i in range(len(input_ids)):
        if i < len(input_ids) - 1 and ((input_ids[i], input_ids[i+1]) == repl_target):
            new_input_ids.append(new_id)
            i+=1
        else:
            new_input_ids.append(input_ids[i])
    return new_input_ids

print(merge([5,6,6,7,9,1],(6,7),99))

#text = """Successful people tend to be persistent. New ideas often don't work at first, but they're not deterred. They keep trying and eventually find something that does."""
text = "aaaaaaabcbcd"
tokens = text.encode("utf-8")
#print(tokens[:50])
tokens = list(map(int,tokens))
#print(tokens[:50])
vocab_size = 276 # imp HP 
num_merges = vocab_size - 256
ids = list(tokens)
merges = {}
for i in range(num_merges):
    stats = get_stats(ids)
    print(stats)
    pair = max(stats, key=stats.get)
    print(f"most common pair = {chr(pair[0]), chr(pair[1])}")
    idx = 256 + i
    print(f"merging {pair} into a new token {idx}")
    ids = merge(ids, pair, idx)
    merges[pair] = idx
