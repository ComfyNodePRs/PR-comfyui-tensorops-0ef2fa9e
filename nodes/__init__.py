from .channel_select import ChannelSelector
from .mask_image import MaskImage
from .save_surreal import SaveToSurreal

NODE_CLASS_MAPPINGS = {
    "ChannelSelector": ChannelSelector,
    "MaskImage": MaskImage,
    "SaveToSurreal": SaveToSurreal,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "ChannelSelector":"ChannelSelector",
    "MaskImage": "MaskImage",
    "SaveToSurreal": "SaveToSurreal",
}
