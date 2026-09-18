import json

class bpe():
    def __init__(self):
        self.merges_file_path = "BPE/tokenizer_data/merges.json"
        try:
            self.merges = self.read_file(self.merges_file_path)
        except:
            self.merges = []

    def train(self, text):
        vocab = self.reduce_to_basic_vocab(text)
        token_amnt = 300
        while len(vocab) > token_amnt:
            vocab = self.tokenize_with_vocab(vocab)

        self.write_to_file(self.merges_file_path, self.merges)

        
    def tokenize_with_vocab(self, vocab):
        # Starts by getting a new vocab (token) and apply's it to the list, returns the result after
        new_vocab = self.calculate_weigth(vocab)
        applied_vocab = self.apply_new_vocab_to_list(vocab, new_vocab)
        return applied_vocab

    def reduce_to_basic_vocab(self, text):
        basic_vocab = []
        for i in range(len(text)):
            if text[i] == " ":
                basic_vocab.append("_")
            else:
                basic_vocab.append(text[i])
        return basic_vocab

    def calculate_weigth(self, vocab:list):
        # Creates a dict with the amount of times every pair appears
        count = {}
        different_pairs = []
        for i in range(len(vocab)-1):
            pair = vocab[i] + vocab[i+1]
            try:
                count[pair] += 1
            except:
                count[pair] = 1
                different_pairs.append(pair)
        return self.get_most_present(count, different_pairs)

    def apply_new_vocab_to_list(self, vocab, new_vocab):
        # Iterates through the vocabs, if theres a match with new_vocab, delete vocab pair and add the new_vocab instead
        final_vocab_list = []
        i=0
        while i < len(vocab):
            if not i == len(vocab)-1:
                if vocab[i] + vocab[i+1] == new_vocab:
                    final_vocab_list.append(new_vocab)
                    i += 2
                else:
                    final_vocab_list.append(vocab[i])
                    i += 1
            else:
                final_vocab_list.append(vocab[i])
                i += 1
        return final_vocab_list

    def get_most_present(self, count, diff_pairs):
        # iterates through the whole 'count' dict to find the pair w/ the most occurences
        biggest = diff_pairs[0]
        amount_of_biggest = [diff_pairs[0]]
        for voc in diff_pairs:
            if count[voc] > count[biggest]:
                biggest = voc
                amount_of_biggest = [voc]
            elif count[voc] == count[biggest]:
                amount_of_biggest.append(voc)
        
        # When there is multiple pairs w/ the same amount of occurences, pick the smallest one in length
        smallest = amount_of_biggest[0]
        for i in amount_of_biggest:
            if len(i) < len(smallest):
                smallest = i
        self.merges.append(smallest)
        return smallest

    def write_to_file(self, file_name:str, content):
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(content, file, ensure_ascii=False, indent=2)

    def read_file(self, file_name):
        with open(file_name, "r", encoding="utf-8") as file:
            return json.load(file)

if __name__ == "__main__":
    b = bpe()
    text =  """
The tokenizer transforms text into smaller units called tokens.
Tokenization allows an artificial intelligence model to process language.
A tokenizer can recognize common patterns in words and reuse them.
Tokenization, optimization, organization, normalization, serialization, and generation
all contain recurring pieces of language.
A token can represent a character, a word, or a common part of a word.
When the same sequence appears many times, the tokenizer can learn it as a token.
Learning useful tokens makes text processing more efficient.
The model receives token IDs instead of raw text.
These IDs are converted back into tokens when the model generates language.

The system can process information, understand patterns, generate responses,
and transform one sequence into another.
Training requires many examples because repeated patterns provide stronger signals.
A small dataset may produce strange merges, while a larger dataset can produce
more useful representations.
The tokenizer should therefore learn from a diverse collection of text.

Natural language contains many recurring structures.
Words such as running, runner, runs, walked, walking, walker, generated,
generation, generating, generated, optimized, optimization, optimized,
organized, organization, organizing, normalized, normalization, and normalizing
share common pieces.
These repeated structures can become useful subword tokens.

Artificial intelligence systems process enormous amounts of information.
Language models learn statistical relationships between tokens.
The tokenizer determines how text is represented before it enters the model.
A good vocabulary contains both small fundamental tokens and larger frequently
occurring subword tokens.
Rare words can still be represented by combining smaller tokens.
This allows the tokenizer to handle words it has never encountered before.
"""
    small_text = "This is a test"
    b.train(small_text)