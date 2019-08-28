# enter student list

# if yann is in emilie's choices: match yann with emilie
student_list = ['yann', 'emilie', 'margaux', 'loic', 'bobby', 'dolly', 'iggy']
no_go_list = []
chosen_list = []

# make student doing choices
student_dict = {
    'yann': {
        'choice1': 'emilie',
        'choice2': 'margaux'
    },
    'emilie': {
        'choice1': 'yann',
        'choice2': 'margaux'
    },
    'margaux': {
        'choice1': 'loic',
        'choice2': 'yann'
    },
    'loic': {
        'choice1': 'margaux',
        'choice2': 'emilie'
    },
    'bobby': {
        'choice1': 'marc',
        'choice2': 'billy'
    },
    'dolly': {
        'choice1': 'marc',
        'choice2': 'iggy'
    },
    'iggy': {
        'choice1': 'marc',
        'choice2': 'dolly'
    }
}

# print('*'*50)

for i in student_list:
    if i in no_go_list:
        pass
    elif i not in no_go_list:
        for u in student_dict:
            if i == student_dict[u]['choice1'] and u == student_dict[i]['choice1']:
                print(i, ' is matched, first choice with ', student_dict[i]['choice1'])
                no_go_list.append(student_dict[i]['choice1'])
                chosen_list.append(i)
                chosen_list.append(student_dict[i]['choice1'])
        for u in student_dict:
            if i == student_dict[u]['choice2'] and u == student_dict[i]['choice2']:
                print(i, ' is matched, second choice with ', student_dict[i]['choice2'])
                no_go_list.append(student_dict[i]['choice2'])
                chosen_list.append(i)
                chosen_list.append(student_dict[i]['choice2'])


for person in student_list:
    if person not in chosen_list:
        print(person, ' has not been chosen by anybody!')
