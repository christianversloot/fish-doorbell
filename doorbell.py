import cv2
import matplotlib.pyplot as plt
import numpy as np
import os


def load_image(file):
  """
    Load an image.
  """
  return cv2.imread(file, cv2.IMREAD_GRAYSCALE)


def run_doorbell_on_images():
  """
    Run the Fish Doorbell on a set of images.
  """
  images = os.listdir(f"{os.getcwd()}/images")
  for image in images:
    run_doorbell_on_image(f"{os.getcwd()}/images/{image}")


def run_doorbell_on_image(file):
  """
    Run the Fish Doorbell on a single image.
  """
  # Load image
  image = load_image(file)
  
  # Perform cropping, blurring and edge detection
  cropped_image = crop_image(image)
  blurred_image = apply_blur(cropped_image)
  image_with_edges = canny_edges(blurred_image)
  
  # Check if image hash fish
  fish = has_fish(image_with_edges)
  
  # Plot image and result
  fig, axs = plt.subplots(2)
  plt.suptitle(f'Image has fish = {fish}')
  plot_image(cropped_image, axs, 0)
  plot_image(image_with_edges, axs, 1)
  plt.show()


def crop_image(image, crop_top_bottom_px = 50):
  """
    Crop 50 pixels from bottom and top to remove webcam text.
  """
  height, width = image.shape
  cropped_image = image[crop_top_bottom_px:height-crop_top_bottom_px][0:width]
  return cropped_image


def plot_image(image, axes, index, cmap = 'gray'):
  """
    Plot an image on some plt axis.
  """
  axes[index].imshow(image, cmap = cmap)
  axes[index].axis('off')


def canny_edges(image):
  """
    Perform Canny edge detection.
  """
  return cv2.Canny(image, 10, 15)


def apply_blur(image):
  """
    Apply blur.
  """
  return cv2.blur(image, (15, 15))


def has_fish(image):
  """
    Check for fish.
    Simplistic but effective in many cases.
  """
  fish_like_pixels = np.count_nonzero(image)
  return fish_like_pixels > 50


if __name__ == "__main__":
  run_doorbell_on_images()