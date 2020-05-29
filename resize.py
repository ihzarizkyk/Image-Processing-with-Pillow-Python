from PIL import Image

img = Image.open("image_new.png")
new_image = img.resize((400, 400)) # untuk mengatur ulang ukuran gambar

# simpan kembali gambar yang telah diubah ulang ukurannya dengan nama yang berbeda
new_image.save("image_r400.png")
new_image.show() # tampilkan gambar