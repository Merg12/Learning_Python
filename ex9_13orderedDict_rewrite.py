from collections import OrderedDict

new_glossary = OrderedDict()

new_glossary['if'] = 'conditional statement'
new_glossary['not'] = 'inverses'
new_glossary['elif'] = 'similar to else if'
new_glossary['key'] = 'what you look for'
new_glossary['value'] = 'value associated with key'
new_glossary['morgan'] = 'a happy dude'
new_glossary['logan'] = 'a happy boy'

for key,value in new_glossary.items():
    print(str(key) + " means its a " + str(value))