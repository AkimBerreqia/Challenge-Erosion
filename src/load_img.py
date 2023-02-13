
def load_pbm(filename):
    # compléter le code ici pour charger l'image depuis le fichier
    with open(filename, 'r') as fd:
        content = []
        for line in fd.readlines():
            if line[0] != '#':
                content.append(line.strip().split(' '))

        img_format = content[0][0] # facultatif pour les exemples demandés
        largeur = int(content[1][0])
        hauteur = int(content[1][1])
        img_lst = content[2:]

        if len(img_lst) == largeur and len(img_lst[-1]) == hauteur:
            final_img_lst = img_lst
        else:
            new_img_lst = ''.join([''.join(element)
            for element in img_lst])

            final_img_lst = [new_img_lst[i:i+largeur]
            for i in range(0, len(new_img_lst), largeur)]

        return [[int(element) for element in line]
        for line in final_img_lst]
            
        
        
        
#print(load_pbm('circle-nb.pbm'))
print(load_pbm('circle-nb-2.pbm'))
#print(load_pbm('circle-nb-3.pbm'))
