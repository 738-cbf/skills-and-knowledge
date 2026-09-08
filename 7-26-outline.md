# Tiny Language Model Learning Checklist

### *Context:*
*This list is the result of a conversation with 5.6-Sol about my goals and interests in ML. Expect contents of each phase's directory to deviate somewhat from info here or go beyond/have other related projects in them. I am trying to use what I learn to create other interesting things alongside the initial project to explore the concept that was presented.

Goal: understand tokenization and pretraining by building up from character prediction to a tiny GPT.

## How to use this checklist

- [ ] Work on only one unchecked item at a time.
- [ ] Write about what you learned before stopping.
- [ ] Do all exercises! Helps to build math skills and reinforce concepts
- [ ] If stuck for 30 minutes, consult the accompanying notebook or implementation and record what unblocked you.

## Phase 1 — Neural-network foundations

Resource: [Neural Networks: Zero to Hero](https://github.com/karpathy/nn-zero-to-hero)

- [x] Complete Lecture 1: micrograd and backpropagation.
- [x] Be able to explain a parameter, gradient, loss, and optimization step in plain language.
	- Parameter: initialized and learned weights and biases within the model that affect activations (~residual stream) as they flow through the model. It is a tunable component, whose gradient says how a tiny change in the parameter (at its current value) would affect the loss.
	- Gradient: property of a parameter, derivative of loss with respect to parameter's value, including the derivatives of any other parameters in between. Essentially, a vector that points towards increased loss and that we are aiming to go in the opposite direction of for each parameter to minimize the loss. 
	- Loss: how far off the NN's prediction is from the goal.
	- Optimization step: run the model forward to produce outputs, then, starting at the output (final layer) and going backwards, compute the gradients of each parameter wrt the loss and alter each parameter by a small value times the negation of their gradient, nudging them towards lower loss (minimizing the loss function) and in the opposite direction of increased loss.

**Move on when:** you understand that training changes parameters in the direction that reduces a measured error.

Cali note: got this now! Moving on. - 9/7/26

## Phase 2 — Your first character language model

Resources:

- [Zero to Hero, Lecture 2: makemore](https://github.com/karpathy/nn-zero-to-hero)
- [makemore reference project](https://github.com/karpathy/makemore)

- [ ] Complete Lecture 2's bigram character model.
- [ ] Connect its vocabulary to your project: each character is one token.
- [ ] Identify the context, target character, predicted probabilities, and loss.
- [ ] Generate a few samples from the trained model.
- [ ] Compare learned prediction with your current random automated player.

**Move on when:** you understand how raw text becomes context/target training examples and how the model learns next-character probabilities.

## Phase 3 — Learn the basic PyTorch workflow

Resource: [PyTorch: Learn the Basics](https://docs.pytorch.org/tutorials/beginner/basics/intro.html)

- [ ] Read Tensors.
- [ ] Read Datasets and DataLoaders.
- [ ] Read Build the Neural Network.
- [ ] Read Automatic Differentiation.
- [ ] Read Optimizing Model Parameters.
- [ ] Relate each topic back to the makemore model.

**Move on when:** you can follow a training loop and explain what the data, model, loss, gradients, and optimizer each do. You do not need to memorize PyTorch syntax.

## Phase 4 — Tokenization

Resources:

- [Let's Build the GPT Tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE)
- [minBPE companion project](https://github.com/karpathy/minbpe)

- [ ] Understand why character tokens work but make sequences long.
- [ ] Understand the difference between characters, bytes, and tokens.
- [ ] Follow the byte-pair encoding merge process.
- [ ] Understand encoding text into token IDs.
- [ ] Understand decoding token IDs back into text.
- [ ] Experiment with how the same text is split by different vocabularies.

**Move on when:** you can explain how a tokenizer learns its vocabulary separately from the language model and can describe encode/decode in plain language.

## Phase 5 — Build a tiny GPT

Resource: [Let's Build GPT: From Scratch, in Code, Spelled Out](https://www.youtube.com/watch?v=kCc8FmEb1nY)

- [ ] Follow the initial character-level data preparation.
- [ ] Understand batches and context windows.
- [ ] Understand embeddings and positional information.
- [ ] Understand causal self-attention at a high level.
- [ ] Understand why future tokens are hidden during training.
- [ ] Follow loss calculation and optimization.
- [ ] Train the small model and generate text from it.

**Move on when:** you can trace the full path from raw text to tokens, training examples, predicted next-token probabilities, loss, updated weights, and generated text.

## Phase 6 — See a practical training implementation

Resource: [nanoGPT](https://github.com/karpathy/nanoGPT)

- [ ] Read the README and run the smallest example available to you.
- [ ] Locate configuration, dataset preparation, training, checkpointing, and sampling.
- [ ] Compare its organization with the from-scratch GPT lesson.
- [ ] Avoid optimization details until you have a reason to need them.

**Move on when:** you recognize how the educational pieces are organized into a reusable pretraining project.

## Phase 7 — Read the original transformer paper

Resource: [Attention Is All You Need](https://arxiv.org/abs/1706.03762)

- [ ] Read the abstract and introduction.
- [ ] Study the main architecture diagram.
- [ ] Read the sections on scaled dot-product and multi-head attention.
- [ ] Skim unfamiliar mathematical or experimental details on the first pass.
- [ ] Write a short summary of what transformers changed.

**Done when:** the paper connects ideas you have already used instead of feeling like an entirely new vocabulary.

## Parking lot — not needed yet

- Reinforcement learning or reward modeling
- Large datasets
- Multi-GPU training
- Fine-tuning large pretrained models
- Production tokenization libraries
- Training a useful general-purpose LLM

## Progress log

- Date:
- Completed:
- One thing I learned:
- Next smallest action:
