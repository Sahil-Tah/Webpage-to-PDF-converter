file = 'templates/index.html'
file2 = 'templates/index2.html'

from re import sub
#import datetime

#now = datetime.datetime.now()
#dt = now

file_open = open(file, 'r')
file_read = file_open.read()
file_open.close()

new_file_open = open(file2, 'w')

#Based on dict, replaces key with the value on the target.
def replace_content(dict_replace, target):
    for check, replacer in list(dict_replace.items()):
        target = sub(check, replacer, target)
        # target = target.replace(check, replacer)

    return target


# check : replacer
dict_replace = {'{{package}}': 'PEPTize', '{{student}}': 'Yashvant Singh', '{{level}}': 'Level 1'}
#dict_replace = {'{{package}}': 'PEPTize', '{{student}}': 'Yashvant Singh', '{{level}}': 'Level 1', '{{certdate}}': dt}

new_content = replace_content(dict_replace, file_read)
new_file_open.write(new_content)
new_file_open.close()

# Test
print(file_read)

print(new_content)
