import os
from diffusers import StableDiffusionPipeline


MODEL_PATH = "./models/faster_rcnn_model.pth"
MODEL_ID = "stabilityai/stable-diffusion-2-1"


def load_model(model_path=MODEL_PATH):

    if os.path.exists(model_path):
        print("Load Model")
        pipe = StableDiffusionPipeline.from_pretrained(model_path).to("cpu")

    else:
        print("Save and Load Model")
        pipe = StableDiffusionPipeline.from_pretrained(MODEL_ID).to("cpu")
        pipe.enable_attention_slicing()
        os.makedirs(os.path.dirname(model_path), exist_ok=True)
        pipe.save_pretrained(model_path)
    
    print("Done")
        
    return pipe


pipe = load_model()


def image_generation(prompt, steps=3, size=256):

    print("Generate Image")
    print("Prompt", prompt)
    print("Steps", steps)
    print("Size", size)
    image = pipe(
        prompt,
        height=int(size), 
        width=int(size),
        num_inference_steps=int(steps)
    ).images[0]
    print("Done")
    return image


def main():

    print("Start")
    prompt = "a cute magical flying robot, fantasy art drawn, high quality, highly detailed"
    steps = 3
    size = 256
    result_image = image_generation(prompt, steps, size)
    result_image.save(f"images/generated_{steps}.jpg")


if __name__ == '__main__':
    main()