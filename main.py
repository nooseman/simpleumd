import visualize, collect
from collect import cfg

choice = input('Do you want to create an intermediary CSV file to track data?\n')
choice = choice.lower()

nos = ('no', 'nope', 'no thanks', 'n', '\n', '')
yeses = ('yes', 'yep', 'ye', 'y')


#while choice not in nos or choice not in yeses or choice != 'quit':
while choice not in nos and choice not in yeses and choice != 'quit':
	print('Hmm. I don\'t know what that means.\n')
	choice = input('Do you want to create an intermediary CSV file to track data?\n')
	choice = choice.lower()

if choice in nos:
	visualize.graphMatrix(collect.collectToMatrix())
elif choice in yeses:
	collect.collectToCSV()
	visualize.graphCSV(cfg['FILENAME'])