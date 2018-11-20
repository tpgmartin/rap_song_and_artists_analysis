from copy import deepcopy
from random import randint

artists = ['BROCKHAMPTON', 'Drake', 'Eminem', 'Future', 'Gucci Mane',
                 'J. Cole', 'Kendrick Lamar', 'Kevin Gates', 'Kodak Black',
                 'Lil Uzi Vert', 'Lil Yachty', 'Migos', 'Moneybagg Yo', 'NF',
                 'Post Malone', 'Russ', 'Wiz Khalifa', 'YoungBoy Never Broke Again']

for i in range(5):

    artists_copy = deepcopy(artists)
    targetIndex = randint(0,len(artists_copy)-1)
    targetArtist = artists_copy[targetIndex]

    title = "Which of the artists below is most similar to " + targetArtist + "?"
    print(title)
  
    del artists_copy[targetIndex]
    for j in range(5):
        choiceIndex = randint(0,len(artists_copy)-1)
        choiceValue = artists_copy[choiceIndex]
        del artists_copy[choiceIndex]
        print(choiceValue)
    
    print('---------------\n')