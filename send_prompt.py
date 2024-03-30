from transformers import GPT2Tokenizer, GPT2LMHeadModel

tokenizer = GPT2Tokenizer.from_pretrained('sberbank-ai/rugpt3medium_based_on_gpt2')
model = GPT2LMHeadModel.from_pretrained('sberbank-ai/rugpt3medium_based_on_gpt2')

def send_prompt(prompt):
    prompt_text = "Привет! Я ваш персональный модератор. Вот что мне нужно сделать сегодня:  Автоматическое модерирование: Я могу автоматически сканировать сообщения на канале и идентифицировать нежелательный контент, такой как спам, оскорбления, и некорректные материалы" + prompt
    encoded_input = tokenizer(prompt_text, return_tensors='pt', padding=True, truncation=True, max_length=512)
    output = model.generate(encoded_input.input_ids, max_length=300, num_return_sequences=1, do_sample=True, no_repeat_ngram_size=2, temperature=0.7)
    text_output = tokenizer.decode(output[0], skip_special_tokens=True)
    return text_output
