import qrcode
data = "Скородумова Ульяна/9б/2022-02-07/2334"
filename = "qrcode30"
img = qrcode.make(data)
img.save(filename)