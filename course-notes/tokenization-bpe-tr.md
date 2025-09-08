## Çift bayt kodlama (Byte pair encoding)

- [Byte pair encoding wikipedia](https://en.wikipedia.org/wiki/Byte-pair_encoding) örneği

Örnek olarak aşağıdaki veriyi kodlalım.

	aaabdaaabac


**aa** çifti en çok geçtiği için, onun yerine Z simgesi verilcektir.
Bu durumda aşağıdaki veri ve sözlük oluşturulacaktır. 

	ZabdZabac
	Z=aa

Aynı süreç tekrarlanır ve **ab** yerine Y yerleştirilir.

	ZYdZYac
	Y=ab
	Z=aa


Bu veride en fazla tekrar eden **ZY** çifti, X ile değiştirilir.


	XdXac
	X=ZY
	Y=ab
	Z=aa

Büyük verilerde sözlük büyüklüğüne görede kodlama durabilir.
Örneğin en fazla 10 simge kullanılacaktır denilebilir.
GPT2 sayılaştırma sözlük boyutu 50257'dir.



- [Örnek BPE 1 Andrej Karpathy](https://github.com/karpathy/minbpe/blob/master/exercise.md)
- [Örnek BPE 2 Sebastian Raschka](https://github.com/rasbt/LLMs-from-scratch/blob/main/ch02/05_bpe-from-scratch/bpe-from-scratch.ipynb)


## Kaynak Vidyolar

[Let's build the GPT Tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE)


## Kütüphaneler

- [sentencepiece](https://github.com/google/sentencepiece) Tokenizer Google: LLaMa, some Google LLMs
- [tiktoken](https://github.com/openai/tiktoken) Tokenizer OpenAI: GPT2, GPT4, ....

[Örnek notebook](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb)

- [minbpe](https://github.com/karpathy/minbpe/)

