columns = ['Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium','Total phenols',
            'Flavanoids','Nonflavanoid phenols', 'Proanthocyanins', 'Color intensity', 'Hue'
            'OD280/OD315 of diluted wines', 'Proline']

cols1 = [ True, False, False,  False, False, False,  True, False,  False,
        True, False,  False, False]

cols2 = [ True, False, False, False, False, False,  True, False, False,
        True,  True,  True,  True]

if(cols1==cols2):
    print('yes')
else: print('no')

cols = cols1

for j in range(len(cols)):
    cols[j] = int(cols[j])
nums = cols
n=6
print(nums)
for i in range(len(nums)):
    if nums[i]==1:
        print(columns[i]+',')

print(sum([False,  True,  True,  True,  True, False,  True, False, False,
       False, False,  True,  True,  True, False, False]))