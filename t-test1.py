from scipy.stats import ttest_ind

lause1="Kui Arno isaga koolimajja jõudis olid tunnid juba alanud"
lause2="Mu isamaa mu õnn ja rõõm kui kaunis oled sa"

sonad1=lause1.split()
sonad2=lause2.split()
print(sonad1,sonad2)
print(len(sonad1)) # sõnu lauses kokku
print(len(sonad1[3])) # kuva sõna nr 3 tähtede av

sonapikkused1=[len(sona) for sona in sonad1]
sonapikkused2=[len(sona) for sona in sonad2]
print(sonapikkused1, sonapikkused2)

print(ttest_ind([3, 4, 5, 10, 6, 4, 6, 4, 6], [2, 6, 2, 3, 2, 4, 3, 6, 4, 2]))

# leia t-test abil, kas nende lausete keskmine pikkus erineb üldistatavalt

print(sum(sonapikkused1)/len(sonapikkused1))
print(sum(sonapikkused2)/len(sonapikkused2))