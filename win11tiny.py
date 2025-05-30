import requests

url = "https://download937.mediafire.com/ialhefs3vbxg3wNJDqz_MPqMcQVZk1X19MEIgzJWsSNoowvAvFk8PBMcxkQ/win10.zip"
output = "/mnt/win10.zip"

print("Đang tải file...")

r = requests.get(url, stream=True)
with open(output, "wb") as f:
    for chunk in r.iter_content(chunk_size=8192):
        if chunk:
            f.write(chunk)

print(f"✅ File đã được tải về và lưu tại: {output}")
