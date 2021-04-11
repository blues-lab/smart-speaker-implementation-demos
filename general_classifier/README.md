### Running the notebooks
Download Glove for word embeddings
```sh
mkdir GloVe
curl -Lo GloVe/glove.840B.300d.zip http://nlp.stanford.edu/data/glove.840B.300d.zip
unzip GloVe/glove.840B.300d.zip -d GloVe/
```

and 
Download infersent for sentence embeddings
```sh
mkdir encoder
curl -Lo encoder/infersent1.pkl https://dl.fbaipublicfiles.com/infersent/infersent1.pkl
```

Run the classifier notebook classifier.ipynb to load and view the data.

### Running the Server 
Current Accuracy:

Download deepspeech-0.7.3-models from deepspeech directory. The files that should be included are 
```
├── deepspeech-0.7.3-models.pbmm
├── lm.binary
├── output_graph.pb
├── output_graph.pbmm
├── output_graph.tflite
└── trie
```

## Download + Accessing Colabs
Copy the model files for the relevant classification system
https://drive.google.com/drive/folders/1gzlJk7iL88Fpe2OzW7NQI_9iSyIqx39B?usp=sharing
Download ffc_keras_model,label_encoding.pkl, and infraset_model.torch from the notebook 
