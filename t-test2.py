from scipy.stats import ttest_ind
lause1="Kui Arno isaga koolimajja jõudis olid tunnid juba alanud Kooliõpetaja kutsus mõlemad oma tuppa kõneles nendega  natuke aega, käskis Arnol hoolas ja korralik ja seadis ta siis pinki ühe pikkade juustega poisi kõrvale istuma"
lause2="Mu isamaa mu õnn ja rõõm kui kaunis oled sa Ei leia mina iial tääl see suure laia ilma pääl"

# Lisage hümnile ja Kevadele kummalegi ka järgmine lause. 
# Võrrelge p-väärtusi ühe ja kahe lause puhul

# Leia T-testi abil, kas nende lausete sõnade keskmine pikkus erineb üldistatavalt
sonad1=lause1.split()
sonapikkused1=[len(sona) for sona in sonad1]
sonad2=lause2.split()
sonapikkused2=[len(sona) for sona in sonad2]
print(ttest_ind(sonapikkused1, sonapikkused2))
print(sum(sonapikkused1)/len(sonapikkused1))

# 6.175432-05  = 0.000006175432