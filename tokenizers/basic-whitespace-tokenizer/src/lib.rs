// WIP
pub fn whitespace_tokenizer(text: &str) -> Vec<&str> {
	let mut tokens = Vec::new();
	let mut start = None;
	
	for (i, c) in text.char_indices() {
		if c.is_whitespace() {
			if let Some(s) = start {
				tokens.push(&test[s..i]);
				start = None;
			}
		} else if start.is_none() {
			start = Some(i);
		}
	}
	
	if let Some(s) = start {
		tokens.push(&text[s..]);
	}

	tokens
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn basic_tokenization() {
        assert_eq!(
            whitespace_tokenizer("hello   world\t\nfoo"),
            vec!["hello", "world", "foo"]
        );
    }

    #[test]
    fn edge_cases() {
        assert_eq!(whitespace_tokenizer(""), Vec::<&str>::new());
        assert_eq!(whitespace_tokenizer("   "), Vec::<&str>::new());
        assert_eq!(whitespace_tokenizer("a"), vec!["a"]);
    }
}

// Benchmarks
#[cfg(feature = "bench")]
mod benches {
    use super::*;
    use criterion::{black_box, criterion_group, criterion_main, Criterion};

    fn benchmark_tokenizer(c: &mut Criterion) {
        let text = "hello ".repeat(1000) + &"\t".repeat(100) + &"test".repeat(500);
        
        c.bench_function("whitespace_tokenizer", |b| {
            b.iter(|| whitespace_tokenizer(black_box(&text)))
        });
    }

    criterion_group!(benches, benchmark_tokenizer);
    criterion_main!(benches);
}
