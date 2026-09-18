from BPE import bpe

class tokenizer():
    def __init__(self):
        self.BPE = bpe()

    def apply_merges_to_prompt(self, prompt):
        merges = self.BPE.read_file(self.BPE.merges_file_path)
        vocab = prompt
        for i in merges:
            vocab = self.BPE.apply_new_vocab_to_list(vocab, i)
        return vocab

test = tokenizer()
print(test.apply_merges_to_prompt(input("Prompt : ")))