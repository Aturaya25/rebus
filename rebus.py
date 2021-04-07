from itertools import permutations

def findLetterToReplace(a, b):
    for i in range(max(len(a), len(b))):
        if i < len(a) and a[-i-1].isalpha():
            return a[-i-1], i+1
        if i < len(b) and b[-i-1].isalpha():
            return b[-i-1], i+1
    return '_', -1


def makeHypothesys(a, b, c, letters, digits):
    result = []
    if not letters:
        if int(a) + int(b) != int(c):
            return []
        return [a + '+' + b + '=' + c]
    l, i = findLetterToReplace(a, b)
    if l == '_':
        requiredDigit = str((int(a) + int(b)) // 10**(len(c)-1))
        if not requiredDigit in digits:
            return []
        if int(a) + int(b) != int(requiredDigit + c[1:]):
            return []
        return [a + '+' + b + '=' + requiredDigit + c[1:]]
    for j in range(len(digits)):
        aNew = a.replace(l, digits[j])
        bNew = b.replace(l, digits[j])
        cNew = c.replace(l, digits[j])
        lettersNew = letters.replace(l, '')
        if '0' in [aNew[0], bNew[0], cNew[0]]:
            continue
        if (i <= len(a) and aNew[-i].isalpha()) or (i <= len(b) and bNew[-i].isalpha()):
            result += makeHypothesys(aNew, bNew, cNew, lettersNew, digits[:j] + digits[j+1:])
            continue
        if cNew[-i].isdigit():
            if (int(aNew[-min(i, len(a)):]) + int(bNew[-min(i, len(b)):])) % 10**i != int(cNew[-min(i, len(c)):]):
                continue
            result += makeHypothesys(aNew, bNew, cNew, lettersNew, digits[:j] + digits[j+1:])
            continue
        requiredDigit = str((int(aNew[-min(i, len(a)):]) + int(bNew[-min(i, len(b)):])) % 10**i // 10**(i-1))
        if not requiredDigit in digits[:j] + digits[j+1:]:
            continue
        aNew = aNew.replace(c[-i], requiredDigit)
        bNew = bNew.replace(c[-i], requiredDigit)
        cNew = cNew.replace(c[-i], requiredDigit)
        lettersNew = lettersNew.replace(c[-i], '')
        digitsNew = (digits[:j] + digits[j+1:]).replace(requiredDigit, '')
        result += makeHypothesys(aNew, bNew, cNew, lettersNew, digitsNew)
    return result


s = input()

a = s.split('+')[0]
b = s.split('+')[1].split('=')[0]
c = s.split('=')[1]

alphabet = ''.join(list(dict.fromkeys(a+b+c)))
digits = '1234567890'

solutions = makeHypothesys(a, b, c, alphabet, digits)
solutions.sort()
for solution in solutions:
    print(solution)
if not solutions:
    print('NO')
