#put the functions for the example print_models.py in a separate file
#called printing_function.py. write an import statement at the top of
#print_models.py and modify the file to use the imported functions

import printing_functions

unprinted_designs = ['blue', 'red', 'yellow']
completed_models = []

printing_functions.print_models(unprinted_designs, completed_models)