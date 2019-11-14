import sys, json, csv, shutil, os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from flask import Flask

datos = json.loads(sys.argv[1])


goalWords = word_tokenize(str(datos["goals"]))
userWords = word_tokenize(str(datos["users"]))
sourceWords = word_tokenize(str(datos["sources"]))
conceptWords = word_tokenize(str(datos["concepts"]))

filteredGoals = []
filteredUsers = []
filteredSources = []
filteredConcepts = []
filteredIndicators = []
filteredConceptgens = []
filteredIndicatorgens = []
filteredVisualizations = []
filteredEnvironments = []

superfilteredGoals = []
superfilteredUsers = []
superfilteredSources = []
superfilteredConcepts = []
superfilteredIndicators = []
superfilteredConceptgens = []
superfilteredIndicatorgens = []
superfilteredVisualizations = []
superfilteredEnvironments = []

def limpiar(wordsObject):
    wordy = ''
    limpioObject = []
    stop_words = set(stopwords.words("spanish"))
    for w in wordsObject:
        if w not in stop_words and w != "[" and w != "]" and w != "," and w != "." and w != "'":
            wordy = w.replace("'", "")
            limpioObject.append(wordy)
    return limpioObject        


def refinar(filteredObject):
    superfilteredObject = []
    sentence = ''
    for w in filteredObject:
        if w.isupper():
            if filteredObject.index(w) == len(filteredObject)-1:
                superfilteredObject.append(sentence)
                superfilteredObject.append(w)
            else: 
                if not filteredObject[filteredObject.index(w)+1].isupper() and not filteredObject[filteredObject.index(w)+1].islower(): #If proxima palabra mayuscula
                    superfilteredObject.append(sentence)
                    sentence = ''
                    superfilteredObject.append(w)
                else:
                    sentence = w
        else:
            sentence = sentence + ' ' + w
            if filteredObject.index(w) == len(filteredObject)-1:
                superfilteredObject.append(sentence)
            else:
                if not filteredObject[filteredObject.index(w)+1].isupper() and not filteredObject[filteredObject.index(w)+1].islower(): #If proxima palabra mayuscula
                    superfilteredObject.append(sentence)
                    sentence = ''    
    return superfilteredObject                


filteredGoals = limpiar(goalWords)
filteredUsers = limpiar(userWords)
filteredSources = limpiar(sourceWords)
filteredConcepts = limpiar(conceptWords)
filteredIndicators = limpiar(indicatorWords)
filteredConceptgens = limpiar(conceptGenWords)
filteredIndicatorgens = limpiar(indicatorGenWords)
filteredVisualizations = limpiar(visualizationWords)
filteredEnvironments = limpiar(environmentWords)

superfilteredGoals = refinar(filteredGoals)
superfilteredUsers = refinar(filteredUsers)
superfilteredSources = refinar(filteredSources)
superfilteredConcepts = refinar(filteredConcepts)
superfilteredIndicators = refinar(filteredIndicators)
superfilteredConceptgens = refinar(filteredConceptgens)
superfilteredIndicatorgens = refinar(filteredIndicatorgens)
superfilteredVisualizations = refinar(filteredVisualizations)
superfilteredEnvironments = refinar(filteredEnvironments)

# superfilteredGoals[0] = 'goals: ' + superfilteredGoals[0]
# superfilteredUsers[0] = 'users: ' + superfilteredUsers[0]
# superfilteredSources[0] = 'sources: ' + superfilteredSources[0]
# superfilteredConcepts[0] = 'concepts: ' + superfilteredConcepts[0]
# superfilteredIndicators[0] = 'indicators: ' + superfilteredIndicators[0]
# superfilteredConceptgens[0] = 'conceptgens: ' + superfilteredConceptgens[0]
# superfilteredIndicatorgens[0] = 'indicatorgens: ' + superfilteredIndicatorgens[0]
# superfilteredVisualizations[0] = 'visualizations: ' + superfilteredVisualizations[0]
# superfilteredEnvironments[0] = 'environments: ' + superfilteredEnvironments[0]

super1 = ""
super2 = ""
super3 = ""
super4 = ""
super5 = ""
super6 = ""
super7 = ""
super8 = ""
super9 = ""

for w in superfilteredGoals:
    super1 += w
for w in superfilteredUsers:
    super2 += w
for w in superfilteredSources:
    super3 += w
for w in superfilteredConcepts:
    super4 += w
for w in superfilteredIndicators:
    super5 += w
