import torch
from transformers import BartTokenizer, BartForConditionalGeneration, BartConfig
from transformers import T5Tokenizer, T5ForConditionalGeneration, T5Config
from transformers import BartTokenizer, BartModel

#model= BartForConditionalGeneration.from_pretrained('facebook/bart-large')
#tokenizer= BartModel.from_pretrained('facebook/bart-large')

BART_PATH = 'facebook/bart-large'
model = BartForConditionalGeneration.from_pretrained(BART_PATH)
tokenizer = BartTokenizer.from_pretrained(BART_PATH)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


def bart_summarize(input_text, num_beams=4, num_words=50):
    input_text = str(input_text)
    input_text = ' '.join(input_text.split())
    input_tokenized = tokenizer.encode(input_text, return_tensors='pt').to(device)
    summary_ids = model.generate(input_tokenized,
                                      num_beams=int(num_beams),
                                      no_repeat_ngram_size=3,
                                      length_penalty=2.0,
                                      min_length=30,
                                      max_length=int(num_words),
                                      early_stopping=True)
    output = [tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=False) for g in summary_ids]
    return output[0]


def work(sentence,num_words,num_beams):
    output = bart_summarize(sentence, num_beams, num_words)
    return output
