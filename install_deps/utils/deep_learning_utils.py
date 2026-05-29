"""Deep learning / NLP dependencies.

One function per dependency: torch, tensorflow, jax, transformers, datasets,
sentence-transformers, spacy, nltk, gensim.
"""

import torch
import torch.nn as nn
import tensorflow as tf
import jax
import jax.numpy as jnp
from transformers import AutoTokenizer
import datasets
import sentence_transformers
import spacy
import nltk
import gensim


def torch_tensor_sum(values) -> float:
    """torch: build a tensor and reduce it to a scalar sum."""
    t = torch.tensor(list(values), dtype=torch.float32)
    return float(t.sum())


class TinyNet(nn.Module):
    """torch.nn: a one-layer network used by build_tiny_net."""

    def __init__(self) -> None:
        super().__init__()
        self.fc = nn.Linear(1, 1)

    def forward(self, x):
        return self.fc(x)


def build_tiny_net() -> "TinyNet":
    """torch.nn: instantiate a tiny network."""
    return TinyNet()


def tf_constant_sum(values) -> float:
    """tensorflow: build a constant tensor and sum it."""
    t = tf.constant(list(values), dtype=tf.float32)
    return float(tf.reduce_sum(t).numpy())


def jax_grad_square():
    """jax: gradient of x**2 evaluated at x=3.0 (expected 6.0)."""
    grad_fn = jax.grad(lambda x: jnp.square(x))
    return float(grad_fn(3.0))


def load_tokenizer(name: str = "bert-base-uncased"):
    """transformers: load a pretrained tokenizer."""
    return AutoTokenizer.from_pretrained(name)


def make_dataset(rows: list[dict]):
    """datasets: build an in-memory HuggingFace dataset."""
    return datasets.Dataset.from_list(rows)


def embed_sentences(sentences: list[str], model: str = "all-MiniLM-L6-v2"):
    """sentence-transformers: encode sentences into embeddings."""
    encoder = sentence_transformers.SentenceTransformer(model)
    return encoder.encode(sentences)


def blank_nlp(lang: str = "en"):
    """spacy: create a blank language pipeline."""
    return spacy.blank(lang)


def tokenize_text(text: str) -> list[str]:
    """nltk: tokenize text into words."""
    return nltk.tokenize.word_tokenize(text)


def train_word2vec(sentences: list[list[str]]):
    """gensim: train a tiny Word2Vec model."""
    return gensim.models.Word2Vec(sentences, vector_size=16, min_count=1, workers=1)
