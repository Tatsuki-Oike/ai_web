import os
from PIL import Image, ImageOps
import torch
import torchvision


MODEL_PATH = "./models/vit_model.pth"


def load_model(model_path=MODEL_PATH):
    
    weights = torchvision.models.ViT_B_16_Weights.DEFAULT

    if os.path.exists(model_path):
        print("Load Model")
        model = torchvision.models.vit_b_16(weights=None)
        model.load_state_dict(torch.load(model_path))
        model.eval()

    else: 
        print("Save and Load Model")
        model = torchvision.models.vit_b_16(weights=weights)
        model.eval()
        os.makedirs(os.path.dirname(model_path), exist_ok=True)
        torch.save(model.state_dict(), model_path)
    
    print("Done")
        
    return model, weights


model, weights = load_model()


def image_recognition(image):
    
    # 画像の前処理
    print("Preprocess")
    preprocess = weights.transforms()
    resized_image = ImageOps.pad(image, (224, 224), method=0, color=0)
    batch = preprocess(resized_image).unsqueeze(0)

    # 画像認識
    print("Prediction")
    prediction = model(batch).squeeze(0).softmax(0)
    class_id = prediction.argmax().item()
    score = prediction[class_id].item()
    category_name = weights.meta["categories"][class_id]

    return score, category_name


def main():

    IMAGE_PATH = "./images/cat.jpg"

    # 画像の読み込み
    print("Load Image")
    image = Image.open(IMAGE_PATH)

    score, category_name = image_recognition(image)
    print(f"{category_name}: {100 * score:.1f}%")


if __name__ == '__main__':
    main()