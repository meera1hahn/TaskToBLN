import sys
import nltk
from nltk.parse.stanford import StanfordDependencyParser
path_to_jar = '/home/meerahahn/Documents/software/stanford-corenlp-full-2016-10-31/stanford-corenlp-3.7.0.jar'
path_to_models_jar = '/home/meerahahn/Documents/software/stanford-corenlp-full-2016-10-31/stanford-corenlp-3.7.0-models.jar'
dependency_parser = StanfordDependencyParser(path_to_jar=path_to_jar, path_to_models_jar=path_to_models_jar)

queries = []

query_types = {'isa':'IsA(Object1,', 'loc':'AtLocation(Object1,', 'use':'UsedFor(Object1,', 'prop':'HasProperty(Object1,'}

def get_question_type(obj):
	if "where" in sentence or "location" in sentence:
		question_type = query_types['loc']
		return question_type + obj + ')'
	return None	

def get_attributes(dep_list, obj):
	modifiers = ['compound', 'nmod', 'amod']
	for dep in dep_list:
		if dep[1] in modifiers:
			if dep[0][0] == obj:
				return dep[2][0]
			if dep[2][0] == obj:
				return dep[0][0]
	return None

def get_object(pos_list, dep_list):
	potential_obj = []
	for each in pos_list:
		if each[1] == 'NN' or each[1] == 'NNS':
			potential_obj.append(each[0])
	if len(potential_obj) == 0:
		return ""
	if len(potential_obj) == 1:
		return potential_obj[0]
	obj = potential_obj[len(potential_obj) - 1]
	for dep in dep_list:
		    if dep[1] == 'case':
				if dep[0][0] in potential_obj:
					obj = dep[0][0]
				elif dep[2][0] in potential_obj:
					obj = dep[2][0]
	return obj

def parseQuery(sentence):
	text = nltk.word_tokenize(sentence)
	pos_list = nltk.pos_tag(text)
	result = dependency_parser.raw_parse(sentence)
	dep = result.next()
	dep_list = list(dep.triples())
	return pos_list, dep_list

if __name__ == '__main__':
	sentence = "where is the red cup"

	#parse sentence for dependency tree and parts of speech
	[pos_list, dep_list] = parseQuery(sentence)

	#get the object in question
	obj = get_object(pos_list, dep_list)
	if obj == "":
		print "no object found"

	#add attributes
	att = get_attributes(dep_list, obj)
	if att:
		queries.append(query_types['prop']+att + ')')

	#asking add location query
	loc = get_question_type(obj)
	if loc:
		queries.append(loc)

	print queries
