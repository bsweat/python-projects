#DNA Sequencer project 1/7/2020 by Brandon Sweat, TR 1pm
import os


def fileToList(filename):
    lines = []
    if os.path.isfile(filename):
        file = open(filename)
        for line in file:
            lines.append(line.strip())
        file.close()
    return lines



def returnFirstString(strings):
    if strings != []:
        first = strings[0]
    elif strings == []:
        first = ''
    return first

def strandsAreNotEmpty(strand1,strand2):
    firstStrand = bool(strand1 != '')
    secondStrand = bool(strand2 != '')
    empty = firstStrand and secondStrand
    return empty

def strandsAreEqualLengths(strand1,strand2):
    len1 = len(strand1)
    len2 = len(strand2)
    equal = bool(len1 == len2)
    return equal

def candidateOverlapsTarget(target,candidate,overlap):
    overlapBool = False
    if target[-overlap:] == candidate[0:overlap]:
        overlapBool = True
    else:
        overlapBool = False
    return overlapBool

def findLargestOverlap(target,candidate):
    equality = strandsAreEqualLengths(target,candidate)
    if equality == True and target != '':
        length = len(target)
        lengthlist = range(0,length+1)
        longest = 0
        for x in lengthlist:
            overlaps = 0
            overlapBool = False
            if target[-x:] == candidate[0:x]:
                overlapBool = True
            else:
                overlapBool = False
            if overlapBool == True:
                if x > longest:
                    longest = x
                else:
                    pass
            else:
                pass
        return longest
        #longest type  = int
            
    else:
        return -1
    
def findBestCandidate(target,candidates):
    longest = 0
    candidate = ''
    for x in candidates:
        test = findLargestOverlap(target,x)
        if test > longest:
            longest = test
            candidate = x
    bestCandidate = (candidate,longest)
    return bestCandidate

def joinTwoStrands(target, candidate, overlap):
    joined = target + candidate[overlap:]
    return joined

'''
def main():
    targetFileName = input('Target strand filename')
    candidateFileName = input('Candidate strand filename')
    target = open(targetFileName)
    candidateList = fileToList(candidateFileName)
    candidateFirst = returnFirstString(candidateList)
    best = findBestCandidate(target,candidateList)
    print(best)
'''

def main():
    targetFileName = input('Target strand filename: ')
    candidateFileName = input('Candidate strand filename: ')
    fileToList(targetFileName)
    fileToList(candidateFileName)
    firstTarget = returnFirstString(targetFileName)
    firstCandidate = returnFirstString(candidateFileName)
    best = findBestCandidate(firstTarget,firstCandidate)
    finished = joinTwoStrands(firstTarget,best(0),best(1))
    print(finished)
    
if __name__ == '__main__':
    main()
    
    
        