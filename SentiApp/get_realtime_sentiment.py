from encoder import Model
import csv
import time
model=Model()
def get_activations(text):
	activations = []
	temp2 = []
	new_text = []
	for i in range(len(text)):
		new_text.append(text[i])
		temp_text = ''.join(new_text)
		temp2.append(temp_text)
	print ("Transforming")
	print ("Number of samples to transform " + str(len(temp2)))
	a = time.time()
	text_features = model.transform(temp2)
	b = time.time()
	c = b - a
	print ("Time taken to transform: " + str(c) + " secs")

	
	for i in range(len(temp2)):
		sentiment = text_features[i, 2388]
		activations.append(sentiment)
	list1 = []
	for i in range(len(text)):
		list1.append([text[i], activations[i]])


	return list1




