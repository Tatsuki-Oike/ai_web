import os
from PIL import Image
import torch
from torchvision import transforms
import torchvision.transforms.functional as TF
from torchvision.models.segmentation import fcn_resnet50, FCN_ResNet50_Weights


MODEL_PATH = "./models/fcn_resnet.pth"


def load_model(model_path=MODEL_PATH):
    
    weights = FCN_ResNet50_Weights.DEFAULT

    if os.path.exists(model_path):
        print("Load Model")
        model = fcn_resnet50(weights=None)
        model_dict = model.state_dict()
        pretrained_dict = torch.load(model_path)
        pretrained_dict = {k: v for k, v in pretrained_dict.items() if k in model_dict}
        model_dict.update(pretrained_dict)
        model.load_state_dict(model_dict)
        model.eval()

    else: 
        print("Save and Load Model")
        model = fcn_resnet50(weights=weights)
        model.eval()
        os.makedirs(os.path.dirname(model_path), exist_ok=True)
        torch.save(model.state_dict(), model_path)
    
    print("Done")
        
    return model, weights


model, weights = load_model()


def segmentation(image):

    # 画像の前処理
    print("Preprocess")
    preprocess = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    batch = preprocess(image).unsqueeze(0)

    # 予測
    print("Prediction")
    prediction = model(batch)["out"]
    normalized_masks = prediction.softmax(dim=1)
    class_to_idx = {cls: idx for (idx, cls) in enumerate(weights.meta["categories"])}
    
    # 背景切り抜き
    inverse_background_mask = 1 - normalized_masks[0, class_to_idx["__background__"]]
    tensor_inverse_background_mask = inverse_background_mask
    masked_tensor_image = TF.to_tensor(image) * tensor_inverse_background_mask
    result_image = TF.to_pil_image(masked_tensor_image)

    return result_image


def main():

    IMAGE_PATH = "./images/cat.jpg"

    # 画像の読み込み
    print("Load Image")
    image = Image.open(IMAGE_PATH).convert("RGB")
    result_image = segmentation(image)

    # 画像の保存
    print("Save")
    result_image.save("./images/segment_image.jpg")


if __name__ == '__main__':
    main()
