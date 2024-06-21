import cv2
import numpy as np
from matplotlib import pyplot as plt


def load_image(file_path):
    try:
        image = cv2.imread(file_path)
        if image is None:
            raise ValueError(f"Unable to load image from {file_path}.")
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB
        return image
    except Exception as e:
        print(f"Error: {e}")
        return None


def display_image_with_result(image, lsb_ratio, result_text):
    try:
        plt.imshow(image)
        plt.title('Original Image')
        plt.axis('off')
        plt.figtext(0.5, 0.03, f"LSB Ratio: {lsb_ratio:.4f}\n{result_text}", wrap=True, horizontalalignment='center',
                    fontsize=10)
        plt.show()
    except Exception as e:
        print(f"Error displaying image: {e}")


def check_lsb_steganography(image):
    try:
        height, width, channels = image.shape
        lsb_planes = [np.bitwise_and(image[:, :, channel], 1) for channel in range(channels)]
        lsb_image = np.stack(lsb_planes, axis=-1)

        # Calculate the percentage of 1s in the LSB plane
        lsb_ratio = np.mean(lsb_image)
        result_text = ""

        # Heuristic: If the ratio is significantly different from 0.5, it might indicate hidden data
        if abs(lsb_ratio - 0.5) > 0.1:  # Threshold can be adjusted
            result_text = "Potential steganography detected based on LSB analysis."
        else:
            result_text = "No steganography detected based on LSB analysis."

        return lsb_ratio, result_text
    except Exception as e:
        print(f"Error during LSB analysis: {e}")
        return None, "Error during LSB analysis."


def main():
    file_path = input("Enter the image file path: ")
    image = load_image(file_path)
    if image is not None:
        lsb_ratio, result_text = check_lsb_steganography(image)
        display_image_with_result(image, lsb_ratio, result_text)
    else:
        print("Failed to load and process the image.")


if __name__ == "__main__":
    main()
