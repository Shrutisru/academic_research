import os
import cv2

# ==========================================
# EuRoC Dataset Path
# ==========================================

EUROC_PATH = r"D:\research\data_set\MH_01_easy\MH_01_easy"

MAV0_PATH = os.path.join(EUROC_PATH, "mav0")

CAM0_PATH = os.path.join(MAV0_PATH, "cam0")
CAM1_PATH = os.path.join(MAV0_PATH, "cam1")
IMU_PATH = os.path.join(MAV0_PATH, "imu0")

CAM0_DATA_PATH = os.path.join(CAM0_PATH, "data")


# ==========================================
# Check dataset
# ==========================================

print("Checking EuRoC dataset...\n")

print("Dataset path:", EUROC_PATH)
print("mav0 exists:", os.path.exists(MAV0_PATH))
print("cam0 exists:", os.path.exists(CAM0_PATH))
print("cam1 exists:", os.path.exists(CAM1_PATH))
print("imu0 exists:", os.path.exists(IMU_PATH))
print("cam0/data exists:", os.path.exists(CAM0_DATA_PATH))


# ==========================================
# Check camera images
# ==========================================

if not os.path.exists(CAM0_DATA_PATH):
    raise FileNotFoundError(
        f"\nCamera data folder not found:\n{CAM0_DATA_PATH}"
    )

images = sorted([
    f for f in os.listdir(CAM0_DATA_PATH)
    if f.lower().endswith((".png", ".jpg", ".jpeg"))
])

print("\nNumber of Camera 0 images:", len(images))

if len(images) == 0:
    raise FileNotFoundError(
        "No images found inside cam0/data!"
    )


# ==========================================
# Load first image
# ==========================================

first_image = images[0]
first_image_path = os.path.join(CAM0_DATA_PATH, first_image)

print("\nFirst image:", first_image)
print("Full path:", first_image_path)

image = cv2.imread(first_image_path)

if image is None:
    raise ValueError("Could not load the image!")


# ==========================================
# Display information
# ==========================================

print("\nImage loaded successfully!")
print("Image size:", image.shape)


# ==========================================
# Show image
# ==========================================

cv2.imshow("EuRoC MH_01_easy - Camera 0", image)

print("\nPress any key to close the image window...")

cv2.waitKey(0)
cv2.destroyAllWindows()
