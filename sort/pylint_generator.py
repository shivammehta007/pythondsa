import os
import glob

PYLINT_SCORE_DIRECTORY = 'pylint_scores'
if not os.path.exists(PYLINT_SCORE_DIRECTORY):
    os.makedirs(PYLINT_SCORE_DIRECTORY)

for filename in glob.glob('*.py'):
    if filename == 'pylint_generator.py' or filename.startswith('__'):
        continue
    pylint_output_filename = '{}_sort_pylint.out'.format(filename.split('.')[0])
    final_ouput = os.path.join(PYLINT_SCORE_DIRECTORY, pylint_output_filename)
    print(final_ouput)
    os.system('pylint {} > {}'.format(filename, final_ouput))

print('PyLint Scores Generated Check Folder: {}'.format(PYLINT_SCORE_DIRECTORY))
