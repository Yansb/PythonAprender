welcome= "welcome to my nightmare", "Alice cooper", 1975
bad= "Bad Company", "Bad Company", 1974
budgie= "Nightflight","bugie", 1981
imelda= "More Mayhem", "Imilda May", 2011,((1, "Pulling the Rug"), (2, 'psycho'),(3,"Mayhem"), (4, "Kentish Town Waltz"),
(5, "All for you"),(6, "Eternity"),(7,"Inside Out"),(8,"Proud And Humble"),(9,"Sneaky Freak"),(10,"Bury My Troubles"),
(11,"Too Sad To Cry"),(12,"I'm Alive"),(13,"Let Me Out"),(14,"Tainted Love"),(15,"Johnny Got A Boom Boom"),
(16,"Road Runner"),(17,"Gypsy"),(18,"Blues Calling"),(19,"Walking After Midnight"),(20,"Inside Out - Remix"),
(21,"Proud And Humble - Remix")), "Germany"

#agora vamos "abrir" a tuple, e tirar o seu conteudo = unpacking
title, artist, year, tracks, country = imelda
print(title)
print(artist)
print(year)
for song in tracks:
    track, title = song
    print("\tSong number {}, {}".format(track, title))
print("country")