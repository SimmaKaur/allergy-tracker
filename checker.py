from tokenize import String


allergens = ['Amerchol L101','Peg-16 lanolin','Lanolin peg-16','Peg-16 lanolin alcohol','Lanolin polyethylene glycol ether (16 moles)','Lanolin derivative'
,'Lanolin PEG-16 acetate','Polyethylene glycol (16) lanolin','Lanolin PEG-16 ether'
,'PEG-16 lanolin derivative','Lanolin ethoxylate (16 moles)'
,'Benzoyl Peroxide','Bpo','Benzoyl peroxyde','Dibenzoyl peroxide','Peroxyde de benzoyle'
,'Benzoyl superoxide','Dibenzoyl peroxide','Peroxybenzoyl','Peroxide, benzoyl'
,'Benzoyl dioxide','Benzoyl hydroperoxide','Dibenzoyl peroxyde'
,'Carba Mix','Carbamix','Carba mix II','Carbamide mix','Mercapto mix'
,'Mercaptobenzothiazole mix','Mercaptobenzothiazole','MBT mix','MBT'
,'Compositae Mix','Compositae plant mix','Asteraceae mix','Daisy mix'
,'Ragweed mix','Composite mix','Chrysanthemum mix','Sunflower mix'
,'Marigold mix','Arnica mix','D-Limonene','Limonene','(+)-Limonene'
,'Limonene-D','Dipentene','p-Mentha-1,8-diene','Racemic limonene'
,'dl-Limonene','Limoneno','Citrus terpenes','Decyl Glucoside'
,'Decyl polyglucoside','Decyl d-glucoside','Alkyl polyglucoside'
,'Polyglucoside','D-Glucopyranose','Decyl glucopyranoside'
,'1-Decyl glucoside','Fragrance','Parfum','Perfume','Aroma','Essential oils'
,'Fragrant oils','Scent','Odorant','Fragrance Mix','Perfume Mix'
,'Fragrance cocktail','Scent mixture','Fragrance blend','Perfume blend'
,'Glutaraldehyde','Glutaric dialdehyde','Glutaric aldehyde','Glutar'
,'Glutaral','Glutaraldéhyde','Glutardialdehyde','Lidocaine','Xylocaine'
,'Lignocaine','Lidocaine hydrochloride','Lidocaina','Lidocaína','Alphacaine'
,'Lignocaine hydrochloride','Linalool','β-linalool','p-linalool'
,'Linalyl alcohol','3,7-Dimethyl-1,6-octadien-3-ol'
,'2,6-Dimethyl-2,7-octadien-6-ol','Propolis','Bee glue','Bee propolis'
,'Bee cement','Propolis extract','Apis propolis','Beeswax']

new_allergens_list = []
for i in allergens:
    new_allergens_list.append(i.lower())
allergens = new_allergens_list

def checker(input):
    input = input.lower()
    input = input.partition(", ")
    print('DEBUG: input list after partitioning is: ', input)
    found_allergens = []
    for i in input:
        if i in allergens:
            found_allergens.append(i)
    return found_allergens

ingredients = 'Benzoyl Peroxide, buh'

print(checker(ingredients))