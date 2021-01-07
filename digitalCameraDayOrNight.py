'''
Author: shamo0 

You need to construct a feature in a Digital Camera, which will 
auto-detect and suggest to the photographer whether the picture 
should be clicked in day or night mode, depending on whether the
picture is being clicked in the daytime or at night. You only 
need to implement this feature for cases which are directly 
distinguishable to the eyes (and not fuzzy scenarios such as dawn,
dusk, sunrise, sunset, overcast skies which might require more 
complex aperture adjustments on the camera).

A 2D Grid of pixel values will be provided (in regular text format
through STDIN), which represent the pixel wise values from the images 
(which were originally in JPG or PNG formats).

Each pixel will be represented by three comma separated values in the
range 0 to 255 representing the Blue, Green and Red components 
respectively. There will be a space between successive pixels in the same row.
'''

image = input().split(" ")
tot = 0
pixel_tot = 0

for i in range(len(image)):
    image[i] = image[i].split(',')
    
for item in image:
    pixel_sum = 0
    for i in item:
        pixel_sum += int(i)
    pixel_div = pixel_sum/3
    pixel_tot += pixel_div
    tot+=1

if (pixel_tot/tot)>90:
    print('day')
else:
    print('night')
