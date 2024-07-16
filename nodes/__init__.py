from .channel_select import ChannelSelector
from .mask_image import MaskImage

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "ChannelSelector": ChannelSelector,
    "MaskImage": MaskImage
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "ChannelSelector":"ChannelSelector",
    "MaskImage": "MaskImage"
}
