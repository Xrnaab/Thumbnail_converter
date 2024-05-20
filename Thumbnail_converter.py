from PIL import Image
import os

def create_thumbnail(input_image_path, output_image_path, size=(128, 128)):
    """
    Create a thumbnail of the input image and save it to the output path.

    :param input_image_path: Path to the input image file.
    :param output_image_path: Path to save the thumbnail image.
    :param size: Desired size of the thumbnail (width, height).
    """
    try:
        with Image.open(input_image_path) as img:
            img.thumbnail(size)
            img.save(output_image_path)
            print(f"Thumbnail saved to {output_image_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    input_image_path = input("Enter the path to the input image: ")
    output_image_path = input("Enter the path to save the thumbnail: ")
    
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_image_path), exist_ok=True)

    create_thumbnail(input_image_path, output_image_path)
