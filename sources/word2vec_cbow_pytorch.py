import torch
import torch.nn as nn
import torch.optim as optim
import random
from collections import Counter

# ----------------------------
# 1. Prepare Data
# ----------------------------
corpus = [
    "we are what we repeatedly do",
    "excellence then is not an act but a habit",
    "the unexamined life is not worth living",
    "to be yourself in a world that is constantly trying to make you something else is the greatest accomplishment"
]

def tokenize(text):
    return text.lower().split()

tokenized_corpus = [tokenize(sentence) for sentence in corpus]

vocab = Counter(word for sentence in tokenized_corpus for word in sentence)
# Add <PAD> token to vocab for context padding
print(vocab)
vocab["<PAD>"] = 1  # ensure it exists
word2idx = {w: idx for idx, (w, _) in enumerate(vocab.items())}
idx2word = {idx: w for w, idx in word2idx.items()}
vocab_size = len(vocab)

# Generate CBOW training pairs with fixed-length context
window_size = 2
pairs = []
context_len = 2 * window_size  # fixed size

for sentence in tokenized_corpus:
    for center_pos, center_word in enumerate(sentence):
        context = []
        for w in range(-window_size, window_size + 1):
            context_pos = center_pos + w
            if w == 0 or context_pos < 0 or context_pos >= len(sentence):
                continue
            context.append(word2idx[sentence[context_pos]])
        # Pad if context shorter than full size
        while len(context) < context_len:
            context.append(word2idx["<PAD>"])
        pairs.append((context, word2idx[center_word]))

print(f"Total training pairs: {len(pairs)}")

# ----------------------------
# 2. CBOW Model
# ----------------------------
class CBOW(nn.Module):
    def __init__(self, vocab_size, embedding_dim):
        super(CBOW, self).__init__()
        self.embeddings = nn.Embedding(vocab_size, embedding_dim)
        self.linear = nn.Linear(embedding_dim, vocab_size)

    def forward(self, context_words):
        embeds = self.embeddings(context_words)  # (batch, context_len, embed_dim)
        avg_embeds = embeds.mean(dim=1)          # (batch, embed_dim)
        out = self.linear(avg_embeds)            # (batch, vocab_size)
        return out

# ----------------------------
# 3. Train
# ----------------------------
embedding_dim = 50
batch_size = 8
epochs = 50

model = CBOW(vocab_size, embedding_dim)
loss_fn = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

for epoch in range(epochs):
    random.shuffle(pairs)
    total_loss = 0
    for i in range(0, len(pairs), batch_size):
        batch = pairs[i:i+batch_size]
        context_batch = torch.tensor([p[0] for p in batch], dtype=torch.long)
        target_batch = torch.tensor([p[1] for p in batch], dtype=torch.long)

        optimizer.zero_grad()
        output = model(context_batch)
        loss = loss_fn(output, target_batch)
        loss.backward()
        optimizer.step()

        total_loss += loss.item()
    print(f"Epoch {epoch+1}, Loss: {total_loss:.4f}")

# ----------------------------
# 4. Test Embeddings
# ----------------------------
def get_embedding(word):
    idx = word2idx[word]
    return model.embeddings.weight.data[idx]

print("\nEmbedding for 'excellence':")
print(get_embedding("excellence"))
