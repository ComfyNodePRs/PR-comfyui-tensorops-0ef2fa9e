import torch

class MaskImage:
   
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "mask": ("MASK",),
            },
        }

    RETURN_TYPES = ("IMAGE",)

    FUNCTION = "main"

    CATEGORY = "tensorops"

    def main(self, image: torch.Tensor, mask: torch.Tensor):
        print("MaskImage")
        print("ImageShape", image.shape)
        print("MaskShape", mask.shape)
        return (image * mask.unsqueeze(0).unsqueeze(-1),)

