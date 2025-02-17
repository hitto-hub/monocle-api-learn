import base64
from io import BytesIO
from PIL import Image

# Base64データをデコード
base64_data = b'XHgxOVx4MWElJlwnKCkqNDU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6XHg4M1x4ODRceDg1XHg4Nlx4ODdceDg4XHg4OVx4OGFceDkyXHg5M1x4OTRceDk1XHg5Nlx4OTdceDk4XHg5OVx4OWFceGEyXHhhM1x4YTRceGE1XHhhNlx4YTdceGE4XHhhOVx4YWFceGIyXHhiM1x4YjRceGI1XHhiNlx4YjdceGI4XHhiOVx4YmFceGMyXHhjM1x4YzRceGM1XHhjNlx4YzdceGM4XHhjOVx4Y2FceGQyXHhkM1x4ZDRceGQ1XHhkNlx4ZDdceGQ4XHhkOVx4ZGFceGUxXHhlMlx4ZTNceGU0XHhlNVx4ZTZceGU3XHhlOFx4ZTlceGVhXHhmMVx4ZjJceGYzXHhmNFx4ZjVceGY2XHhmN1x4ZjhceGY5XHhmYVx4ZmZceGM0XHgwMFx4MWZceDAxXHgwMFx4MDNceDAxXHgwMVx4MDFceDAxXHgwMVx4MDFceDAxXHgwMVx4MDFceDAwXHgwMFx4MDBceDAwXHgwMFx4MDBceDAxXHgwMlx4MDNceDA0XHgwNVx4MDZceDA3XHgwOFx0XG5ceDBiXHhmZlx4YzRceDAwXHhiNVx4MTFceDAwXHgwMlx4MDFceDAyXHgwNFx4MDRceDAzXHgwNFx4MDdceDA1XHgwNFx4MDRceDAwXHgwMVx4MDJ3XHgwMFx4MDFceDAyXHgwM1x4MTFceDA0XHgwNSExXHgwNlx4MTJBUVx4MDdhcVx4MTMiMlx4ODFceDA4XHgxNEJceDkxXHhhMVx4YjFceGMxXHQjM1JceGYwXHgxNWJyXHhkMVxuXHgxNiQ0XHhlMSVceGYxXHgxN1x4MThceDE5XHgxYSZcJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2g='
image_data = base64.b64decode(base64_data)

# 画像を表示
img = Image.open(BytesIO(image_data))
img.show()