for w in superfilteredConceptgens:
    super6 += w
for w in superfilteredIndicatorgens:
    super7 += w
for w in superfilteredVisualizations:
    super8 += w
for w in superfilteredEnvironments:
    super9 += w

super10 = '' + super1 + super2 + super3 + super4 + super5 + super6 + super7 + super8 + super9 + ''
superMega = []
header = []
superMega.append(super10)

with open('./datasets/empty.csv', mode='w') as empty_file:
    to_write = csv.writer(empty_file)
    to_write.writerow(superMega)


# Seccion de crear y escribir .txt files que se comprimiran en un 
# .zip para ser utilizado como dataset en el modelo de autoML.
 
# with open("./datasets/goals.txt", "w") as f:   # Opens file and casts as f 
#     f.write('"')
#     f.write('goals: ')
#     for w in superfilteredGoals:
#         if superfilteredGoals.index(w) != superfilteredGoals.index(superfilteredGoals[len(superfilteredGoals)-1]):
#             f.write(w + ', ')
#         else:
#             f.write(w + '"')    

# with open("./datasets/users.txt", "w") as f:   # Opens file and casts as f 
#     f.write('"')
#     f.write('users: ')
#     for w in superfilteredUsers:
#         if superfilteredUsers.index(w) != superfilteredUsers.index(superfilteredUsers[len(superfilteredUsers)-1]):
#             f.write(w + ', ')
#         else:
#             f.write(w + '"')

# with open("./datasets/sources.txt", "w") as f:   # Opens file and casts as f 
#     f.write('"')
#     f.write('sources: ') 
#     for w in superfilteredSources:
#         if superfilteredSources.index(w) != superfilteredSources.index(superfilteredSources[len(superfilteredSources)-1]):
#             f.write(w + ', ')
#         else:
#             f.write(w + '"')
    
# with open("./datasets/concepts.txt", "w") as f:   # Opens file and casts as f 
#     f.write('"')    
#     f.write('concepts: ') 
#     for w in superfilteredConcepts:
#         if superfilteredConcepts.index(w) != superfilteredConcepts.index(superfilteredConcepts[len(superfilteredConcepts)-1]):
#             f.write(w + ', ')
#         else:
#             f.write(w + '"')

# with open("./datasets/indicators.txt", "w") as f:   # Opens file and casts as f 
#     f.write('"')
#     f.write('indicators: ')
#     for w in superfilteredIndicators:
#         if superfilteredIndicators.index(w) != superfilteredIndicators.index(superfilteredIndicators[len(superfilteredIndicators)-1]):
#             f.write(w + ', ')
#         else:
#             f.write(w + '"')

# with open("./datasets/conceptGens.txt", "w") as f:   # Opens file and casts as f 
#     f.write('"')
#     f.write('conceptGens: ')
#     for w in superfilteredConceptgens:
#         if superfilteredConceptgens.index(w) != superfilteredConceptgens.index(superfilteredConceptgens[len(superfilteredConceptgens)-1]):
#             f.write(w + ', ')
#         else:
#             f.write(w + '"')

# with open("./datasets/indicatorGens.txt", "w") as f:   # Opens file and casts as f 
#     f.write('"')
#     f.write('indicatorGens: ')
#     for w in superfilteredIndicatorgens:
#         if superfilteredIndicatorgens.index(w) != superfilteredIndicatorgens.index(superfilteredIndicatorgens[len(superfilteredIndicatorgens)-1]):
#             f.write(w + ', ')
#         else:
#             f.write(w + '"')

# with open("./datasets/visualizations.txt", "w") as f:   # Opens file and casts as f 
#     f.write('"')
#     f.write('visualizations: ')
#     for w in superfilteredVisualizations:
#         if superfilteredVisualizations.index(w) != superfilteredVisualizations.index(superfilteredVisualizations[len(superfilteredVisualizations)-1]):
#             f.write(w + ', ')
#         else:
#             f.write(w + '"')

# with open("./datasets/environments.txt", "w") as f:   # Opens file and casts as f 
#     f.write('"')
#     f.write('environments: ')
#     for w in superfilteredEnvironments:
#         if superfilteredEnvironments.index(w) != superfilteredEnvironments.index(superfilteredEnvironments[len(superfilteredEnvironments)-1]):
#             f.write(w + ', ')
#         else:
#             f.write(w + '"')

shutil.make_archive('dataset', 'zip', './datasets')

sys.stdout.flush()