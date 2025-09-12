

# Present

## We do not understand even small language models

- We can engineer and build LLMs.
- These LLMs work astonishingly well, in practice.
- *But*, We do not understand how LLMs work theoretically.
- But even for 100x parameters small language models, our theory knowledge is lacking

 
- [Alexandar Rush: Large Language Models in 5 Formulas](https://youtu.be/k9DnQPrfJQs)


## LLM Scaling Laws

- Hypothesis: The performance of an LLM is a function of
- N — the number of parameters in the network (weights and biases)
- D — the amount of text we train on

![](images/LLM-Scaling-Laws.png)

- A lot of LLM companies insinuated that AGI will be reached with LLM scaling
- With the release GPT 5, we see that this hypothesis does not hold


## AGI is not impossible but we are not there yet

![](images/AGI-is-not-impossible-but-we-are-not-there-yet.png)

## Road to AGI: More paradigms are needed 

- AGI with only LLM/NN approach is impossible.
- Different approaches is needed

## Multi modal LLM

![](images/Multimodal-LLMs.png)

## Tool Usage 

- RAG
- Web Search
- Code backends
- Plugins
	* [Wolfram ChatGPT Plugin](https://writings.stephenwolfram.com/2023/04/instant-plugins-for-chatgpt-introducing-the-wolfram-chatgpt-plugin-kit)


## Tool Usage example: Python interpreter

- Using python and other interpreter usage is increasing 
- Gemini and ChatGPT are already using python interpreter for some tasks, even when you do not ask for it.
- ChatGPT 5 does not explicitly show its tool usage.

::: {#fig-gemini layout-ncol=3}

![](images/python-code-usage-chatgpt.png)

![](images/python-code-usage-gemini-1.png)

![](images/python-code-usage-gemini-2.png)

ChatGPT/Gemini tool usage
:::



## Tool usage is a Neurosymbolic approach

- Obviously combining a code interpreter (which is a symbolic system of enormous complexity) with a LLM is neurosymbolic. 
- AlphaGo was neurosymbolic as well. 
- These are universally accepted definitions

- [Tweet François Chollet](https://x.com/fchollet/status/1802785277758591054)
- read more [How o3 and Grok 4 Accidentally Vindicated Neurosymbolic AI](https://garymarcus.substack.com/p/how-o3-and-grok-4-accidentally-vindicated)

## Small Language Models 

- Small Language Models are becoming more popular
- especially for defined limited tasks like agents
- read [Small Language Models are the Future of Agentic AI](https://arxiv.org/abs/2506.02153)