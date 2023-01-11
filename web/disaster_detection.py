# DISASTER DETECTION
def get_disasters(row):
  disasters = []
  content = row.lower()
  if any(word in content for word in ['covid', 'coronavirus']):
    disasters.append('COVID-19')
  if 'pandemic' in content:
    disasters.append('Hurricane')
  if 'hurricane' in content:
    disasters.append('Hurricane')
  if 'earthquake' in content:
    disasters.append('Earthquake')
  if 'flood' in content:
    disasters.append('Flood')
  if 'tsunami' in content:
    disasters.append('Tsunami')
  if 'wildfire' in content:
    disasters.append('Wildfire')
  if 'cyclone' in content:
    disasters.append('Cyclone')
  if 'tornado' in content:
    disasters.append('Tornado')
  if 'drought' in content:
    disasters.append('Drought')
  if 'landslide' in content:
    disasters.append('Landslide')
  if 'typhoon' in content:
    disasters.append('Typhoon')
  if len(disasters) == 0:
    return None
  else:
    return disasters

#count the no.of times each disaster type shows and show the top 2

from collections import Counter
 
def count_letters(filename):
  letter_counter = Counter()
  with open(filename) as file:
    for line in file:
      line_letters = [char for char in line.lower() if char.isalpha()]
      letter_counter.update(Counter(line_letters))
  return letter_counter