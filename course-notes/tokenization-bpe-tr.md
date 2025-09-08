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


## Notebook Tiktoken Tokenizer GPT2

Example notebook for [Tiktoken Tokenizer](https://github.com/ati-ozgur/course-nn-deep-learning/blob/master/notebooks/tokenizer-tiktoken.ipynb)

## Sorunlar tekrar

- Heceleme

```txt
strawberry
heceleme
```


- Aritmetik, toplama çıkarma

```txt
127 + 677 = 804
1275 + 6773 = 8041
```


- Büyük küçük harf

```txt
hello
 hello
HELLO
```


- İngilizce harici diller

```txt
Merhaba Büyük Dil Modelleri dersine giriş
```

- Python kodlama problemi: GPT2  vs cl100_base


```python
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("Fifteen")
    elif i % 3 == 0:
        print("Three")
    elif i % 5 == 0:
        print("Five")
    else:
        print(i)
```


- JSON vs YAML

JSON örnek:

```json
 {"name":"John", "age":30, "car":null}
```

YAML versiyonu:


```yaml
---
name: John
age: 30
car: 
```

### SolidGoldMagikarp 

Bu bir reddit kullanıcısı.
ChatGPT 14 Şubat 2023'ten önce **SolidGoldMagikarp** hakkında soru sorulduğu zaman hata veriyordu.
GPT3 için BPE algoritması eğitilirken reddit üzerinden alınan bir metin grubu kullanılmış.
SolidGoldMagikarp bu yazı grubu içinde çok fazla yazının sahibi.

Tahminlere göre, Sayılaştırma veri seti ile LLM veri seti farklı.
SolidGoldMagikarp sayısı (token), LLM veri setinde yok.
Bu yüzden girdi olarak verildiğinde C dilinde oluşan atanmamış bellek (Un-allocated memory) hatası gibi bir şey oluyor.
Daha fazlası için bakınız: 

- [SolidGoldMagikarp article](https://www.lesswrong.com/posts/aPeJE8bSo6rAFoLqg/solidgoldmagikarp-plus-prompt-generation)
- https://www.beren.io/2023-02-04-Integer-tokenization-is-insane/
- https://www.lesswrong.com/posts/aPeJE8bSo6rAFoLqg/solidgoldmagikarp-plus-prompt-generation
- https://www.lesswrong.com/posts/Ya9LzwEbfaAMY8ABo/solidgoldmagikarp-ii-technical-details-and-more-recent
- https://aizi.substack.com/p/explaining-solidgoldmagikarp-by-looking
- https://deconstructing.ai/deconstructing-ai%E2%84%A2-blog/f/the-enigma-of-solidgoldmagikarp-ais-strangest-token



## LLM Modellerinin Tokenizasyon Sözlük Boyutları 

ChatGPT 5 ile üretilmiştir.

{{< include ./tables/table-tokenization-vocabulary-sizes-of-llm-models-en.md >}}


## Kaynak Vidyolar

[Let's build the GPT Tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE)


## Kütüphaneler

- [sentencepiece](https://github.com/google/sentencepiece) Tokenizer Google: LLaMa, some Google LLMs
- [tiktoken](https://github.com/openai/tiktoken) Tokenizer OpenAI: GPT2, GPT4, ....

[Örnek notebook](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb)

- [minbpe](https://github.com/karpathy/minbpe/)

