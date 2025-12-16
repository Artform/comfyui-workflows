#Once the prompt execution is done it downloads the images using the /history endpoint
import websocket #NOTE: websocket-client (https://github.com/websocket-client/websocket-client)
import uuid
import json
import urllib.request
import urllib.parse

server_address = "127.0.0.1:8188"
client_id = str(uuid.uuid4())

# Move file to input folder
def move_file_to_input_folder(file_path, input_folder):
    import shutil
    import os

    if not os.path.exists(input_folder):
        os.makedirs(input_folder)

    file_name = os.path.basename(file_path)
    destination = os.path.join(input_folder, file_name)
    shutil.move(file_path, destination)
    return destination

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

def get_images(ws, prompt):
    prompt_id = str(uuid.uuid4())
    queue_prompt(prompt, prompt_id)
    output_images = {}
    while True:
        out = ws.recv()
        if isinstance(out, str):
            message = json.loads(out)
            if message['type'] == 'executing':
                data = message['data']
                if data['node'] is None and data['prompt_id'] == prompt_id:
                    break #Execution is done
        else:
            # If you want to be able to decode the binary stream for latent previews, here is how you can do it:
            # bytesIO = BytesIO(out[8:])
            # preview_image = Image.open(bytesIO) # This is your preview in PIL image format, store it in a global
            continue #previews are binary data

    history = get_history(prompt_id)[prompt_id]
    for node_id in history['outputs']:
        node_output = history['outputs'][node_id]
        images_output = []
        if 'images' in node_output:
            for image in node_output['images']:
                image_data = get_image(image['filename'], image['subfolder'], image['type'])
                images_output.append(image_data)
        output_images[node_id] = images_output

    return output_images

# Configure the prompt to run the workflow (latest file goes here)
def queue_prompt(prompt):
    p = {"prompt": prompt, "client_id": client_id}
    data = json.dumps(p).encode('utf-8')
    req = urllib.request.Request(f"http://{server_address}/prompt", data=data)
    return json.loads(urllib.request.urlopen(req).read())

# Define the prompt JSON using the existing workflow file
with open("cias.json", "r", encoding="utf-8") as f:
    workflow_data = f.read()
    prompt = json.loads(workflow_data)

# Check if scan folder has a file
folder = "/Users/razaa/Documents/ComfyUI/input/scan/"
file = folder + "img20251202_17050626.png"  # Example file path
prompt["102"]["inputs"]["image"] = file
# Check if file was located
if not file:
    raise Exception("No file found in scan folder")
else:
    print(f"Found file: {file}")
    prompt["102"]["inputs"]["image"] = file

ws = websocket.WebSocket()
ws.connect("ws://{}/ws?clientId={}".format(server_address, client_id))

#images = get_images(ws, prompt)

response = queue_prompt(prompt)
print("Workflow queued, response:")
print(response)

ws.close() # for in case this example is used in an environment where it will be repeatedly called, like in a Gradio app. otherwise, you'll randomly receive connection timeouts
#Commented out code to display the output images:

# Run API call




#move_file_to_input_folder(file, "/Users/razaa/Documents/ComfyUI/input/")
