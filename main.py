import torch
from comfyui import Node, Input, Output

class ChannelSelector(Node):
   
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "channel_index": ("INT", {
                    "default": 0, 
                    "min": 0, #Minimum value
                    "max": 100, #Maximum value
                    "step": 1, #Slider's step
                    "display": "number" # Cosmetic only: display as "number" or "slider"
                })
            },
        }

    RETURN_TYPES = ("IMAGE",)

    FUNCTION = "process"

    CATEGORY = "tensorops"
    
    def __init__(self):
        super(ChannelSelectorNode, self).__init__()

    def process(self, image, channel_index):
        # Select the specified channel and add a new dimension at position 0
        mask = image[channel_index].unsqueeze(0)

        return {"mask": mask}

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "ChannelSelector": ChannelSelector,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "ChannelSelector":"ChannelSelector",
}
