import os
from transformers import MarianMTModel, MarianTokenizer

SAVE_DIR = "./models"
MODEL_NAME = "Helsinki-NLP/opus-mt-ja-en"

def load_model(save_dir=SAVE_DIR):

    if os.path.exists(SAVE_DIR):
        print("Load Model")
        model = MarianMTModel.from_pretrained(save_dir)
        tokenizer = MarianTokenizer.from_pretrained(save_dir)

    else:
        print("Save and Load Model")
        model = MarianMTModel.from_pretrained(MODEL_NAME)
        tokenizer = MarianTokenizer.from_pretrained(MODEL_NAME)
        os.makedirs(save_dir, exist_ok=True)
        model.save_pretrained(save_dir)
        tokenizer.save_pretrained(save_dir)
    
    print("Done")
        
    return model, tokenizer


model, tokenizer = load_model()


def translate(input_text):

    # 予測
    print("Prediction")
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    output_ids = model.generate(input_ids)
    output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    return output_text


def main():

    input_text = "こんにちは、元気ですか？"
    output_text = translate(input_text)
    print(f"input: {input_text}")
    print(f"result: {output_text}")


if __name__ == '__main__':
    main()
