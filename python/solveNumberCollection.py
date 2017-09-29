from sympy import summation,Symbol,pprint

"""差の数列の一般項から元の数列の一般項を求める関数"""
def sigma(a,f):
    n = Symbol("n")
    return a + summation(f ,(n,1,n-1))

"""自分自身の数列の差を数列にし続け一般項を作り出す再帰関数"""
def difflist(l):
    n = Symbol("n")
    dlist = list(map(lambda a,b: b-a,l,l[1:]))
    if len(dlist) < 2:
        #差の配列があと一個になってしまったら、解は出ない
        exp = 0
    elif dlist[0]==dlist[1]:
        #等差数列になった段階で、一次方程式を作る
        if len(list(filter(lambda x: x != dlist[0],dlist))) == 0:
            exp = dlist[0]*n + l[0] - dlist[0]
        #等差数列と思われるのに、差が異なるものがあるときは不整合
        else:
            exp=0
    else:
        exp = difflist(dlist)
        if exp != 0:
            exp = sigma(l[0],exp)
    return exp

"""メインの処理だよ！"""
n = Symbol("n")
orglist = [0,1,7,22,50]
exp = difflist(orglist)

#結果表示するよ！
if exp != 0:
    pprint(exp)
    print(list(map(lambda a:exp.subs([(n, a)]),range(1,11))))
else:
    print("有効な等差数列型の数列でないか、ヒントが不十分です")