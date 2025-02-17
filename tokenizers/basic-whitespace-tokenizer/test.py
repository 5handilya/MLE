import timeit
from memory_profiler import profile

def whitespace_tokenizer(text):
	current_token = []
	tokens = []
	for char in text:
		if text.isspace():
			tokens.append(''.join(current_token))
			current_token = []
		else:
			current_token.append(char)
	# add remaining tokens
	if current_token:
		tokens.append(''.join(current_token))
	return tokens

@profile
def profile_tokenizer():
	sample_input = ("word1" * 1000 + "\t" * 100 + "test" * 500) * 100
	whitespace_tokenizer(sample_input)

if __name__ = "__main__":
	print("Total time taken:", timeit.timeit(profile_tokenizer, number=10))
