import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration, T5Config


T5_PATH = 't5-base'
t5_model = T5ForConditionalGeneration.from_pretrained(T5_PATH)
t5_tokenizer = T5Tokenizer.from_pretrained(T5_PATH)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def t5_summarize(input_text, num_beams=4, num_words=50):
    input_text = str(input_text).replace('\n', '')
    input_text = ' '.join(input_text.split())
    input_tokenized = t5_tokenizer.encode(input_text, return_tensors="pt").to(device)
    summary_task = torch.tensor([[21603, 10]]).to(device)
    input_tokenized = torch.cat([summary_task, input_tokenized], dim=-1).to(device)
    summary_ids = t5_model.generate(input_tokenized,
                                    num_beams=int(num_beams),
                                    no_repeat_ngram_size=3,
                                    length_penalty=2.0,
                                    min_length=30,
                                    max_length=int(num_words),
                                    early_stopping=True)
    output = [t5_tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=False) for g in summary_ids]
    return output[0]

sentence="Google facebook apple microsoft are all moving ahead at a great speed in improving this artificial intelligence software so it's very exciting software is going to solve that where it'll look at all the new information and present to you knowing about your interests what would be most valuable so making us more efficient we're focusing on what we've talked about on autonomous systems and we sort of see it as the mother of all ai projects so autonomy is something that's incredibly uh exciting for us we'll see where it takes us wouldn't it be wonderful if someday we got to the point where there were robots every place they were running farms they were driving cars they were doing all sorts of things that we don't even think about right now and all you had to do was one person could punch a button at the start of every morning and all the goods and services that we're getting now would be turned out by robots it is seeping into our lives in ways that we just don't notice we're just getting better and better at it and we're seeing that happen in every aspect of our lives from medicine to transportation to how electricity is distributed and it promises to create a vastly more productive and efficient economy and if properly harnessed can generate enormous prosperity for people opportunity for people can cure diseases that we haven't seen before can make us safer because it eliminates inherent human error in a lot of work uh artificial intelligence is going be extremely helpful and and the risk that it gets super smart that's way out in the future and uh probably worth talking about but now what we are seeing is that for the first time computers can see as well as humans that's pretty incredible uh nissa did a study on on tesla's autopilot version one which is relatively primitive and found that it was a 45 reduction in highway accidents and that's despite autopilot one being just version one um version two i think will be at least two or three times better that's the current version that's running right now um so the rate of improvement is really dramatic but we have to figure out some way to ensure that the advent of digital super intelligence is a good thing and that it is symbiotic with humanity ."
num_beams=5
num_words=500
output = t5_summarize(sentence, num_beams, num_words)
t5_model.to(device)
t5_model.eval()