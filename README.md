```
 ██╗  ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗     ██████╗  ██████╗ ██████╗  ██████╗ 
 ██║  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗    ╚════██╗██╔═████╗╚════██╗██╔════╝ 
 ███████║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝     █████╔╝██║██╔██║ █████╔╝███████╗ 
 ██╔══██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗    ██╔═══╝ ████╔╝██║██╔═══╝ ██╔═══██╗
 ██║  ██║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║    ███████╗╚██████╔╝███████╗╚██████╔╝
 ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝ ╚══════╝ ╚═════╝ 
```

 # Getting Started
 Version 7 of the workflow is out, but these instructions are for version 6. They'll need to be adapted when I have a chance.
 
 ## General Setup
 
 1. Open the autoshow JSON in ComfyUI
 2. There will be several errors and a request to install missing nodes. Accept this and ComfyUI will prompt to restart on completion.
 3. On second start it will state on more node isn't available and cannot be found. This needed to be manually installed.
    1. (Comfyroll CustomNodes)[https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes]
 4. Install the following models to the `ComfyUI\models\checkpoints\`
    1. (Realities Edge XL Lightning)[https://civitai.com/models/129666/realities-edge-xl-lightning-turbo]
 5. Install the following models to the `ComfyUI\models\controlnets\`
    1. (control_v11p_sd15_scribble_fp16.safetensors)[https://comfyui-wiki.com/en/resource/controlnet-models/controlnet-v1-1-sd15-sd2]
 6. Install LoRAs to `ComfyUI\models\loras\`
    1. https://civitai.com/models/368804/automotive-design
    2. https://civitai.com/models/151180?modelVersionId=169042 
    3. Look at the LoRA list in ComfyUI for any other items
 7. Upscaler model (check the workflow version)
 8. Refiner model is in version 7
