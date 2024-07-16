import torch
from comfyui import Node, Input, Output

class ChannelSelector(Node):
    # Define the node's metadata
    title = "Channel Selector"
    category = "Custom"
    description = "Select a specific channel from a tensor of shape C x W x H and reduce it to 1 x W x H"

    # Define the inputs and outputs
    inputs = {
        "input_tensor": Input(torch.Tensor, description="Input tensor of shape C x W x H"),
        "channel_index": Input(int, description="Index of the channel to select")
    }
    outputs = {
        "output_tensor": Output(torch.Tensor, description="Output tensor of shape 1 x W x H")
    }

    def __init__(self):
        super(ChannelSelectorNode, self).__init__()

    def process(self, input_tensor, channel_index):
        # Validate the channel index
        if channel_index < 0 or channel_index >= input_tensor.size(0):
            raise ValueError(f"Invalid channel index: {channel_index}. Must be between 0 and {input_tensor.size(0) - 1}")

        # Select the specified channel and add a new dimension at position 0
        output_tensor = input_tensor[channel_index].unsqueeze(0)

        return {"output_tensor": output_tensor}

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "ChannelSelector": ChannelSelector,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "ChannelSelector":"ChannelSelector",
}
