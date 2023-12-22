import os
from PIL import Image, ImageOps, ImageDraw, ImageFont
import torch
from torchvision.models.detection import fasterrcnn_resnet50_fpn_v2, FasterRCNN_ResNet50_FPN_V2_Weights


MODEL_PATH = "./models/faster_rcnn_model.pth"


def load_model(model_path=MODEL_PATH):
    
    weights = FasterRCNN_ResNet50_FPN_V2_Weights.DEFAULT

    if os.path.exists(model_path):
        print("Load Model")
        model = fasterrcnn_resnet50_fpn_v2(weights=None, box_score_thresh=0.9)
        model.load_state_dict(torch.load(model_path))
        model.eval()

    else: 
        print("Save and Load Model")
        model = fasterrcnn_resnet50_fpn_v2(weights=weights, box_score_thresh=0.9)
        model.eval()
        os.makedirs(os.path.dirname(model_path), exist_ok=True)
        torch.save(model.state_dict(), model_path)
    
    print("Done")
        
    return model, weights


model, weights = load_model()


def object_detection(image):

    # 画像の前処理
    print("Preprocess")
    resized_image = ImageOps.pad(image, (224, 224), method=0, color=0)
    preprocess = weights.transforms()
    batch = [preprocess(resized_image)]

    # 予測
    print("Prediction")
    prediction = model(batch)[0]
    labels = [weights.meta["categories"][i] for i in prediction["labels"]]

    # バウンディングボックスの作成 
    print("Plot")
    draw = ImageDraw.Draw(resized_image)

    for box, label, score in zip(prediction["boxes"], labels, prediction["scores"]):
        font = ImageFont.load_default(size=int((box[2]-box[0])/8))
        draw.rectangle(box.tolist(), outline="red", width=4)
        text_bbox = draw.textbbox(
                (box[0], box[1] - int((box[2]-box[0])/15)), 
                f"{label}: {score:.2f}", 
                font=font
            )
        draw.rectangle(text_bbox, fill="white")
        draw.text(
                (box[0], box[1] - int((box[2]-box[0])/15)), 
                f"{label}: {score:.2f}", 
                fill="red", 
                font=font
            )

    return resized_image


def main():

    IMAGE_PATH = "./images/cat.jpg"

    print("Load Image")
    image = Image.open(IMAGE_PATH).convert("RGB")
    result_image = object_detection(image)
    
    print("Save")
    result_image.save("./images/detected_image.jpg")


if __name__ == '__main__':
    main()
