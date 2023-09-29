import cv2
import numpy as np
import os
import pandas as pd

path = r"G:\My Drive\Background"
image_paths = [os.path.join(path, p) for p in os.listdir(path)]
image_by_sizes = {}

duplicates = []
for image in image_paths:
    if image.endswith((".jpg", ".jpeg", ".png")):
        try: 
            img = cv2.imread(image)
            if img.size not in image_by_sizes.keys():
                image_by_sizes[img.size] = []
            else:
                for i in image_by_sizes[img.size]:
                    if i["array"].shape == img.shape:
                        diff = cv2.subtract(i["array"], img)
                        b, g, r = cv2.split(diff)
                        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
                            print(f"\t {i['path']} is duplicate of {image}")
                            duplicates.append({i['path']: image})
            image_by_sizes[img.size].append({"path":image, "array":img})
        except Exception as e:
            print(e)
    print(image, " done.")

print(duplicates)
    