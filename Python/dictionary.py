#Dictionary :   Mapping

Dict = {}
Dict1 = dict()

print(type(Dict), type(Dict1))

print('Dict : ', Dict)
Dict["rollno"] = '0302EE221024'
print('Dict : ', Dict)
Dict['name'] = 'Prateek'
print('Dict\t: ', Dict)

Dict1 = {'name' : 'Arzoo', 'address' : 'Satna'}
Dict1['rollno'] = '0302EE221016'

print('Dict1\t: ', Dict1)

#Dictionary Key should be an immutable data type
#Dictionary Key should not a mutable data type

Shivani = {'rollno' : '0302EE221037', 
           'name' : {'firstName' : 'Shivani',
                     'lastName' : 'Bagri'}, 
           'add' : 'Satna', 
           'contact' : '+91-5648796321',
           'marks' : [12, 13, 20, 19],
           'course' : 'B.Tech',
           'branch' : 'Electrical Engineering',
           'semester' : 'V'}

print('-'*10, '*'*50, '-'*10)
#print(Shivani)     :   prints complete dictionary items
print('Marks Details :',Shivani['marks'])
print(Shivani['name']['firstName'])
print(Shivani.get('rollno'))