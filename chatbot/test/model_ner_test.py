import sys
sys.path.append('chatbot') 
from utils.Preprocess import Preprocess
from models.ner.NerModel import NerModel

p = Preprocess(word2index_dic=r'chatbot_dict.bin',
               userdic=r'chatbot\utils\user_dic.tsv')

ner = NerModel(model_name=r'chatbot/ner_model.h5', preprocess=p)
query = input()
predicts = ner.predict(query)
print(predicts)