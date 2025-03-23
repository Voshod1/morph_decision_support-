import pandas as pd

class MorphologicalMethod:
    def __init__(self, dataSt):
        self.data = dataSt

    def work(self):
        bzalt = self.data.morphTable
        mvzip = self.data.connectionTable
        mvzip2 = self.data.matrixOfUzgodzhiennia
        tabl = pd.DataFrame(columns=['1', '2', '3', '4', '5', '6', 'p0', 'C', 'p1', 'p_final'])
        n = 0

        for i in bzalt['1'].index:
            one = bzalt['1'][i]
            ont = '1.' + str(i + 1)
            for ii in bzalt['2'].index:
                two = bzalt['2'][ii]
                tw = '2.' + str(ii + 1)
                for iii in bzalt['3'].index:
                    three = bzalt['3'][iii]
                    th = '3.' + str(iii + 1)
                    for iiii in bzalt['4'].index:
                        four = bzalt['4'][iiii]
                        fo = '4.' + str(iiii + 1)
                        for iiiii in bzalt['5'].index:
                            five = bzalt['5'][iiiii]
                            fi = '5.' + str(iiiii + 1)
                            for iiiiii in bzalt['6'].index:
                                six = bzalt['6'][iiiiii]
                                sx = '6.' + str(iiiiii + 1)
                                p = one * two * three * four * five * six
                                if (p != 0):
                                    C = 1
                                    for l in (ont, tw, th, fo, fi):
                                        for ll in (tw, th, fo, fi, sx):
                                            C *= (1 + mvzip[l][float(ll)])
                                    p1 = p * C
                                    dat = {'1': ont, '2': tw, '3': th, '4': fo, '5': fi, '6': sx, 'p0': p, 'C': C,
                                           'p1': p1, 'p_final': 0}
                                    tabl = tabl.append(dat, ignore_index=True)
                                    n += 1
        summa = tabl['p1'].sum()
        print("sum = ", summa)
        tabl['p_final'] = tabl['p1'] / summa
        print(tabl)
        print(tabl['p_final'].sum())

        for i in bzalt.columns:
            for j in bzalt[i].index:
                bzalt[i][j] = tabl[tabl[i] == i + '.' + str(j + 1)]['p_final'].sum()
        print(bzalt)
        # print(tabl[tabl['p_final']==tabl['p_final'].mean()])

        print(mvzip2)
        tabl2 = pd.DataFrame(
            columns=['1', '2', '3', '4', '5', '6', 'p_final', 'r71', 'r72', 'r73', 'r81', 'r82', 'r83', 'r84', 'r85',
                     'R71', 'R72', 'R73', 'R81', 'R82', 'R83', 'R84', 'R85', 'pR71', 'pR72', 'pR73', 'pR81', 'pR82',
                     'pR83', 'pR84', 'pR85'])
        for i in range(tabl['1'].size):
            rs = []
            for r in mvzip2.columns[:3]:
                C = 1
                for l in tabl2.columns[:6]:
                    C *= (1 + mvzip2[r][float(tabl[l][i])])
                rs.append(C)
            rs1 = rs / sum(rs)
            rs2 = rs1 * tabl['p_final'][i]
            rss = []
            for r in mvzip2.columns[3:]:
                C = 1
                for l in tabl2.columns[:6]:
                    C *= (1 + mvzip2[r][float(tabl[l][i])])
                rss.append(C)
            rss1 = rss / sum(rss)
            rss2 = rss1 * tabl['p_final'][i]
            ft = {'1': tabl['1'][i], '2': tabl['2'][i], '3': tabl['3'][i], '4': tabl['4'][i], '5': tabl['5'][i],
                  '6': tabl['6'][i], 'p_final': tabl['p_final'][i], 'r71': rs[0], 'r72': rs[1], 'r73': rs[2],
                  'r81': rss[0], 'r82': rss[1], 'r83': rss[2], 'r84': rss[3], 'r85': rss[4], 'R71': rs1[0],
                  'R72': rs1[1], 'R73': rs1[2], 'R81': rss1[0], 'R82': rss1[1], 'R83': rss1[2], 'R84': rss1[3],
                  'R85': rss1[4], 'pR71': rs2[0], 'pR72': rs2[1], 'pR73': rs2[2], 'pR81': rss2[0], 'pR82': rss2[1],
                  'pR83': rss2[2], 'pR84': rss2[3], 'pR85': rss2[4]}
            tabl2 = tabl2.append(ft, ignore_index=True)
        print(tabl2)
        tabl2.to_csv("endindVariants.csv")
        bzalt.to_csv("endindMorph.csv")
        ed1 = pd.Series([tabl2['pR71'].sum(), tabl2['pR72'].sum(), tabl2['pR73'].sum()], name="7.Дії держави")
        ed2 = pd.Series(
            [tabl2['pR81'].sum(), tabl2['pR82'].sum(), tabl2['pR83'].sum(), tabl2['pR84'].sum(), tabl2['pR85'].sum()],
            name="8.Дії керівництва компанії")
        df = pd.concat([ed1, ed2], axis=1)
        """print(df.where(df['p_final'].max()==))"""
        ed2.to_csv("decisions.csv")

        kik = tabl2.iloc[[tabl2['p_final'].idxmax()]]

        self.resultConfig = kik.loc[:,"1":"p_final"]
        self.data.morphTable=bzalt
        self.data.connectionTable=tabl2
        self.data.matrixOfUzgodzhiennia=df

