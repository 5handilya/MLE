# Tokenizer Projects Learning Path by DeepSeek R1

From basic text splitting to advanced ML tokenizers, with implementation checklists and blogging tasks.

## Level 1: Basic Tokenizers

### 1.1 Whitespace Tokenizer
- Split text by whitespace
- [x] Handle multiple spaces
- [x] Basic punctuation handling
- [x] Python implementation
- [ ] Rust implementation
- [ ] Documented

### 1.2 Character-Level Tokenizer
- Split text into individual characters
- [ ] Handle Unicode characters
- [ ] Basic stats (char frequency)
- [ ] Python implementation
- [ ] Rust implementation
- [ ] Documented

## Level 2: Intermediate Tokenizers

### 2.1 Regex-Based Tokenizer
- Implement regex patterns for word separation
- Handle contractions (e.g., "don't")
- Capture special tokens (URLs, emails)
- [ ] Python implementation (`re` module)
- [ ] Rust implementation (`regex` crate)
- [ ] Documented

### 2.2 Vocabulary-Based Tokenizer
- Build vocabulary from corpus
- Handle OOV tokens
- Add special tokens ([UNK], [PAD])
- [ ] Python implementation
- [ ] Rust implementation
- [ ] Documented

## Level 3: Subword Tokenizers

### 3.1 Byte Pair Encoding (BPE)
- Implement BPE training
- Merge operations
- Encoding/decoding logic
- [ ] Python implementation (numpy/pure Python)
- [ ] Rust implementation (rayon for parallelism)
- [ ] Documented

### 3.2 WordPiece Tokenizer
- Implement likelihood-based merging
- Handle subword ambiguity
- [ ] Python implementation
- [ ] Rust implementation
- [ ] Documented

### 3.3 SentencePiece Unigram
- Implement unigram language model
- Probabilistic subword selection
- [ ] Python implementation
- [ ] Rust implementation
- [ ] Documented

## Level 4: Production-Grade Tokenizers

### 4.1 Unicode Normalization
- [ ] Implement NFC/NFD normalization
- [ ] Python implementation (`unicodedata`)
- [ ] Rust implementation (`unicode-normalization`)
- [ ] Documented

### 4.2 Pre-tokenization Pipeline
- Combine multiple strategies:
  - Whitespace splitting
  - Punctuation separation
  - Regex rules
- [ ] Python implementation
- [ ] Rust implementation
- [ ] Documented

## Level 5: Advanced ML Integration

### 5.1 Tensor/Serialization Support
- Convert tokens to PyTorch/TensorFlow tensors
- Implement padding/truncation
- [ ] Python implementation
- [ ] Rust implementation (with ONNX support)
- [ ] Documented

### 5.2 Parallel Tokenization
- Implement multithreaded preprocessing
- Batch processing optimizations
- [ ] Python implementation (Ray/multiprocessing)
- [ ] Rust implementation (tokio async)
- [ ] Documented

## Level 6: State-of-the-Art (SoTA)

### 6.1 BBPE (Byte-level BPE)
- Implement GPT-style byte-level encoding
- Handle BOM (Byte Order Mark)
- [ ] Python implementation
- [ ] Rust implementation
- [ ] Documented

### 6.2 Tiktoken-Style Tokenizer
- Implement cl100k_base equivalent
- Optimize for speed with caching
- [ ] Python implementation
- [ ] Rust implementation
- [ ] Documented

### 6.3 Distributed Tokenizer Training
- Implement sharded vocabulary building
- Merge partial vocabularies
- [ ] Python implementation (PySpark/Dask)
- [ ] Rust implementation (Rayon distributed)
- [ ] Documented

## Level 7: Specialized Tokenizers

### 7.1 Multimodal Tokenizer
- Combine text/image tokens
- Implement CLIP-style tokenization
- [ ] Python implementation
- [ ] Rust implementation
- [ ] Documented

### 7.2 Biological Sequence Tokenizer
- Handle DNA/protein sequences
- Implement k-mer tokenization
- [ ] Python implementation
- [ ] Rust implementation
- [ ] Documented

## Final Challenge

### Hugging Face Tokenizers Library Clone
- Reimplement core features:
  - Normalizers
  - PreTokenizers
  - Models (BPE/WordPiece/Unigram)
  - PostProcessors
- [ ] Python implementation
- [ ] Rust implementation
- [ ] Documented
