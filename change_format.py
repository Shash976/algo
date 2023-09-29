import cv2
import os

main_path = r"C:\Users\shashg\Downloads\character_database"
images = [os.path.join(main_path, parent_path, p) for parent_path in os.listdir(main_path) for p in os.listdir(os.path.join(main_path, parent_path)) if p.endswith(".jpg")]
for image in images:
    img = cv2.imread(image)
    if type(img) != type(None):
        cv2.imshow(os.path.split(image)[-1], img)
        cv2.imwrite(f"{os.path.splitext(image)[0]}.jpeg", img)
        cv2.waitKey(100)
        cv2.destroyAllWindows()
        os.remove(image)