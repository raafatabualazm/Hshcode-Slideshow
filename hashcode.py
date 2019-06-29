vListCombine = []
outputList = []
vList = []
hList = []


def findCommonTags(a, b):
    a = a[3:]
    b = b[3:]
    return list(set(a) & set(b))

def sortThePics(a, b):

    while len(a) != 0 or len(b) != 0:
        max_so_far_a = 0
        max_so_far_b = 0
        max_so_far_c = 0
        max_so_far_d = 0
        a_index = 1
        b_index = 0
        while a_index < len(a):
            x1 = len(set(a[0][2:]) & set(a[a_index][2:]))
            x2 = len(set(a[0][2:]) - set(a[a_index][2:]))
            x3 = len(set(a[a_index][2:]) - set(a[0][2:]))
            score = min(x1, x2, x3)
            if score > max_so_far_a:
                max_so_far_a = score
                a_index_2 = a_index
            a_index += 1

        while b_index < len(b) and len(a) != 0:
            y1 = len(set(a[0][2:]) & set(b[b_index][3:]))
            y2 = len(set(a[0][2:]) - set(b[b_index][3:]))
            y3 = len(set(b[b_index][3:]) - set(a[0][2:]))
            score = min(y1, y2, y3)
            if score > max_so_far_b:
                max_so_far_b = score
                b_index_2 = b_index
            b_index += 1

        a_index = 0
        b_index = 1
        while a_index < len(a) and len(b) != 0:
            z1 = len(set(b[0][3:]) & set(a[a_index][2:]))
            z2 = len(set(b[0][3:]) - set(a[a_index][2:]))
            z3 = len(set(a[a_index][2:]) - set(b[0][3:]))
            score = min(z1, z2, z3)
            if score > max_so_far_c:
                max_so_far_c = score
                a_index_3 = a_index
            a_index += 1

        while b_index < len(b):
            w1 = len(set(b[0][3:]) & set(b[b_index][3:]))
            w2 = len(set(b[0][3:]) - set(b[b_index][3:]))
            w3 = len(set(b[b_index][3:]) - set(b[0][3:]))
            score = min(w1, w2, w3)
            if score > max_so_far_d:
                max_so_far_d = score
                b_index_3 = b_index
            b_index += 1

        if max(max_so_far_a,max_so_far_b,max_so_far_c,max_so_far_d) == max_so_far_a and len(a) != 0:
            outputList.append(a[0][0])
            outputList.append(a[a_index_2][0])
            a.pop(0)
            a.pop(a_index_2-1)
        elif max(max_so_far_a,max_so_far_b,max_so_far_c,max_so_far_d) == max_so_far_b and (len(a) != 0 and len(b) != 0):
            outputList.append(a[0][0])
            outputList.append((b[b_index_2][1], b[b_index_2][2]))
            a.pop(0)
            b.pop(b_index_2)
        elif max(max_so_far_a,max_so_far_b,max_so_far_c,max_so_far_d) == max_so_far_d and len(b) != 0:
            outputList.append((b[0][1], b[0][2]))
            outputList.append((b[b_index_3][1], b[b_index_3][2]))
            b.pop(0)
            b.pop(b_index_3-1)
        elif max(max_so_far_a,max_so_far_b,max_so_far_c,max_so_far_d) == max_so_far_c and (len(a) != 0 and len(b) != 0):
            outputList.append((b[0][1], b[0][2]))
            outputList.append(a[a_index_3][0])
            b.pop(0)
            a.pop(a_index_3)

        if len(a) == 1:
            outputList.append(a[0][0])
            a.pop(0)
        elif len(b) == 1:
            outputList.append((b[0][1], b[0][2]))
            b.pop(0)


def findMostCommonTags(c):
    indx1 = 0
    indx2 = -1
    while indx1 < len(c):
        max_so_far = 0
        union = ['V']
        for k in range(indx1 + 1, len(c)):
            com = findCommonTags(c[indx1], c[k])
            if len(com) > max_so_far:
                max_so_far = len(com)
                indx2 = k

        if max_so_far == 0:
            indx1 += 1
        else:
            union.append(c[indx1][0])
            union.append(c[indx2][0])
            union += list(set().union(c[indx1][3:], c[indx2][3:]))
            vListCombine.append(union)
            c.pop(indx1)
            c.pop(indx2-1)
    indx1 = 0
    while len(c) != 0:
        max_so_far = 0
        union = ['V']
        # for k in range(1, len(c)):
        #     com = findCommonTags(c[indx1], c[k])
        #     if len(com) > max_so_far:
        #         max_so_far = len(com)
        #         indx2 = k
        #         union.append(c[indx1][0])
        #         union.append(c[indx2][0])
        #         union += list(set().union(c[indx1][3:], c[indx2][3:]))
        if max_so_far == 0:
            indx2 = len(c) - 1
            union.append(c[indx1][0])
            union.append(c[indx2][0])
            union += list(set().union(c[indx1][3:], c[indx2][3:]))

        vListCombine.append(union)
        c.pop(indx1)
        if len(c) != 0:
            c.pop(indx2-1)


n = input()
n = int(n)
for i in range(n):
    inputElem = input()
    inputElem = str(i) + " " + inputElem
    inputElem = inputElem.split()
    if inputElem[1] == 'H':
        hList.append(inputElem)
    else:
        vList.append(inputElem)
findMostCommonTags(vList)

sortThePics(hList, vListCombine)
print(len(outputList))
for elem in outputList:
    if type(elem) == tuple:
        print(elem[0], elem[1])
    else:
        print(elem)
