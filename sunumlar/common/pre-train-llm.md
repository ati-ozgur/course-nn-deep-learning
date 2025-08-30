# pre-train LLM

## Dump language model 1 (Before pre-train)

{{< include ../figures/dump-language-model-1-en.mermaid >}}

- When LLM first start training, it randomly generates output.
- Therefore, probability of any word coming is $\frac{1}{vocabulary size}$
- GPT2 vocabulary size is 50257
- at the start of the pre-training, we expect to see similar number, 10.82, for loss value

## Dump language model 2 (Before pre-train)


{{< include ../figures/dump-language-model-together-en.mermaid >}}

- here, we have to different vocab sizes, 50257 and 100
- correspondingly, we will start with two different losses


## Training LLMs Example llama2

Training is like compression of the terabytes of text

![llama2 training](../images/training-Llama2.png)

## Pre-Train step 1 dataset

![](../images/pretrain-step1-dataset.png)

## Pre-Train step 2 tokenization

![](../images/pretrain-step2-tokenization.png)

## Pre-Train step 3 neural network training

![](../images/pretrain-step3-neural-network-training.png)

## Pre-Train step 4 inference

![](../images/pretrain-step4-inference.png)


