from scipy.stats import ttest_ind

# Ameerika Ühendriikidest vs. Euroopa riikidest imporditud filmid dekaadi (2014-2024) jooksul. Kas Ameerikast imporditud filmide keskmine arv erineb Euroopast imporditutest?
ameerika = [108, 119, 111, 87, 106, 101, 61, 75, 98, 92, 100]
euroopa = [101, 113, 136, 139, 151, 154, 133, 94, 94, 138, 128]
vastus = ttest_ind(ameerika, euroopa)
print(vastus)

if vastus.pvalue < 0.05: # Lugesin, et 0.05 peaks olema standard arv sellise võrdluse jaoks.
    print("Kahe piirkonna vahel on märkimisväärne erinevus imporditud filmide koguses.")
else:
    print("Kahe piirkonna vahel ei ole märkimisväärset erinevust imporditud filmide koguses.")

# Kahe arvujada aritmeetiline keskmine.
def keskmine(m):
    return sum(m)/len(m)
print(keskmine(ameerika), keskmine(euroopa))