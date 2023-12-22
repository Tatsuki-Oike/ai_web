import os
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


SAVE_DIR = "./models"
MODEL_NAME = "microsoft/DialoGPT-medium"


def load_model(save_dir=SAVE_DIR):

    if os.path.exists(SAVE_DIR):
        print("Load Model")
        model = AutoModelForCausalLM.from_pretrained(save_dir)
        tokenizer = AutoTokenizer.from_pretrained(save_dir, padding_side="left")

    else:
        print("Save and Load Model")
        model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, padding_side="left")
        os.makedirs(save_dir, exist_ok=True)
        model.save_pretrained(save_dir)
        tokenizer.save_pretrained(save_dir)
    
    print("Done")
        
    return model, tokenizer


model, tokenizer = load_model()


def chat(input_text):

    # 予測
    print("Prediction")
    input_ids = tokenizer.encode(input_text + tokenizer.eos_token, return_tensors="pt")
    attention_mask = torch.ones(input_ids.shape, device=model.device)
    output_ids = model.generate(
        input_ids,
        attention_mask=attention_mask,
        max_length=150,
        num_beams=5,
        no_repeat_ngram_size=2,
        top_k=50,
        top_p=0.95,
        do_sample=True
    )
    output_text = tokenizer.decode(output_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)

    return output_text


def main():

    input_text = "Hello. How are you?"
    output_text = chat(input_text)
    print(f"input: {input_text}")
    print(f"result: {output_text}")


if __name__ == '__main__':
    main()
