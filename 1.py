import qrcode
from PIL import Image

# 1. 配置二维码内容（替换为你的网页链接）
https://github.com/JuHuo0601/math.git= "file:///C:/Users/%E6%B5%99%E6%B1%9F%E5%BD%AD%E4%BA%8E%E6%99%8F/Desktop/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9/Untitled-1.html"  # 例如："https://math-modeling-club.example.com"

# 2. 二维码基础设置（高容错率，确保清晰可扫）
qr = qrcode.QRCode(
    version=1,  # 二维码复杂度（1-40，数字越大内容容量越大）
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # 最高容错率（允许30%遮挡仍可识别）
    box_size=12,  # 每个小方块的像素大小（数值越大二维码越大）
    border=4,  # 二维码边框宽度（默认4，保持简洁）
)
qr.add_data(web_url)
qr.make(fit=True)

# 3. 自定义颜色（标题蓝+白色背景，适配海报主题）
# 颜色值可根据海报标题蓝微调：#3399ff（亮蓝）、#2c7be5（深蓝）
img = qr.make_image(
    fill_color="#3399ff",  # 二维码主体颜色（海报标题蓝色）
    back_color="white"     # 二维码背景色（纯净白色，提升对比度）
).convert("RGBA")  # 转为透明通道格式，方便后期贴到海报

# 4. 保存二维码图片
img.save("math_modeling_qr.png")
print("二维码生成成功！文件名为：math_modeling_qr.png")

