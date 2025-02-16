import Data.Map (Map)
import qualified Data.Map as Map

-- I. TYPES

type Document = [String]
type Corpus = [Document]

-- Type for Term Frequency: word -> frequency map

type IDF = Map String Double
type TFIDF = Map String Double



-- II. FUNCTIONS

-- 1. Term Frequency
computeTF :: Document -> Map String Double
computeTF doc = Map.map ( \count -> fromIntegral count / fromIntegral totalWords ) wordCounts
	where
		wordCounts = countWords doc
		totalWords = length doc
-- 1a. Helper function: doc's word x frequency map
countWords :: Document -> Map String Int
countWords = foldr ( \word acc -> Map.insertWith (+) word 1 acc ) Map.empty
