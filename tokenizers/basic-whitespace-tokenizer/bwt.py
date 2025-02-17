import timeit
from memory_profiler import profile

ALPHABETS = [x for x in "qwertyuiopasdfghjklzxcvbnm"]

def tokenize(input_text):
	# basically input_text.lower().split()
	tokens = []
	curr_token = []
	lower_input_text = input_text.lower()
	for char in lower_input_text:
		if is_break_point(char):
			if curr_token:
				tokens.append("".join(curr_token))
				curr_token = []
		else:
			curr_token.append(char)
	if curr_token:
		tokens.append("".join(curr_token))
	return tokens

def is_break_point(char):
	return char not in ALPHABETS

@profile
def profile_tokenizer():
	sample = ("hELlo " * 1000 + "\t" * 100 + "test " * 500) * 100
	tokenize(sample)

if __name__ == "__main__":
	print("Time taken:", timeit.timeit(profile_tokenizer, number=10))
