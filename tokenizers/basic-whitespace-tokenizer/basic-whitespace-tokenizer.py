
import timeit
from memory_profiler import profile

def whitespace_tokenizer(text):
	tokens = []
	current_token = []
	for char in text:
		if char.isspace():
			if current_token:
				tokens.append(''.join(current_token))
				current_token = []
		else:
			current_token.append(char)
	# add any remaining tokens
	if current_token:
		tokens.append(''.join(current_token))
	return tokens

@profile
def profile_tokenizer():
	sample = ("hello " * 1000 + "\t" * 100 + "test " * 500) * 100
	whitespace_tokenizer(sample)

if __name__ == "__main__":
	print("Time taken:", timeit.timeit(profile_tokenizer, number=10))


