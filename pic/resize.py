import os
from PIL import Image

def resize_images_to_512x512():
    """将当前文件夹下的所有图片调整为512x512大小"""
    
    # 支持的图片格式
    supported_formats = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp', '.JPG')
    
    # 获取当前目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 遍历当前目录下的所有文件
    for filename in os.listdir(current_dir):
        if filename.lower().endswith(supported_formats):
            try:
                # 构建完整的文件路径
                file_path = os.path.join(current_dir, filename)
                
                # 打开图片
                with Image.open(file_path) as img:
                    # 调整大小为512x512
                    resized_img = img.resize((512, 512), Image.Resampling.LANCZOS)
                    
                    # 保存图片，保持原格式
                    resized_img.save(file_path)
                    print(f"已调整 {filename} 的大小为 512x512")
                    
            except Exception as e:
                print(f"处理 {filename} 时出错: {e}")

if __name__ == "__main__":
    resize_images_to_512x512()
    print("所有图片处理完成！")
