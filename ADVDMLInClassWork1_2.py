# -*- coding: utf-8 -*-
"""
Created on Tue May 15 17:11:53 2018

@author: fengh
"""

# Q1
import pandas as pd
from io import StringIO
data1 = """
ID	Sales
1	7641
7	6621
6	8089
9	4719
7	2162
4	5235
2	2082
9	3887
5	4782
3	2576
8	6701
9	2154
8	3546
7	8648
5	9777
7	3143
7	2768
5	8518
1	8063
9	9086
5	8942"""
Qtr1 = pd.read_table(StringIO(data1), sep="\s+")
Qtr1.head(5)

data2 = """
ID	Sales
2	7668
7	7365
7	1837
5	1320
4	3674
2	9952
4	7874
9	4598
4	7393
5	5986
7	1120
2	2323
5	9756
3	7382
2	8156
1	8620
4	5689
5	6785
7	8425
1	1976
7	1858"""
Qtr2 = pd.read_table(StringIO(data2), sep="\s+")
Qtr2.head(5)
# Q2
# part a
sheet1 = """
1	4	X	9
2	3	W	5
3	2	W	7
4	4	X	7
5	3	W	5
6	5	CE	6
1	6	E	5
6	4	W	7
1	3	V	5
2	4	S	7
2	7	W	3
4	9	W	9
2	7	X	9
2	5	V	2
4	7	S	7
5	6	V	6
5	1	S	5
1	7	V	3
1	7	S	9
3	7	W	2
6	8	X	9
5	5	CE	8
6	5	CE	7
4	5	W	2
2	7	X	8
5	3	CE	3
2	2	S	5
1	4	V	2
2	1	CE	9
1	3	W	3
2	3	S	8
2	5	V	4"""
Sheet1 = pd.read_table(StringIO(sheet1), sep="\s+")
Sheet1 = pd.DataFrame(Sheet1, columns = ["Person", "Quantity", "Label", "Data"])
Sheet1.head(5)

# part b
# Dont' quite sure about this one
# Do you mean read from original file again?
# if so, what's the point to repeat same process as part a?
col3 = """
1	4	X
2	3	W
3	2	W
4	4	X
5	3	W
6	5	CE
1	6	E
6	4	W
1	3	V
2	4	S
2	7	W
4	9	W
2	7	X
2	5	V
4	7	S
5	6	V
5	1	S
1	7	V
1	7	S
3	7	W
6	8	X
5	5	CE
6	5	CE
4	5	W
2	7	X
5	3	CE
2	2	S
1	4	V
2	1	CE
1	3	W
2	3	S
2	5	V"""
Col3 = pd.read_table(StringIO(col3), sep="\s+")
Col3 = pd.DataFrame(Col3, columns = ["ID", "Quantity", "Total"])
Col3.head(5)

# part c
sheet2 = """
Flavor	Data
Choc	23
Van	12
Van	43
Choc	32
Van	43
Choc	91
Van	29
Choc	31
Choc	75
Choc	34"""
Sheet2 = pd.read_table(StringIO(sheet2), sep="\s+)





