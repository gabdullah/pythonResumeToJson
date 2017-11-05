import json

from jsonschema import validate
import simplejson as simple

schema = {
	#"type": "object",
	"properties": {
		"basics": {
			"name": {"type": "string"},
			"label": {"type": "string"},
			"email": {"type": "string", "format": "email"},
			"phone": {"type": "string", "format": "phone"},
			"website": {"type": "string", "format": "uri"},
			"summary": {"type": "string"},
			"location": {
				"address": {"type": "string"},
				"postalCode": {"type": "integer"},
				"city": {"type": "string"},
				"countryCode": {"type": "string"},
				"region": {"type": "string"},
			},
			"profiles": {
				"type": "array",
				"items": [
					{"type": "string"},
					{"type": "string"},
					{"type": "string", "format": "uri"},
				],
			},
		},
		"work": {
			"type": "array",
			"items": [
				{"type": "string"},
				{"type": "string"},
				{"type": "string", "format": "uri"},
				{"type": "string", "format": "date"},
				{"type": "string", "format": "date"},
				{"type": "string"},
				{"type": "array", "items": {"type": "string"}},
			],
		},
		"volunteer": {
			"type": "array",
			"items": [
				{"type": "string"},
				{"type": "string"},
				{"type": "string", "format": "uri"},
				{"type": "string", "format": "date"},
				{"type": "string", "format": "date"},
				{"type": "string"},
				{"type": "array", "items": {"type": "string"}},
			],
		},
		"education": {
			"type": "array",
			"items": [
				{"type": "string"},
				{"type": "string"},
				{"type": "string"},
				{"type": "string", "format": "date"},
				{"type": "string", "format": "date"},
				{"type": "integer"},
				{"type": "array", "items": {"type": "string"}},
			],
		},
		"skills": {
			"type": "array",
			"items": [
				{"type": "string"},
				{"type": "string"},
			],
		},
		"languages": {
			"type": "array",
			"items": [
				{"type": "string"},
				{"type": "string"},
			],
		},
		"interests": {
			"type": "array",
			"items": [
				{"type": "string"},
				{"type": "array", "items": {"type": "string"}},
			],
		},
	},
}

with open('testResume.json', encoding="cp437") as jsonData:
#	data = json.load(jsonData)
	for temp in jsonData:
		temp = jsonData.read()
		data = json.load(jsonData)
		print(data)

#validate({data["basics"]["name"]}, schema)
#print(data["basics"]["profiles"])

#d = json.open('testResume.json').read()

#data = json.loads(d)

#print(simple.dumps('testResume.json'))
#simple.dumps('lmao')
