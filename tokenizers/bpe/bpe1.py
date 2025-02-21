
########################################################## OVERVIEW #######################################################
#
#       I.   Training :      Learn merge rules from training corpus
#       II.  Encoding :      Apply all learned rules to input
#       III. Testing  :      (TODO) Track OOVs & perf profiling
#
############################################################# LIB #########################################################

class BPETokenizer:

    # Train BPE on a corpus of texts
    def train(self, texts):

        # 0. Pre-processing
        ids = self._pre_process(texts)

        # 1. Initialize vocabulary
        self._initialize_vocab(ids)

        # 3. Learn merge rules. Terminal condition = target vocab size specified at init
        while len(self.vocab) < self.target_vocab_size:
            pair_freqs      = self._count_token_pairs(ids)
            most_freq_pair  = max(pair_freqs, key=pair_freqs.get)
            new_token_id    = len(self.vocab)
            ids             = self._merge_pair(ids, most_freq_pair, new_token_id)
            self._learn_merge_rule(most_freq_pair, new_token_id)
            print(f"Vocab size: {len(self.vocab)}, target: {self.target_vocab_size}")

    def encode(self, text):
        # Convert text to a list of byte values (initial token IDs)
        text_bytes = text.encode("utf-8")
        ids = list(text_bytes)
        # Iteratively apply merge rules until no more merges can be performed
        while len(ids) >= 2: # For sanity, the real break comes from the membership check below
            # Count occurrences of adjacent token pairs
            pair_freqs = self._count_token_pairs(ids)
            # Identify the earliest mergeable pair in pair_freqs by checking the lowest matching merge rule index
            first_pair_to_merge = min(pair_freqs, key=lambda p: self.merge_rules.get(p, float("inf")))
            # Stop merging if the identified pair is not in the merge rules - no more merges possible
            if first_pair_to_merge not in self.merge_rules:
                break
            # Apply the merge
            merged_id = self.merge_rules[first_pair_to_merge]
            ids = self._merge_pair(ids, first_pair_to_merge, merged_id)
        return ids

    def decode(self, ids):
        # decode the byte sequence corresponding to ids in vocab using utf-8
        text_bytes = b"".join(self.vocab[id] for id in ids)
        text = text_bytes.decode("utf-8", errors="replace")
        return text

# internals -----------------------------------------------------------------------------------------------------------------

    def __init__(self, target_vocab_size):
        # Initialize the tokenizer with target vocabulary size as the terminal condition
        self.target_vocab_size = target_vocab_size
        self.vocab = {}  # token id -> byte mapping
        self.inverse_vocab = {}  # byte -> id mapping
        self.merge_rules = {}  # stores learned BPE merge rules (int, int) : int which will be used for encoding

    def _pre_process(self, texts):
        # Simple pp for now -- split into chars, turn into ints
        # cant handle punctuation etc properly 
        concat = "".join(("".join(texts)).split())
        encoded_corpus = concat.encode("utf-8")
        ids = list(encoded_corpus)
        return ids

    def _count_characters(self, texts):
        # Count frequency of each character in the given text
        freqs = {}
        for word in texts:
            for char in word:
                freqs[char] = freqs.get(char, 0) + 1
        return freqs

    def _initialize_vocab(self, ids):
        # Initialize a id : byte dict with given ids
        self.vocab = {id: bytes([id]) for id in range(256)}

    def _count_token_pairs(self, ids):
        # Count frequencies of adjacent token pairs
        pair_freqs = {}
        for pair in zip(ids, ids[1:]):
            pair_freqs[pair] = pair_freqs.get(pair, 0) + 1
        return pair_freqs

    def _learn_merge_rule(self, pair, id):
        # Add a new merge rule for pair of ids -> id & update vocabulary
        self.merge_rules[pair] = id
        self.vocab[id] = self.vocab[pair[0]] + self.vocab[pair[1]]

    def _merge_pair(self, tokens, target_pair, new_token):
        # Apply a merge rule to a sequence of tokens
        i = 0
        result = []
        while i < len(tokens):
            if (i < len(tokens) - 1) and ((tokens[i], tokens[i+1]) == target_pair):
                result.append(new_token)
                i += 2
            else:
                result.append(tokens[i])
                i += 1
        return result

################################################## mischief managed ################################################## 