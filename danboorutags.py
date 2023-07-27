import subprocess
import requests
import json
import sys


def clear_screen():
    try:
        subprocess.run('clear', shell=True, check=True, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        subprocess.run('cls', shell=True, check=True, stderr=subprocess.DEVNULL)
    except:
        pass


def main(image_id):
    base_url = 'https://danbooru.donmai.us/posts'

    clear_screen()

    response = requests.get(f'{base_url}/{image_id}.json')

    if image_id == '':
        sys.exit('[ABORTED]: The Image ID cannot be empty!')

    if not response.status_code == 200:
        sys.exit(f'[ERROR]: {response.status_code}')
    
    data = json.loads(response.text)

    character = data['tag_string_character']
    origin = data['tag_string_copyright']
    tags = data['tag_string_general']
    tags = tags.replace(" ", ", ")
    prompt = f'{character.replace("_", " ")}, {tags.replace("_", " ")}'

    print(f'Character: {character}')
    print(f'Origin: {origin}')
    print(f'Tags: {tags}')
    print(f'\nPrompt: {prompt}')

  
if __name__ == '__main__':
    args = sys.argv
    if len(args) < 2:
        print("usage: python danboorutags.py [image id]")
        exit(0)
    
    image_id = args[1]
    
    main(image_id)
