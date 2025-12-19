#Once the prompt execution is done it downloads the images using the /history endpoint
import websocket #NOTE: websocket-client (https://github.com/websocket-client/websocket-client)
import uuid
import json
import urllib.request
import urllib.parse
import os
import time
from datetime import datetime
import shutil
import random

server_address = "127.0.0.1:8188"
client_id = str(uuid.uuid4())

def queue_prompt(prompt, prompt_id):
    p = {"prompt": prompt, "client_id": client_id, "prompt_id": prompt_id}
    data = json.dumps(p).encode('utf-8')
    req = urllib.request.Request("http://{}/prompt".format(server_address), data=data)
    urllib.request.urlopen(req).read()

def get_image(filename, subfolder, folder_type):
    data = {"filename": filename, "subfolder": subfolder, "type": folder_type}
    url_values = urllib.parse.urlencode(data)
    with urllib.request.urlopen("http://{}/view?{}".format(server_address, url_values)) as response:
        return response.read()

def get_history(prompt_id):
    with urllib.request.urlopen("http://{}/history/{}".format(server_address, prompt_id)) as response:
        return json.loads(response.read())


# Configure the prompt to run the workflow (latest file goes here)
def queue_prompt(prompt):
    p = {"prompt": prompt, "client_id": client_id}
    data = json.dumps(p).encode('utf-8')
    req = urllib.request.Request(f"http://{server_address}/prompt", data=data)
    return json.loads(urllib.request.urlopen(req).read())

def choicer(options):
    return random.choice(options.split("|"))

def prompt_creater():
    car_type = "classic|widebody|concept|modern|low-rider|muscle|law enforcement|drone|futuristic|steampunk|cyberpunk|modded|street|military|offroad"
    paint_type = "vibrant|iridescent|orange|gun metal|purple|blue|cyan|red|yellow|green|gold|silver|flames decal|platinum|metallic|matte|camo|neon LED accents"
    background_type = "city|skyline|winter|jungle|slum|extraterrestrial|shipping yard|summer|tropical|alpine|Banff|Norway|Hawaii|cavernous|futuristic|urban|apocalyptic|California|warzone|Monaco|Greek|Roman|Caribbean|college campus|mountainous|rural|lunar|winding road|mansion|modern|cliffside|volcano"
    time_of_day = "early morning|night time|evening|golden hour"
    
    prompt_text = f"professional photo of a {choicer(car_type)} car with {choicer(paint_type)} paint, metal geometric symmetrical rims on wheels, clean contours,{choicer(background_type)} background, {choicer(time_of_day)}, professional lighting, highly detailed, high budget,marketing photo, cinemascope, gorgeous, slick, masterpiece"
    return prompt_text

# ---------- Main code ----------

# Define the prompt JSON using the existing workflow file
with open("cias.json", "r", encoding="utf-8") as f:
    workflow_data = f.read()
    prompt = json.loads(workflow_data)

# Check if scan folder has a file
folder = "/Users/razaa/Documents/ComfyUI/input/scan/"
#file = folder + "img20251202_17050626.png"  # Example file path


#loop to check for new files in the scan folder
print(str(datetime.now().timestamp()) + f": Checking folder (ctrl+c to quit) {folder}")
while True:
    # delay = 10  # seconds
    files = os.listdir(folder)
    if files:
        #loop through to find each file
        for file in files:
            #ensure it's an image file
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                print(str(datetime.now().timestamp()) + f": New file found: scan/{file}")
                # # Run the ComfyUI API call using websockets
                ws = websocket.WebSocket()
                ws.connect("ws://{}/ws?clientId={}".format(server_address, client_id))
                
                # Shift the processed file to the output folder
                shutil.move(folder + file, "/Users/razaa/Documents/ComfyUI/input/scan/output/" + file)  # Move the file to the output subfolder
                prompt["11"]["inputs"]["image"] = "scan/output/" + file
                prompt["45"]["inputs"]["seed"] = random.randint(0, 2**32 - 1)  # New random seed for each run
                prompt["7"]["inputs"]["text"] = prompt_creater()  # Generate a new prompt for each run

                response = queue_prompt(prompt)
                print(str(datetime.now().timestamp()) + ": " + str(response))
                ws.close() # for in case this example is used in an environment where it will be repeatedly called, like in a Gradio app. otherwise, you'll randomly receive connection timeouts
                
        # print(str(datetime.now().timestamp()) + f": Waiting {delay} for a change (ctrl+c to exit) - ")
    # time.sleep(delay)  # Simulate processing time
