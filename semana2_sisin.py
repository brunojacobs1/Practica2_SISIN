class Cola:

    def __init__(cola):
        cola.contenido = []

    def __str__(cola):
        resultado = "Contenido " + str(len(cola.contenido)) + " items\n"
        for i in cola.contenido:
            resultado += str(i) + "\n"
        return resultado

    def add(cola, nodo):
        cola.contenido.append(nodo)

    def remove(cola):
        if not cola.vacio():
            return cola.contenido.pop(0)
        else:
            raise Exception("Sin contenido")

    def vacio(cola):
        return len(cola.contenido) == 0

class Nodo:

    def __init__(nodo, estado, anterior, accion, profundidad):
        nodo.estado = estado
        nodo.anterior = anterior
        nodo.accion = accion
        nodo.profundidad = profundidad

    def __str__(nodo):
        resultado = "Estado: " + str(nodo.estado)
        resultado += " Profundidad: " + str(nodo.profundidad)
        if nodo.anterior != None:
            resultado += " Anterior: " + str(nodo.anterior.estado)
            resultado += " accion: " + nodo.accion
        return resultado
    
    def estadoRepetido(nodo):
        if nodo.anterior == None: return 0
        if nodo.anterior.anterior == None: return 0
        if nodo.anterior.anterior.estado.equals(nodo.estado): return 1
        return 0

class Busqueda:

    def __init__(busqueda, estadoInicial, estadoObjetivo):
        busqueda.c = Cola()
        busqueda.c.add(Nodo(estadoInicial, None, None, 0))
        busqueda.estadoObjetivo = estadoObjetivo
        solucion = busqueda.ejecutar()
        if solucion == None:
            print("Busqueda Fallida")
        else:
            busqueda.mostrarSolucion(solucion)

    def ejecutar(busqueda):
        while not busqueda.c.vacio():
            actual = busqueda.c.remove()
            if busqueda.estadoObjetivo.equals(actual.estado):
                return actual
            else:
                sucesores = actual.estado.aplicarAccion()
                acciones = actual.estado.descAccion()
                for i in range(len(sucesores)):
                    if sucesores[i].legal():
                        n = Nodo(sucesores[i],
                                 actual,
                                 acciones[i],
                                 actual.profundidad+1)
                        if n.estadoRepetido():
                            del(n)
                        else:
                            busqueda.c.add(n)
        return None

    def mostrarSolucion(busqueda, nodo):
        camino = busqueda.construirCamino(nodo)
        for actual in camino:
            if actual.profundidad != 0:
                print("Accion: ", actual.accion)
            print(actual.estado)
        print("Objetivo alcanzado en ", actual.profundidad, "pasos")

    def construirCamino(busqueda, nodo):
        resultado = []
        while nodo != None:
            resultado.insert(0, nodo)
            nodo = nodo.anterior
        return resultado

class Problema:

    def __init__(problema, misioneros, Canibales, bote):
        problema.misioneros = misioneros
        problema.Canibales = Canibales
        problema.bote = bote

    def __str__(problema):
        return "("+str(problema.misioneros)+","+str(problema.Canibales)+","+ str(problema.bote)+")"

    def legal(problema):
        if problema.misioneros < 0 or problema.Canibales < 0 or problema.misioneros > 3 or problema.Canibales > 3 or (problema.bote != 0 and problema.bote != 1):
            return False
        if problema.Canibales > problema.misioneros and problema.misioneros > 0:
            return False
        if problema.Canibales < problema.misioneros and problema.misioneros < 3:
            return False
        return True

    def equals(e, estado):
        return e.misioneros == estado.misioneros and e.Canibales == estado.Canibales and e.bote == estado.bote

    def moverMisionero(problema):
        return Problema(problema.misioneros-1, problema.Canibales, problema.bote-1)

    def moverCanibal(problema):
        return Problema(problema.misioneros, problema.Canibales-1, problema.bote-1)

    def regresarMisionero(problema):
        return Problema(problema.misioneros+1, problema.Canibales, problema.bote+1)

    def regresarCanibal(problema):
        return Problema(problema.misioneros, problema.Canibales+1, problema.bote+1)

    def moverMisioneros(problema):
        return Problema(problema.misioneros-2, problema.Canibales, problema.bote-1)

    def moverCanibales(problema):
        return Problema(problema.misioneros, problema.Canibales-2, problema.bote-1)

    def regresarMisioneros(problema):
        return Problema(problema.misioneros+2, problema.Canibales, problema.bote+1)

    def regresarCanibales(problema):
        return Problema(problema.misioneros, problema.Canibales+2, problema.bote+1)

    def moverMisioneroCanibal(problema):
        return Problema(problema.misioneros-1, problema.Canibales-1, problema.bote-1)

    def regresarMisioneroCanibal(problema):
        return Problema(problema.misioneros+1, problema.Canibales+1, problema.bote+1)

    def descAccion(problema):
        return ["Mover misionero", "Mover Canibal", "Regresar misionero",
                "Regresar Canibal", "Mover 2 misioneros", "Mover 2 Canibales",
                "Regresar 2 misioneros", "Regresar 2 Canibales", "Mover misionero y Canibal",
                "Regresar misionero y Canibal"]

    def aplicarAccion(problema):
        return [problema.moverMisionero(), problema.moverCanibal(), problema.regresarMisionero(), problema.regresarCanibal(),
                problema.moverMisioneros(), problema.moverCanibales(), problema.regresarMisioneros(), problema.regresarCanibales(),
                problema.moverMisioneroCanibal(), problema.regresarMisioneroCanibal()]

b = Busqueda(Problema(3,3,1),Problema(0,0,0))
