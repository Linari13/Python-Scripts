#Ask for distance and convert it to an integer
distance = int(input ('À quelle distance (en km) voulez-vous voyager ?'))

#Answer arccording to user's input
if distance >= 300:
  print('Je vous suggère de prendre l\'avion')
elif (distance>=3):
  print('Je vous suggère de conduire une voiture')
else:
  print('Vous pouvez marcher')

""" Could be:

# Determine what mode of transport to use.
if distance < 3:
  mode_of_transport = 'walking'
elif distance < 300:
  mode_of_transport = 'driving'
else:
  mode_of_transport = 'flying'

# Display the result.
print('I suggest {} to your destination.'.format(mode_of_transport))

"""
