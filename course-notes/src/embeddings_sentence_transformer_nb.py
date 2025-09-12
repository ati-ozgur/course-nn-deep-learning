import marimo

__generated_with = "0.15.3"
app = marimo.App()


@app.cell
def _():
    from sentence_transformers import SentenceTransformer
    return (SentenceTransformer,)


@app.cell
def _(SentenceTransformer):
    # 1. Load a pretrained Sentence Transformer model
    model = SentenceTransformer("all-MiniLM-L6-v2")
    return (model,)


@app.cell
def _():
    # The sentences to encode
    sentences = [
        "The weather is lovely today.",
        "It's so sunny outside!",
        "He drove to the stadium.",
    ]
    return (sentences,)


@app.cell
def _(model, sentences):

    # 2. Calculate embeddings by calling model.encode()
    embeddings = model.encode(sentences)
    print(embeddings.shape)
    # [3, 384]
    return (embeddings,)


@app.cell
def _(embeddings, model):
    # 3. Calculate the embedding similarities
    similarities = model.similarity(embeddings, embeddings)
    print(similarities)
    # tensor([[1.0000, 0.6660, 0.1046],
    #         [0.6660, 1.0000, 0.1411],
    #         [0.1046, 0.1411, 1.0000]])
    return


if __name__ == "__main__":
    app.run()
