from PIL import Image
import cv2
import numpy as np


# resize image, keep aspect ratio
def resize_image(input_path, output_path, target_size):
    with Image.open(input_path) as img:
        img.thumbnail(target_size)

        img.save(output_path)


# add thickness of lines
def enhance_lines(image_path, output_path, thickness=100):
    image = cv2.imread(image_path, 0)  # 读取为灰度图像

    # 进行边缘检测
    edges = cv2.Canny(image, 50, 150, apertureSize=3)

    # 定义膨胀核
    kernel = np.ones((thickness, thickness), np.uint8)

    # 对边缘进行膨胀操作
    thick_edges = cv2.dilate(edges, kernel)

    # 叠加原始图像和加粗边缘，得到加粗线条效果
    result = cv2.addWeighted(image, 0.5, thick_edges, 0.5, 0)

    # 保存结果
    cv2.imwrite(output_path, result)


if __name__ == "__main__":
    input_image_path = r"E:\#code\butto\fig\c.png"
    output_image_path = r"E:\#code\butto\fig\c-resized.png"

    target_size = (512, 512)

    # resize_image(input_image_path, output_image_path, target_size)
    enhance_lines(input_image_path, output_image_path, thickness=3)
