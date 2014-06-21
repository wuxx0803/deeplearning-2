from scipy.io import loadmat
import random
import numpy as np


def get_random(num):
    return random.randint(0, num - 1)

##  load the image file
def load_data():
    image_mat = loadmat("IMAGES.mat")
    key = [k for k in image_mat.keys() if k.startswith('IMAGES')][0]
    images = image_mat[key]
    return images

## normalize patches.. 
def normalize(patches):
    norm = (0.1, 0.9)
    pstd = 3 * np.std(patches)
    patches = np.maximum(np.minimum(patches, pstd), -pstd) / pstd
    patches = ((patches + 1) * ((norm[1] - norm[0]) / 2.0)) + norm[0]
    return patches

## generate the patches from the image files 
def gen_patch(image, num_patches=10000, size=(8, 8)):
    patch_data = []
    x, y = size
    t1, t2, num_images = image.shape
    for i in range(0, num_patches):
        image_id = get_random(num_images)
        trial_image = image[:, :, image_id]
        mx, my = tuple(np.array(trial_image.shape) - np.array(size))
        c1, c2 = get_random(mx), get_random(my)
        patch = trial_image[c1:c1 + x, c2:c2 + y]
        patch_data.append(patch.flatten())
    return patch_data

image = load_data()
val = np.array(gen_patch(image))
for i in val:
    print normalize(i)
    sys.exit(-1)
