dic = {
    'clave': 'valor'
}

print(dic['clave'])
print("2", dic.get('clave'))


print("*" * 50)


dic2 = {x: x * 2 for x in range(10)}

print(dic2)