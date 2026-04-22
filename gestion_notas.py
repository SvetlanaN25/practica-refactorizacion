# gestion_notas.py - Sistema de gestión de notas de estudiantes
d = []
def f(n, no):
    x = 0
    ok = True
    for i in no:
        if i < 0 or i > 10:
            ok = False
    if ok == True:
        if len(no) > 0:
            for i in no:
                x = x + i
            p = x / len(no)
        else:
            p = 0
        if p >= 5:
            r = 'aprobado'
        else:
            r = 'suspenso'
        e = {'nombre': n, 'notas': no, 'promedio': p, 'resultado': r}
        d.append(e)
        return e
    else:
        print('Error: notas no validas')
        return None
 
def m():
    if len(d) == 0:
        print('No hay datos')
        return
    for i in d:
        print('Nombre: ' + i['nombre'] + ' | Promedio: ' + str(i['promedio']) + ' | ' + i['resultado'])
    print('---')
    t = 0
    ap = 0
    sus = 0
    for i in d:
        t = t + i['promedio']
        if i['resultado'] == 'aprobado':
            ap = ap + 1
        else:
            sus = sus + 1
    print('Media general: ' + str(t / len(d)))
    print('Aprobados: ' + str(ap) + ' Suspensos: ' + str(sus))
 
def b(nombre):
    for i in d:
        if i['nombre'] == nombre:
            return i
    return None
 
# --- Ejecución principal ---
f('Ana', [7, 8, 6, 9])
f('Luis', [4, 3, 5, 2])
f('Marta', [10, 9, 8, 10])
f('Pedro', [3, 2, 1, 4])
m()
r = b('Marta')
if r != None:
    print('Encontrado: ' + r['nombre'])
