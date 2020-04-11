https://en.wikipedia.org/wiki/Dither
https://www.codementor.io/@isaib.cicourel/image-manipulation-in-python-du1089j1u


# Open an Image
def open_image(path):
  newImage = Image.open(path)
  return newImage

# Save Image
def save_image(image, path):
  image.save(path, 'png')

# Create a new image with the given size
def create_image(i, j):
  image = Image.new("RGB", (i, j), "white")
  return image

# Get the pixel from the given image
def get_pixel(image, i, j):
    # Inside image bounds?
    width, height = image.size
    if i > width or j > height:
      return None

    # Get Pixel
    pixel = image.getpixel((i, j))
    return pixel

    
# Create a Half-tone version of the image
def convert_halftoning(image):
  # Get size
  width, height = image.size

  # Create new Image and a Pixel Map
  new = create_image(width, height)
  pixels = new.load()

  # Transform to half tones
  for i in range(0, width, 2):
    for j in range(0, height, 2):
      # Get Pixels
      p1 = get_pixel(image, i, j)
      p2 = get_pixel(image, i, j + 1)
      p3 = get_pixel(image, i + 1, j)
      p4 = get_pixel(image, i + 1, j + 1)

       # Transform to grayscale
       gray1 = (p1[0] * 0.299) + (p1[1] * 0.587) + (p1[2] * 0.114)
       gray2 = (p2[0] * 0.299) + (p2[1] * 0.587) + (p2[2] * 0.114)
       gray3 = (p3[0] * 0.299) + (p3[1] * 0.587) + (p3[2] * 0.114)
       gray4 = (p4[0] * 0.299) + (p4[1] * 0.587) + (p4[2] * 0.114)

       # Saturation Percentage
       sat = (gray1 + gray2 + gray3 + gray4) / 4

       # Draw white/black depending on saturation
       if sat > 223:
         pixels[i, j]         = (255, 255, 255) # White
         pixels[i, j + 1]     = (255, 255, 255) # White
         pixels[i + 1, j]     = (255, 255, 255) # White
         pixels[i + 1, j + 1] = (255, 255, 255) # White
       elif sat > 159:
         pixels[i, j]         = (255, 255, 255) # White
         pixels[i, j + 1]     = (0, 0, 0)       # Black
         pixels[i + 1, j]     = (255, 255, 255) # White
         pixels[i + 1, j + 1] = (255, 255, 255) # White
       elif sat > 95:
         pixels[i, j]         = (255, 255, 255) # White
         pixels[i, j + 1]     = (0, 0, 0)       # Black
         pixels[i + 1, j]     = (0, 0, 0)       # Black
         pixels[i + 1, j + 1] = (255, 255, 255) # White
       elif sat > 32:
         pixels[i, j]         = (0, 0, 0)       # Black
         pixels[i, j + 1]     = (255, 255, 255) # White
         pixels[i + 1, j]     = (0, 0, 0)       # Black
         pixels[i + 1, j + 1] = (0, 0, 0)       # Black
       else:
         pixels[i, j]         = (0, 0, 0)       # Black
         pixels[i, j + 1]     = (0, 0, 0)       # Black
         pixels[i + 1, j]     = (0, 0, 0)       # Black
         pixels[i + 1, j + 1] = (0, 0, 0)       # Black

  # Return new image
  return new