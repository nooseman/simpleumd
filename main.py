import visualize, collect
from collect import cfg

choice = input('Do you want to create an intermediary CSV file to track data?')

if choice in ('no', 'nope', 'no thanks', 'NO', 'No', 'nO'):
	visualize.graphMatrix(collect.collectToMatrix())
elif choice in ('yes', 'yep', 'YES', 'Yep' ):
	pass