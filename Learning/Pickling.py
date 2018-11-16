import pickle

#
# imelda = ('More mayhem',
#           'Imelda May',
#           '2011',
#           ((1,'Pulling the rug'),
#            (2, 'Psycho'),
#            (3, 'Mayhem'),
#            (4, 'Kentish town Waltz')))
#
# with open('D:\Python file\imelda.pickle', 'wb') as pickle_file:
#     pickle.dump(imelda, pickle_file)

# with open('D:\Python file\imelda.pickle', "rb") as imelda_pickled:
#     imelda2 = pickle.load(imelda_pickled)
#
# print(imelda2)
#
# album, artist, year, track_list = imelda2
#
# print(album)
# print(artist)
# print(year)
# for track in track_list:
#     track_number, track_title = track
#     print(track_number, track_title)


imelda = ('More mayhem',
          'Imelda May',
          '2011',
          ((1,'Pulling the rug'),
           (2, 'Psycho'),
           (3, 'Mayhem'),
           (4, 'Kentish town Waltz')))

even = (0, 10, 2)
odd = (1, 10, 2)

with open('D:\Python file\imelda.pickle', 'wb') as pickle_file:
    pickle.dump(imelda, pickle_file)
    pickle.dump(even, pickle_file)
    pickle.dump(odd, pickle_file)
    pickle.dump(2998302, pickle_file)

