
| Model                        | Vocabulary Size (tokens)           | Notes / Source                                                                              |
|------------------------------|------------------------------------|---------------------------------------------------------------------------------------------|
| GPT-2                        | 50,257                             | Byte-level BPE, includes base vocabulary with merges and merges count (Rohan's Bytes)       |
| GPT-3                        | ~50,257                            | Same tokenizer as GPT-2; widely cited (Rohan's Bytes)                                       |
| GPT-4                        | ~50,000 (not officially disclosed) | No official figure; predecessor GPT-3 had ~50k (Rohan's Bytes)                              |
| LLaMA 2                      | 32,000                             | Standard for LLaMA-2 models (Planet Banatt)                                                 |
| LLaMA 3                      | 128,000                            | Documented token vocabulary (Reddit, Rohan's Bytes)                                         |
| LLaMA 4                      | Not publicly disclosed             | No data available                                                                           |
| Claude (Anthropic)           | Not publicly disclosed             | No definitive source; earlier anecdotal “~65k” figure unverified                            |
| Grok (xAI)                   | Not publicly disclosed             | No reliable number found                                                                    |
| DeepSeek LLM (7B / 67B)      | 102,400                            | Byte-level BPE, includes English and Chinese; vocabulary size explicitly stated (Wikipedia) |
| DeepSeek-V2 / V2-Lite / V2.5 | Presumably same (102,400)          | Not explicitly stated, but likely reused the original LLM tokenizer                         |
| DeepSeek-V3                  | 128,000                            | Uses Byte-level BPE with an extended vocabulary of 128K tokens (arXiv, Medium)              |