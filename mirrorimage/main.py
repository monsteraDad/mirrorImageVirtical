# This program is to provide me with a tool to aid in the
# creation of my photography. this script will take the image
# file and mirror along the virtical midpoint. producing
# a new image file as output. We will be using the Python imaging
# library


# import PIL Module
from PIL import Image

# open the original image
img = Image.open("/Users/casserole/PycharmProjects/mirrorImageVirtical/pictureFiles/weed1.png")

# show image
img.show()

# find the number of pixels vertically across the image
img_size_vertical = img.size[0]
print(img_size_vertical)

# divide the number of pixels by 2 to find midpoint
img_size_vertical_midpoint = img_size_vertical / 2
print(img_size_vertical_midpoint)

# split picture in 2 saving them as img_L(eft) and img_R(ight)
box_L = (0, 0, img_size_vertical_midpoint, img.size[1])
box_R = (img_size_vertical_midpoint, 0, img.size[1], img.size[1])

#box_L = (img_size_vertical_midpoint, img_size_vertical_midpoint, img.size[1], img.size[1])
img_L = img.crop(box_L)
img_R = img.crop(box_R)

# flip imgs and save as img_L_fLip, img_R_flip
img_L_flip = img_L.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
img_R_flip = img_R.transpose(Image.Transpose.FLIP_LEFT_RIGHT)

# take img_L and merge img_L_flip save as mirror_side_L
w = img_L.size[0] + img_L_flip.size[0]
h = max(img_L.size[1], img_L_flip.size[1])

mirror_side_L = Image.new("RGBA", (w, h))

mirror_side_L.paste(img_L)
mirror_side_L.paste(img_L_flip, (img_L.size[0], 0))

mirror_side_L.show()

# take img_R and add img_R_flip save as mirror_side_L
w = img_R.size[0] + img_R_flip.size[0]
h = max(img_R.size[1], img_R_flip.size[1])

mirror_side_R = Image.new("RGBA", (w, h))

mirror_side_R.paste(img_R_flip)
mirror_side_R.paste(img_R, (img_R_flip.size[0], 0))

mirror_side_R.show()

#save new images to desktop
mirror_side_L.save("/Users/casserole/Desktop/python image flip/weed1L.png")

mirror_side_R.save("/Users/casserole/Desktop/python image flip/weed1R.png")