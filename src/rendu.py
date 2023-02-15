from copy import deepcopy

def img2ascii(
    img_data: list[list[int]],
    black: str = '#',
    white: str = '.'
) -> str:
    return '\n'.join([''.join([white if pixel == 0 else black for pixel in line])
                      for line in img_data])

def load_pbm(filename: str) -> list[list[int]]:
    # compléter le code ici pour charger l'image depuis le fichier
    with open(filename, "r") as fd:
        content = []
        for line in fd.readlines():
            if line[0] != "#":
                content.append(line.strip().split(" "))
        img_format = content[0][0]  # facultatif pour les exemples demandés
        largeur = int(content[1][0])
        hauteur = int(content[1][1])
        img_lst = content[2:]

        if len(img_lst) == largeur and len(img_lst[-1]) == hauteur:
            final_img_lst = img_lst
        else:
            new_img_lst = "".join(["".join(element) for element in img_lst])

            final_img_lst = [
                new_img_lst[i : i + largeur]
                for i in range(0, len(new_img_lst), largeur)
            ]
        return [[int(element) for element in line] for line in final_img_lst]


def erosion(img, n):
    def conditions(analysed, limitation):
        return [False if not analysed_condition <= len(limit_condition) - 1 and not analysed_condition >= 0 else True for (analysed_condition, limit_condition) in (analysed, limitation)]
    
    def is_zero_in_img():
        img[lineno - 1][pixelno] == 0
        img[lineno + 1][pixelno] == 0
        img[lineno][pixelno - 1] == 0
        img[lineno][pixelno + 1] == 0
        
    final_img = deepcopy(img)
    for i in range(n):
        if i < n:
            img = deepcopy(final_img)
            for lineno, line in enumerate(final_img):
                for pixelno, pixel in enumerate(line):
                    if (conditions([lineno, pixelno], [final_img, line])[0] == True
                        and is_zero_in_img() == True and pixel == 1
                        or (
                            pixelno == 0
                            or pixelno == len(line) - 1
                            or lineno == 0
                            or lineno == len(img)- 1
                    )):
                        final_img[lineno][pixelno] = 0
        i += 1
    return final_img




print(erosion([[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]], 1))