import os
import pandas as pd
import requests

GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'
CYAN = '\033[96m'
RED = '\033[91m'

def download_img():
    print(CYAN + '==========================================')
    print('Image DATA.')
    print(YELLOW + 'by @fikra ' + CYAN + '(fikra-ye)')
    print(CYAN + '==========================================' + RESET)
    file_path = input('File Path: ')
    column_name = input('Column Name: ')
    os.makedirs('fikra_images', exist_ok=True)
    df = pd.read_excel(file_path)

    for index, url in enumerate(df[column_name]):
        try:
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                image_name = url.split('/')[-1]
                image_path = os.path.join('downloaded_images', image_name)
                with open(image_path, 'wb') as f:
                    f.write(response.content)
                print(GREEN + f"Image '{image_name}' downloaded successfully!" + RESET)
            else:
                print(RED + f"Failed to download image {index + 1}. Invalid link." + RESET)
        except Exception as e:
            print(RED + f"An error occurred while downloading image {index + 1}: {e}" + RESET)

if __name__ == '__main__':
    download_img()
