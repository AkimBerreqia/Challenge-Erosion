def erosion(img, n):
    final_img = [list(range(10))] * 10
    for i in range(n):
        if i < n:
            for lineo, line in enumerate(img):
                for pixelno, pixel in enumerate(line):
                    if (pixelno == 0 or pixelno == len(line) - 1 or line[lineo - 1] == 0 or line[lineo + 1] == 0) and pixel == 1:
                        final_img[lineo][pixelno] = 0
    return img

img = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
print(erosion(img, 1))