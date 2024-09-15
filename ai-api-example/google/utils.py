from PIL import Image

def resize_image(image_path, output_path, max_size=500):
    with Image.open(image_path) as img:
        width, height = img.size
        
        if width > max_size or height > max_size:
            # 긴 쪽이 max_size가 되도록 비율 유지하면서 리사이즈
            if width > height:
                new_width = max_size
                new_height = int((max_size / width) * height)
            else:
                new_height = max_size
                new_width = int((max_size / height) * width)
                
            resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            resized_img.save(output_path)