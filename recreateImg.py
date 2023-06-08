import requests
from PIL import Image
from io import BytesIO
import json, time

def recreate_img(ins_id):
    get_mint_json_url = f"https://ordinals.com/content/{ins_id}"
    get_mint_json_response = requests.get(get_mint_json_url)

    # print("min_json_url: ", get_mint_json_url)
    # print(get_mint_json_response)

    try :
        mint_json = get_mint_json_response.json()
    except Exception as e:
        return 

    # Step 1: Extract deploy_ins from the JSON
    deploy_ins = mint_json["deploy_ins"]

    # Step 2: Query the URL and get the deploy JSON
    url = f"https://ordinals.com/content/{deploy_ins}"
    response = requests.get(url)

    # print("url: ", url)
    # print(response)

    try :
        deploy_json = response.json()
    except Exception as e:
        return

    # Step 3: Get components from the deploy JSON
    components = deploy_json["components"]

    # Step 4: Fetch sprite sheet images and store them
    spritesheet_images = []
    for component_id in components:
        component_url = f"https://ordinals.com/content/{component_id}"
        response = requests.get(component_url)
        spritesheet_image = Image.open(BytesIO(response.content))
        spritesheet_images.append(spritesheet_image)

    # Step 5: Draw the composed image using the spritesheet images
    composed_image = Image.new("RGBA", (32, 32))
    for i, (spritesheet_index, component_index) in enumerate(mint_json["compose"]):
        spritesheet_image = spritesheet_images[spritesheet_index]
        component_image = spritesheet_image.crop((32 * component_index, 0, 32 * (component_index + 1), 32))

        composed_image.paste(component_image, (0,0), mask=component_image)

    # composed_image.show()

    # Step 6: Save the created image to a file
    composed_image.save(f"./generated_imgs/{ins_id}.png")

file_path = "tv_robot_valid_ins.txt"

with open(file_path, "r") as file:
    for ins_id in file:
        recreate_img(ins_id.strip())
        time.sleep(1)

