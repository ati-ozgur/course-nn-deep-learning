# Pre-train speed up

## pre-training speed up

- **We will not cover this topic**
- GPU parallelization 
- learning rates
- optimizers
- quantization (32 bit --> 16 bit)
- and others, **active research**

## Parallelization

- Data parallelization
- Tensor parallelization (split matrix multiplication to multiple GPUs)
- Pipeline parallelization (transformer layers to multiple GPUs)
- [Model parallelization](https://huggingface.co/docs/transformers/v4.13.0/en/parallelism)


## pre-training tricks examples

- **We will not cover this topic**
- [source Andrej Karpathy: Let's reproduce GPT-2 (124M)](https://www.youtube.com/watch?v=l8pRSuU81PU)

- Let’s make it fast. GPUs, mixed precision, 1000ms
- Tensor Cores, timing the code, TF32 precision, 333ms
- float16, gradient scalers, bfloat16, 300ms
- torch.compile, Python overhead, kernel fusion, 130ms
- flash attention, 96ms
- nice/ugly numbers. vocab size 50257 → 50304, 93ms
- hyperpamaters, AdamW, gradient clipping
- learning rate scheduler: warmup + cosine decay
- batch size schedule, weight decay, FusedAdamW, 90ms
