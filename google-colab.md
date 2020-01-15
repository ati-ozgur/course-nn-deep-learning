# google colab

We will use google colab in the class exclusively to avoid installation problems.
If you want to install local version of python, jupyter, tensorflow and other tools see following [notes](local-installation.md)

## Google colab intro



## Getting files

1. wget or curl

    wget url

    curl -O [url]

2. Python code

 
```python
    import urllib.request
    urllib.request.urlretrieve(url, filename)
```


## Uploading files

1. google colab file tabs

2. using code

```python
from google.colab import files
uploaded = files.upload()
```





## Setting kaggle account in colab

- https://towardsdatascience.com/setting-up-kaggle-in-google-colab-ebb281b61463
- https://github.com/bonn0062/colab_kaggle_api/blob/master/kaggle_colab_setup.ipynb


