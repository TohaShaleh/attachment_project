
toha={

    'aa':100,
    'ab':102,
    'ac':104,
    'ad':106

}

value=102
if value in toha.values():
    print(f'\nthe value : {value} exists in the dictionary')
else:
    print('\ndoes not exist')
print('')

result=False
for k,v in toha.items():
    if v==value:
        print(f'The value : {value} exist,,Alhamdulillah')
        print(f'And Its key  is : {k}')
        result=True;
        break;
if result==False:
    print('\nThe value does not exist\n\n')
d=toha['ab']

print(f'\n{d}\n')

    
