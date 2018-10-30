import json

with open('./data/songs_by_artists_since_2010.json') as data:
    d = json.load(data)
    for artist, song_title in d.items():
        if "With" in artist:
            print(artist, song_title)

        if "Featuring" in artist:
            artist = artist.split("Featuring")[0].strip()
        elif "Feat." in artist:
            artist = artist.split("Feat.")[0].strip()
        
        # edge case 
        if artist == "SOB X RBE":
            continue

        # edge case 
        if "X Ambassadors" in artist:
            continue

        if " vs " in artist:
            artist = artist.replace(" vs "," & ")
        elif " X " in artist:
            l = artist.split(" X ")
            if len(l) > 2:
                artist = ", ".join(l[:-1]) + " & " + l[-1]
            else:
                artist = " & ".join(l)
        elif " x " in artist:
            l = artist.split(" x ")
            if len(l) > 2:
                artist = ", ".join(l[:-1]) + " & " + l[-1]
            else:
                artist = " & ".join(l)

# Need to handle "With"
# Brad Paisley Duet With Carrie Underwood ['Remind Me']
# Chris Young Duet With Cassadee Pope ['Think Of You']
# Christina Aguilera With Blake Shelton ['Just A Fool']
# Enrique Iglesias With Usher Featuring Lil Wayne ['Dirty Dancer']
# Idina Menzel Duet With Michael Buble ["Baby It's Cold Outside"]
# Jason Aldean With Kelly Clarkson ["Don't You Wanna Stay"]
# Jason Aldean With Luke Bryan & Eric Church ['The Only Way I Know']
# Kenny Chesney With Grace Potter ['Wild Child']
# Lil Wayne, Wiz Khalifa & Imagine Dragons With Logic & Ty Dolla $ign Feat. X Ambassadors ['Sucker For Pain']
# Michael Jackson Duet With Akon ['Hold My Hand']
# Miranda Lambert Duet With Carrie Underwood ["Somethin' Bad"]
# Skrillex & Diplo With Justin Bieber ['Where Are U Now']
# Tim McGraw With Catherine Dunn ['Diamond Rings And Old Barstools']
# Tim McGraw With Taylor Swift ["Highway Don't Care"]