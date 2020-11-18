'''
#######################################################
   Rapid Python Helper

   To access the workflow's global variable state, simply reference:
   rapid.global_vars
   rapid.global_vars is a normal python dictionary containing the entire global variable state

   Save data to the rapid workflow global variable state
   some_data = {'variable_name':'var_value'}
   rapid.save_to_workflow(some_data)

   Realtime print to the rapid console output
   rapid.print('Telstra Purple')

#######################################################
'''

from rapid import Rapid
rapid = Rapid()
rapid.print('Loaded - Rapid Python Helper')
# print out the global_vars
rapid.print(rapid.global_vars)