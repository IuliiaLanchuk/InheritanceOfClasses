DELIMITER = ' : '
inputRelations = {'': set()}
inheritanceMap = {'': set()}
interSetOfParents = set()


def accumulateParents(parent):
    ancestors = inputRelations.get(parent)
    if ancestors and len(ancestors) > 0:
        for ancestor in ancestors:
            accumulateParents(ancestor)

    interSetOfParents.add(parent)


def createChildParentLink(child, parents):
    allParents = set()
    allParents.add('Object')
    for i in range(len(parents)):
        accumulateParents(parents[i])
        allParents.update(interSetOfParents)
        interSetOfParents.clear()
    allParents.add(child)   #добавляем сами себя в список предков, т.к. класс сам себя наследует
    inheritanceMap[child] = allParents


def buildInheritanceMap(nClasses):  # шаг 1
    for i in range(nClasses):
        childParents = input().split(" : ")
        child = childParents[0]
        parents = []
        if len(childParents) > 1:
            parents = childParents[1].split(" ")
        inputRelations[child] = set(parents)

    for child, parents in inputRelations.items():
        createChildParentLink(child, list(parents))



def verifyInheritance(nChecks):
    for i in range(nChecks):
        parentChild = input().split(' ')
        child = parentChild[1]
        parent = parentChild[0]
        ancestors = inheritanceMap.get(child)
        print('Yes' if ancestors and parent in ancestors else 'No')


if __name__ == '__main__':
    nClasses = int(input())
    buildInheritanceMap(nClasses)
    nChecks = int(input())
    verifyInheritance(nChecks)