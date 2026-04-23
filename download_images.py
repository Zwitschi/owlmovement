"""
Script to download all images from discovered content URLs
and save them locally to the Flask static images directory
"""

import os
import requests
from urllib.parse import urlparse
from pathlib import Path


# Image URLs from discovered content
IMAGE_URLS = {
    "comedy-stains-logo.jpg": "https://static.wixstatic.com/media/11d46c_7439f513351e479c89cb129a9002d411~mv2.jpg",
    "super-silly-show-logo.png": "https://static.wixstatic.com/media/11d46c_4edf89bfd02243b0886637a41c35169b~mv2.png",
    "corky-eye-pizza.gif": "https://static.wixstatic.com/media/11d46c_b97cf97a3e754c13a503e2fd6b800264~mv2.gif",
    "ding-dong-show-thumbnail.jpg": "https://yt3.ggpht.com/ytc/AIdro_kTv0bX_37Lqi2_K13_b3b5hMMgsx35Hzfe__5GQjwCey0=s800-c-k-c0x00ffffff-no-rw",
    "getting-caught-up.jpg": "https://static.wixstatic.com/media/11d46c_894b8abbce22443187515709a2dedb9c~mv2.jpg",
    "stains-of-comedy.png": "https://static.wixstatic.com/media/11d46c_62f309fab95b43b595aa234703f56bfe~mv2.png",
    "new-beginnings-and-old-endings.jpg": "https://static.wixstatic.com/media/11d46c_4d823c329744484bb8b092480ed44cad~mv2.jpg",
    "comedy-square-logo.png": "https://static.wixstatic.com/media/11d46c_f2cffe20d5b848c18163074c0754629b~mv2.png",
}

# Target directory
IMAGES_DIR = Path(__file__).parent / "app" / "static" / "images"


def download_images():
    """Download all images and save them locally"""
    
    # Create images directory if it doesn't exist
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    
    print(f"Downloading images to {IMAGES_DIR}")
    print(f"Total images to download: {len(IMAGE_URLS)}\n")
    
    successful = 0
    failed = 0
    
    for filename, url in IMAGE_URLS.items():
        filepath = IMAGES_DIR / filename
        
        # Skip if file already exists
        if filepath.exists():
            print(f"✓ Skipping {filename} (already exists)")
            successful += 1
            continue
        
        try:
            print(f"⬇ Downloading {filename}...", end=" ")
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            # Write file
            with open(filepath, 'wb') as f:
                f.write(response.content)
            
            print(f"✓ ({len(response.content)} bytes)")
            successful += 1
            
        except requests.exceptions.RequestException as e:
            print(f"✗ Failed: {str(e)}")
            failed += 1
        except Exception as e:
            print(f"✗ Error: {str(e)}")
            failed += 1
    
    print(f"\n{'='*60}")
    print(f"Download complete!")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"{'='*60}\n")
    
    # Print mapping for reference
    print("Local image paths for use in application:\n")
    for filename in sorted(IMAGE_URLS.keys()):
        local_path = f"/static/images/{filename}"
        print(f'    "{filename}": "{local_path}",')


if __name__ == "__main__":
    download_images()
