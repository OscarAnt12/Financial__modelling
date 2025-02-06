import time

try:
    IN = int(input("Ingrese la cantidad de flujos de caja de la serie: "))
    time.sleep(1)
    if IN > 3 and IN <= 20:
        HO = str(input("Escriba 'VA' si desea llevar estos flujos de caja a valor presente o 'VF' si desea llevar estos flujos de caja a valor futuro: "))
        time.sleep(1)
        BY = str(input("Escriba '+' si desea que haya intervalos crecientes de tiempo entre flujos de caja o '-' si desea que haya intervalos decrecientes de tiempo entre flujos de caja: "))
        time.sleep(1)
        RE = str(input("Escriba 'S' si el tipo de interés es simple o 'C' si el tipo de interés es compuesto: "))
        A = 2500000
        r = 0.03
        if HO == "VF" and BY == "-" and RE == "C":
            def ecuaciónValorFuturoDeSerieConInterésCompuestoConLiteralesConIntervalosDeTiempoDecrecientes():
                print()
                print("SE ESCRIBE LA SERIE DE PAGOS DE IGUAL VALOR E IGUAL TASA DE INTERÉS CON UN PATRON LINEAL DE DISMINUCIÓN EN LOS INTERVALOS ENTRE CADA PAGO")
                time.sleep(1)

                IF = "A*(1+r)"
                FCF1 = [f"{IF}^{i*(i+1)/2} " for i in range (IN)]
                print()
                print("La serie de flujos de caja es el siguiente: VF = ",FCF1)
                time.sleep(1)
            ecuaciónValorFuturoDeSerieConInterésCompuestoConLiteralesConIntervalosDeTiempoDecrecientes()
            print()

            def tablaValorFuturoDeSerieConInterésCompuestoConLiteralesConIntervalosDeTiempoDecrecientes():
                print("SE IMPRIME LA TABLA DE VALORES\n")
                print("    __________________ ____________________ ____________________________")
                print("   |                  |                    |            |               |")
                print("   |  VALOR PERIÓDICO |   TASA DE INTERÉS  |  MOMENTOS  |  VALOR FINAL  |")
                print("   |__________________|____________________|____________|_______________|")
                for i in range(IN):
                    print("   |    $",A,"    |    ",r*100,"% EBV      |   ",i*(i+1)/2,"    |  $",round(A*((1+r) ** (i*(i+1)/2)), 2)," |")
                    time.sleep(1)
                print("   |__________________|____________________|____________|_______________|")
                time.sleep(1)
            tablaValorFuturoDeSerieConInterésCompuestoConLiteralesConIntervalosDeTiempoDecrecientes()
            print()

            def ecuaciónValorFuturoDeSerieConInterésCompuestoConNúmerosConIntervalosDeTiempoDecrecientes():
                print("SE ESCRIBE LA SERIE DE PAGOS DE IGUAL VALOR E IGUAL TASA DE INTERÉS CON UN PATRON LINEAL DE DISMINUCIÓN EN LOS INTERVALOS ENTRE CADA PAGO")
                time.sleep(1)
                print()
                IF = "$2'500.000*(1+0.03)"
                FCF1 = [f"{IF}^{i*(i+1)/2} " for i in range (IN)]
                print("La serie de flujos de caja es el siguiente: VF = ",FCF1)
                time.sleep(1)
                print()
                IF1 = 1+0.03
                FCF2 = [f"{"$"}{A}*{round(IF1 ** (i*(i+1)/2), 2)} " for i in range (IN)]
                print("Los multiplicadores de conversión a valor futuro generados por cada pago son: VF = ",FCF2)
                time.sleep(1)
                print()
                FCF3 = [round(A*(1+r)**(i*(i+1)/2), 2) for i in range (IN)]
                print("Los valores futuros generados por cada pago son: VF = ",FCF3)
                time.sleep(1)
                print()
                j = 0
                for i in FCF3:
                    j += i
                FCF4 = j
                print("El valor futuro de la suma de la serie es: VF = $",round(FCF4, 2))
                time.sleep(1)
            ecuaciónValorFuturoDeSerieConInterésCompuestoConNúmerosConIntervalosDeTiempoDecrecientes()
            print()
    
            def gráficaValorFuturoDeSerieConInterésCompuestoConLiteralesConIntervalosDeTiempoDecrecientes():
                print("SE TRAZA LA GRÁFICA CORRESPONDIENTE A LA SERIE DE LOS FLUJOS DE CAJA")
                print()
                print(27*" ","VF",29*"&",30*"*","FL 0")
                print(60*" ","*")
                for i in range(IN-1):
                    print(60*" ",30*"*","FL",i+1)
                    for j in range(i+2):
                        print(60*" ","*")
                print(60*" ",30*"*","FL",IN)
            gráficaValorFuturoDeSerieConInterésCompuestoConLiteralesConIntervalosDeTiempoDecrecientes()

        elif HO == "VA" and BY == "+" and RE == "C":
            def ecuaciónValorActualDeSerieConInterésCompuestoConLiteralesConIntervalosDeTiempoCrecientes():
                print()
                print("SE ESCRIBE LA SERIE DE PAGOS DE IGUAL VALOR E IGUAL TASA DE INTERÉS CON UN PATRON LINEAL DE AUMENTO EN LOS INTERVALOS ENTRE CADA PAGO")
                time.sleep(1)

                IF = "A*(1+r)"
                FCF1 = [f"{IF}^{-i*(i+1)/2} " for i in range (IN)]
                print()
                print("La serie de flujos de caja es el siguiente: VA = ",FCF1)
                time.sleep(1)
            ecuaciónValorActualDeSerieConInterésCompuestoConLiteralesConIntervalosDeTiempoCrecientes()
            print()

            def tablaValorActualDeSerieConInterésCompuestoConLiteralesConIntervalosDeTiempoCrecientes():
                print("SE IMPRIME LA TABLA DE VALORES\n")
                print("    __________________ ____________________ ____________________________")
                print("   |                  |                    |            |               |")
                print("   |  VALOR PERIÓDICO |   TASA DE INTERÉS  |  MOMENTOS  | VALOR INICIAL |")
                print("   |__________________|____________________|____________|_______________|")
                for i in range(IN):
                    print("   |    $",A,"    |    ",r*100,"% EBV      |   ",i*(i+1)/2,"    |  $",round(A*((1+r) ** (-i*(i+1)/2)), 2)," |")
                    time.sleep(1)
                print("   |__________________|____________________|____________|_______________|")
                time.sleep(1)
            tablaValorActualDeSerieConInterésCompuestoConLiteralesConIntervalosDeTiempoCrecientes()
            print()

            def ecuaciónValorActualDeSerieConInterésCompuestoConNúmerosConIntervalosDeTiempoCrecientes():
                print("SE ESCRIBE LA SERIE DE PAGOS DE IGUAL VALOR E IGUAL TASA DE INTERÉS CON UN PATRON LINEAL DE AUMENTO EN LOS INTERVALOS ENTRE CADA PAGO")
                time.sleep(1)
                print()
                IF = "$2'500.000*(1+0.03)"
                FCF1 = [f"{IF}^{-i*(i+1)/2} " for i in range (IN)]
                print("La serie de flujos de caja es el siguiente: VA = ",FCF1)
                time.sleep(1)
                print()
                IF1 = 1+0.03
                FCF2 = [f"{"$"}{A}*{round(IF1 ** (-i*(i+1)/2), 2)} " for i in range (IN)]
                print("Los multiplicadores de conversión a valor actual generados por cada pago son: VA = ",FCF2)
                time.sleep(1)
                print()
                FCF3 = [round(A*(1+r)**(-i*(i+1)/2), 2) for i in range (IN)]
                print("Los valores actuales generados por cada pago son: VA = ",FCF3)
                time.sleep(1)
                print()
                j = 0
                for i in FCF3:
                    j += i
                FCF4 = j
                print("El valor actual de la suma de la serie es: VA = $",round(FCF4, 2))
                time.sleep(1)
            ecuaciónValorActualDeSerieConInterésCompuestoConNúmerosConIntervalosDeTiempoCrecientes()
            print()
    
            def gráficaValorActualDeSerieConInterésCompuestoConLiteralesConIntervalosDeTiempoCrecientes():
                print("SE TRAZA LA GRÁFICA CORRESPONDIENTE A LA SERIE DE LOS FLUJOS DE CAJA")
                print()
                print(27*" ","FL 0",29*"*",29*"&","VA")
                print(60*" ","*")
                for i in range(IN-1):
                    print(27*" ","FL",i+1,29*"*")
                    for j in range(i+2):
                        print(60*" ","*")
                print(27*" ","FL",IN,29*"*")
            gráficaValorActualDeSerieConInterésCompuestoConLiteralesConIntervalosDeTiempoCrecientes()

        elif HO == "VF" and BY == "+" and RE == "C":
            def ecuaciónValorFuturoDeSerieConInterésCompuestoConLiteralesConIntervalosDeTiempoCrecientes():
                print()
                print("SE ESCRIBE LA SERIE DE PAGOS DE IGUAL VALOR E IGUAL TASA DE INTERÉS CON UN PATRON LINEAL DE AUMENTO EN LOS INTERVALOS ENTRE CADA PAGO")
                time.sleep(1)

                IF = "A*(1+r)"
                FCF1 = [f"{IF}^{-i*(i+1)/2 + (IN-1)*IN/2} " for i in range (-IN, 0)]
                print()
                print("La serie de flujos de caja es el siguiente: VF = ",FCF1)
                time.sleep(1)
            ecuaciónValorFuturoDeSerieConInterésCompuestoConLiteralesConIntervalosDeTiempoCrecientes()
            print()

            def tablaValorFuturoDeSerieConInterésCompuestoConLiteralesConIntervalosDeTiempoCrecientes():
                print("SE IMPRIME LA TABLA DE VALORES\n")
                print("    __________________ ____________________ ____________________________")
                print("   |                  |                    |            |               |")
                print("   |  VALOR PERIÓDICO |   TASA DE INTERÉS  |  MOMENTOS  |  VALOR FINAL  |")
                print("   |__________________|____________________|____________|_______________|")
                for i in range(-IN, 0):
                    print("   |    $",A,"    |    ",r*100,"% EBV      |   ",-i*(i+1)/2 + (IN-1)*IN/2,"    |  $",round(A*((1+r) ** (-i*(i+1)/2 + (IN-1)*IN/2)), 2)," |")
                    time.sleep(1)
                print("   |__________________|____________________|____________|_______________|")
                time.sleep(1)
            tablaValorFuturoDeSerieConInterésCompuestoConLiteralesConIntervalosDeTiempoCrecientes()
            print()

            def ecuaciónValorFuturoDeSerieConInterésCompuestoConNúmerosConIntervalosDeTiempoCrecientes():
                print("SE ESCRIBE LA SERIE DE PAGOS DE IGUAL VALOR E IGUAL TASA DE INTERÉS CON UN PATRON LINEAL DE AUMENTO EN LOS INTERVALOS ENTRE CADA PAGO")
                time.sleep(1)
                print()
                IF = "$2'500.000*(1+0.03)"
                FCF1 = [f"{IF}^{-i*(i+1)/2 + (IN-1)*IN/2} " for i in range (-IN, 0)]
                print("La serie de flujos de caja es el siguiente: VF = ",FCF1)
                time.sleep(1)
                print()
                IF1 = 1+0.03
                FCF2 = [f"{"$"}{A}*{round(IF1 ** (-i*(i+1)/2 + (IN-1)*IN/2), 2)} " for i in range (-IN, 0)]
                print("Los multiplicadores de conversión a valor futuro generados por cada pago son: VF = ",FCF2)
                time.sleep(1)
                print()
                FCF3 = [round(A*(1+r)**(-i*(i+1)/2 + (IN-1)*IN/2), 2) for i in range (-IN, 0)]
                print("Los valores futuros generados por cada pago son: VF = ",FCF3)
                time.sleep(1)
                print()
                j = 0
                for i in FCF3:
                    j += i
                FCF4 = j
                print("El valor futuro de la suma de la serie es: VF = $",round(FCF4, 2))
                time.sleep(1)
            ecuaciónValorFuturoDeSerieConInterésCompuestoConNúmerosConIntervalosDeTiempoCrecientes()
            print()
    
            def gráficaValorFuturoDeSerieConInterésCompuestoConLiteralesConIntervalosDeTiempoCrecientes():
                print("SE TRAZA LA GRÁFICA CORRESPONDIENTE A LA SERIE DE LOS FLUJOS DE CAJA")
                print()
        
                print(60*" ",30*"*","FL 0")
                print(60*" ","*")
                for i in range(IN-1):
                    print(60*" ",30*"*","FL",i+1)
                    for j in range(i+2):
                        print(60*" ","*")
                print(27*" ","VF",29*"&",30*"*","FL",IN)
        
            gráficaValorFuturoDeSerieConInterésCompuestoConLiteralesConIntervalosDeTiempoCrecientes()
    
        elif HO == "VA" and BY == "-" and RE == "C":
            def ecuaciónValorActualDeSerieConInterésCompuestoConLiteralesConIntervalosDeTiempoDecrecientes():
                print()
                print("SE ESCRIBE LA SERIE DE PAGOS DE IGUAL VALOR E IGUAL TASA DE INTERÉS CON UN PATRON LINEAL DE DISMINUCIÓN EN LOS INTERVALOS ENTRE CADA PAGO")
                time.sleep(1)

                IF = "A*(1+r)"
                FCF1 = [f"{IF}^{i*(i+1)/2 - (IN-1)*IN/2} " for i in range (-IN, 0)]
                print()
                print("La serie de flujos de caja es el siguiente: VA = ",FCF1)
                time.sleep(1)
            ecuaciónValorActualDeSerieConInterésCompuestoConLiteralesConIntervalosDeTiempoDecrecientes()
            print()

            def tablaValorActualDeSerieConInterésCompuestoConLiteralesConIntervalosDeTiempoDecrecientes():
                print("SE IMPRIME LA TABLA DE VALORES\n")
                print("    __________________ ____________________ ____________________________")
                print("   |                  |                    |            |               |")
                print("   |  VALOR PERIÓDICO |   TASA DE INTERÉS  |  MOMENTOS  | VALOR INICIAL |")
                print("   |__________________|____________________|____________|_______________|")
                for i in range(-IN, 0):
                    print("   |    $",A,"    |    ",r*100,"% EBV      |   ",-i*(i+1)/2 + (IN-1)*IN/2,"    |  $",round(A*((1+r) ** (i*(i+1)/2 - (IN-1)*IN/2)), 2)," |")
                    time.sleep(1)
                print("   |__________________|____________________|____________|_______________|")
                time.sleep(1)
            tablaValorActualDeSerieConInterésCompuestoConLiteralesConIntervalosDeTiempoDecrecientes()
            print()

            def ecuaciónValorActualDeSerieConInterésCompuestoConNúmerosConIntervalosDeTiempoDecrecientes():
                print("SE ESCRIBE LA SERIE DE PAGOS DE IGUAL VALOR E IGUAL TASA DE INTERÉS CON UN PATRON LINEAL DE DISMINUCIÓN EN LOS INTERVALOS ENTRE CADA PAGO")
                time.sleep(1)
                print()
                IF = "$2'500.000*(1+0.03)"
                FCF1 = [f"{IF}^{i*(i+1)/2 - (IN-1)*IN/2} " for i in range (-IN, 0)]
                print("La serie de flujos de caja es el siguiente: VA = ",FCF1)
                time.sleep(1)
                print()
                IF1 = 1+0.03
                FCF2 = [f"{"$"}{A}*{round(IF1 ** (i*(i+1)/2 - (IN-1)*IN/2), 2)} " for i in range (-IN, 0)]
                print("Los multiplicadores de conversión a valor actual generados por cada pago son: VA = ",FCF2)
                time.sleep(1)
                print()
                FCF3 = [round(A*(1+r)**(i*(i+1)/2 - (IN-1)*IN/2), 2) for i in range (-IN, 0)]
                print("Los valores actuales generados por cada pago son: VA = ",FCF3)
                time.sleep(1)
                print()
                j = 0
                for i in FCF3:
                    j += i
                FCF4 = j
                print("El valor actual de la suma de la serie es: VA = $",round(FCF4, 2))
                time.sleep(1)
            ecuaciónValorActualDeSerieConInterésCompuestoConNúmerosConIntervalosDeTiempoDecrecientes()
            print()
    
            def gráficaValorActualDeSerieConInterésCompuestoConLiteralesConIntervalosDeTiempoDecrecientes():
                print("SE TRAZA LA GRÁFICA CORRESPONDIENTE A LA SERIE DE LOS FLUJOS DE CAJA")
                print()
                print(27*" ","FL 0",29*"*")
                print(60*" ","*")
                for i in range(IN-1):
                    print(27*" ","FL",i+1,29*"*")
                    for j in range(i+2):
                        print(60*" ","*")
                print(27*" ","FL",IN,29*"*",29*"&","VA")

            gráficaValorActualDeSerieConInterésCompuestoConLiteralesConIntervalosDeTiempoDecrecientes()

        elif HO == "VF" and BY == "-" and RE == "S":
            def ecuaciónValorFuturoDeSerieConInterésSimpleConLiteralesConIntervalosDeTiempoDecrecientes():
                print()
                print("SE ESCRIBE LA SERIE DE PAGOS DE IGUAL VALOR E IGUAL TASA DE INTERÉS CON UN PATRON LINEAL DE DISMINUCIÓN EN LOS INTERVALOS ENTRE CADA PAGO")
                time.sleep(1)

                FCF1 = [f"{"A*(1+r*"}{i*(i+1)/2}{")"} " for i in range (IN)]
                print()
                print("La serie de flujos de caja es el siguiente: VF = ",FCF1)
                time.sleep(1)
            ecuaciónValorFuturoDeSerieConInterésSimpleConLiteralesConIntervalosDeTiempoDecrecientes()
            print()

            def tablaValorFuturoDeSerieConInterésSimpleConLiteralesConIntervalosDeTiempoDecrecientes():
                print("SE IMPRIME LA TABLA DE VALORES\n")
                print("    __________________ ____________________ ____________________________")
                print("   |                  |                    |            |               |")
                print("   |  VALOR PERIÓDICO |   TASA DE INTERÉS  |  MOMENTOS  |  VALOR FINAL  |")
                print("   |__________________|____________________|____________|_______________|")
                for i in range(IN):
                    print("   |    $",A,"    |    ",r*100,"% EBV      |   ",i*(i+1)/2,"    |  $",round(A*(1+r*(i*(i+1)/2)), 2)," |")
                    time.sleep(1)
                print("   |__________________|____________________|____________|_______________|")
                time.sleep(1)
            tablaValorFuturoDeSerieConInterésSimpleConLiteralesConIntervalosDeTiempoDecrecientes()
            print()

            def ecuaciónValorFuturoDeSerieConInterésSimpleConNúmerosConIntervalosDeTiempoDecrecientes():
                print("SE ESCRIBE LA SERIE DE PAGOS DE IGUAL VALOR E IGUAL TASA DE INTERÉS CON UN PATRON LINEAL DE DISMINUCIÓN EN LOS INTERVALOS ENTRE CADA PAGO")
                time.sleep(1)
                print()
                FCF1 = [f"{"2500000*(1+0,03*"}{i*(i+1)/2}{")"} " for i in range (IN)]
                print("La serie de flujos de caja es el siguiente: VF = ",FCF1)
                time.sleep(1)
                print()
                FCF2 = [f"{"$"}{A}*{round((1+0.03*(i*(i+1)/2)), 2)} " for i in range (IN)]
                print("Los multiplicadores de conversión a valor futuro generados por cada pago son: VF = ",FCF2)
                time.sleep(1)
                print()
                FCF3 = [round(A*(1+r*(i*(i+1)/2)), 2) for i in range (IN)]
                print("Los valores futuros generados por cada pago son: VF = ",FCF3)
                time.sleep(1)
                print()
                j = 0
                for i in FCF3:
                    j += i
                FCF4 = j
                print("El valor futuro de la suma de la serie es: VF = $",round(FCF4, 2))
                time.sleep(1)
            ecuaciónValorFuturoDeSerieConInterésSimpleConNúmerosConIntervalosDeTiempoDecrecientes()
            print()
    
            def gráficaValorFuturoDeSerieConInterésSimpleConLiteralesConIntervalosDeTiempoDecrecientes():
                print("SE TRAZA LA GRÁFICA CORRESPONDIENTE A LA SERIE DE LOS FLUJOS DE CAJA")
                print()
                print(27*" ","VF",29*"&",30*"*","FK 0")
                print(60*" ","*")
                for i in range(IN-1):
                    print(60*" ",30*"*","FK",i+1)
                    for j in range(i+2):
                        print(60*" ","*")
                print(60*" ",30*"*","FK",IN)
            gráficaValorFuturoDeSerieConInterésSimpleConLiteralesConIntervalosDeTiempoDecrecientes()

        elif HO == "VA" and BY == "+" and RE == "S":
            def ecuaciónValorActualDeSerieConInterésSimpleConLiteralesConIntervalosDeTiempoCrecientes():
                print()
                print("SE ESCRIBE LA SERIE DE PAGOS DE IGUAL VALOR E IGUAL TASA DE INTERÉS CON UN PATRON LINEAL DE AUMENTO EN LOS INTERVALOS ENTRE CADA PAGO")
                time.sleep(1)

                FCF1 = [f"{"A/(1+r*"}{i*(i+1)/2}{")"} " for i in range (IN)]
                print()
                print("La serie de flujos de caja es el siguiente: VF = ",FCF1)
                time.sleep(1)
            ecuaciónValorActualDeSerieConInterésSimpleConLiteralesConIntervalosDeTiempoCrecientes()
            print()

            def tablaValorActualDeSerieConInterésSimpleConLiteralesConIntervalosDeTiempoCrecientes():
                print("SE IMPRIME LA TABLA DE VALORES\n")
                print("    __________________ ____________________ ____________________________")
                print("   |                  |                    |            |               |")
                print("   |  VALOR PERIÓDICO |   TASA DE INTERÉS  |  MOMENTOS  |  VALOR FINAL  |")
                print("   |__________________|____________________|____________|_______________|")
                for i in range(IN):
                    print("   |    $",A,"    |    ",r*100,"% EBV      |   ",i*(i+1)/2,"    |  $",round(A/(1+r*(i*(i+1)/2)), 2)," |")
                    time.sleep(1)
                print("   |__________________|____________________|____________|_______________|")
                time.sleep(1)
            tablaValorActualDeSerieConInterésSimpleConLiteralesConIntervalosDeTiempoCrecientes()
            print()

            def ecuaciónValorActualDeSerieConInterésSimpleConNúmerosConIntervalosDeTiempoCrecientes():
                print("SE ESCRIBE LA SERIE DE PAGOS DE IGUAL VALOR E IGUAL TASA DE INTERÉS CON UN PATRON LINEAL DE AUMENTO EN LOS INTERVALOS ENTRE CADA PAGO")
                time.sleep(1)
                print()
                FCF1 = [f"{"2500000/(1+0,03*"}{i*(i+1)/2}{")"} " for i in range (IN)]
                print("La serie de flujos de caja es el siguiente: VF = ",FCF1)
                time.sleep(1)
                print()
                FCF2 = [f"{"$"}{A}/{round((1+0.03*(i*(i+1)/2)), 2)} " for i in range (IN)]
                print("Los divisores de conversión a valor presente generados por cada pago son: VF = ",FCF2)
                time.sleep(1)
                print()
                FCF3 = [round(A/(1+r*(i*(i+1)/2)), 2) for i in range (IN)]
                print("Los valores presentes generados por cada pago son: VF = ",FCF3)
                time.sleep(1)
                print()
                j = 0
                for i in FCF3:
                    j += i
                FCF4 = j
                print("El valor presente de la suma de la serie es: VF = $",round(FCF4, 2))
                time.sleep(1)
            ecuaciónValorActualDeSerieConInterésSimpleConNúmerosConIntervalosDeTiempoCrecientes()
            print()
    
            def gráficaValorActualDeSerieConInterésSimpleConLiteralesConIntervalosDeTiempoCrecientes():
                print("SE TRAZA LA GRÁFICA CORRESPONDIENTE A LA SERIE DE LOS FLUJOS DE CAJA")
                print()
                print(27*" ","FK 0",29*"*",29*"&","VA")
                print(60*" ","*")
                for i in range(IN-1):
                    print(27*" ","FK",i+1,29*"*")
                    for j in range(i+2):
                        print(60*" ","*")
                print(27*" ","FK",IN,29*"*")
            gráficaValorActualDeSerieConInterésSimpleConLiteralesConIntervalosDeTiempoCrecientes()
    
        elif HO == "VF" and BY == "+" and RE == "S":
            def ecuaciónValorFuturoDeSerieConInterésSimpleConLiteralesConIntervalosDeTiempoCrecientes():
                print()
                print("SE ESCRIBE LA SERIE DE PAGOS DE IGUAL VALOR E IGUAL TASA DE INTERÉS CON UN PATRON LINEAL DE AUMENTO EN LOS INTERVALOS ENTRE CADA PAGO")
                time.sleep(1)

                FCF1 = [f"{"A*(1+r*"}{-i*(i+1)/2 + (IN-1)*IN/2}{")"} " for i in range (-IN, 0)]
                print()
                print("La serie de flujos de caja es el siguiente: VF = ",FCF1)
                time.sleep(1)
            ecuaciónValorFuturoDeSerieConInterésSimpleConLiteralesConIntervalosDeTiempoCrecientes()
            print()

            def tablaValorFuturoDeSerieConInterésSimpleConLiteralesConIntervalosDeTiempoCrecientes():
                print("SE IMPRIME LA TABLA DE VALORES\n")
                print("    __________________ ____________________ ____________________________")
                print("   |                  |                    |            |               |")
                print("   |  VALOR PERIÓDICO |   TASA DE INTERÉS  |  MOMENTOS  |  VALOR FINAL  |")
                print("   |__________________|____________________|____________|_______________|")
                for i in range(-IN, 0):
                    print("   |    $",A,"    |    ",r*100,"% EBV      |   ",-i*(i+1)/2 + (IN-1)*IN/2,"    |  $",round(A*(1+r*(-i*(i+1)/2 + (IN-1)*IN/2)), 2)," |")
                    time.sleep(1)
                print("   |__________________|____________________|____________|_______________|")
                time.sleep(1)
            tablaValorFuturoDeSerieConInterésSimpleConLiteralesConIntervalosDeTiempoCrecientes()
            print()

            def ecuaciónValorFuturoDeSerieConInterésSimpleConNúmerosConIntervalosDeTiempoCrecientes():
                print("SE ESCRIBE LA SERIE DE PAGOS DE IGUAL VALOR E IGUAL TASA DE INTERÉS CON UN PATRON LINEAL DE AUMENTO EN LOS INTERVALOS ENTRE CADA PAGO")
                time.sleep(1)
                print()
                FCF1 = [f"{"2500000*(1+0,03*"}{-i*(i+1)/2 + (IN-1)*IN/2}{")"} " for i in range (-IN, 0)]
                print("La serie de flujos de caja es el siguiente: VF = ",FCF1)
                time.sleep(1)
                print()
                FCF2 = [f"{"$"}{A}*{round((1+0.03*(-i*(i+1)/2 + (IN-1)*IN/2)), 2)} " for i in range (-IN, 0)]
                print("Los multiplicadores de conversión a valor futuro generados por cada pago son: VF = ",FCF2)
                time.sleep(1)
                print()
                FCF3 = [round(A*(1+r*(-i*(i+1)/2 + (IN-1)*IN/2)), 2) for i in range (-IN, 0)]
                print("Los valores futuros generados por cada pago son: VF = ",FCF3)
                time.sleep(1)
                print()
                j = 0
                for i in FCF3:
                    j += i
                FCF4 = j
                print("El valor futuro de la suma de la serie es: VF = $",round(FCF4, 2))
                time.sleep(1)
            ecuaciónValorFuturoDeSerieConInterésSimpleConNúmerosConIntervalosDeTiempoCrecientes()
            print()
    
            def gráficaValorFuturoDeSerieConInterésSimpleConLiteralesConIntervalosDeTiempoCrecientes():
                print("SE TRAZA LA GRÁFICA CORRESPONDIENTE A LA SERIE DE LOS FLUJOS DE CAJA")
                print()
        
                print(60*" ",30*"*","FK 0")
                print(60*" ","*")
                for i in range(IN-1):
                    print(60*" ",30*"*","FK",i+1)
                    for j in range(i+2):
                        print(60*" ","*")
                print(27*" ","VF",29*"&",30*"*","FK",IN)
            gráficaValorFuturoDeSerieConInterésSimpleConLiteralesConIntervalosDeTiempoCrecientes()

        elif HO == "VA" and BY == "-" and RE == "S":
            def ecuaciónValorActualDeSerieConInterésSimpleConLiteralesConIntervalosDeTiempoDecrecientes():
                print()
                print("SE ESCRIBE LA SERIE DE PAGOS DE IGUAL VALOR E IGUAL TASA DE INTERÉS CON UN PATRON LINEAL DE DISMINUCIÓN EN LOS INTERVALOS ENTRE CADA PAGO")
                time.sleep(1)

                FCF1 = [f"{"A/(1+r*"}{-i*(i+1)/2 + (IN-1)*IN/2}{")"} " for i in range (-IN, 0)]
                print()
                print("La serie de flujos de caja es el siguiente: VF = ",FCF1)
                time.sleep(1)
            ecuaciónValorActualDeSerieConInterésSimpleConLiteralesConIntervalosDeTiempoDecrecientes()
            print()

            def tablaValorActualDeSerieConInterésSimpleConLiteralesConIntervalosDeTiempoDecrecientes():
                print("SE IMPRIME LA TABLA DE VALORES\n")
                print("    __________________ ____________________ ____________________________")
                print("   |                  |                    |            |               |")
                print("   |  VALOR PERIÓDICO |   TASA DE INTERÉS  |  MOMENTOS  |  VALOR FINAL  |")
                print("   |__________________|____________________|____________|_______________|")
                for i in range(-IN, 0):
                    print("   |    $",A,"    |    ",r*100,"% EBV      |   ",-i*(i+1)/2 + (IN-1)*IN/2,"    |  $",round(A/(1+r*(-i*(i+1)/2 + (IN-1)*IN/2)), 2)," |")
                    time.sleep(1)
                print("   |__________________|____________________|____________|_______________|")
                time.sleep(1)
            tablaValorActualDeSerieConInterésSimpleConLiteralesConIntervalosDeTiempoDecrecientes()
            print()

            def ecuaciónValorActualDeSerieConInterésSimpleConNúmerosConIntervalosDeTiempoDecrecientes():
                print("SE ESCRIBE LA SERIE DE PAGOS DE IGUAL VALOR E IGUAL TASA DE INTERÉS CON UN PATRON LINEAL DE DISMINUCIÓN EN LOS INTERVALOS ENTRE CADA PAGO")
                time.sleep(1)
                print()
                FCF1 = [f"{"2500000/(1+0,03*"}{-i*(i+1)/2 + (IN-1)*IN/2}{")"} " for i in range (-IN, 0)]
                print("La serie de flujos de caja es el siguiente: VF = ",FCF1)
                time.sleep(1)
                print()
                FCF2 = [f"{"$"}{A}/{round((1+0.03*(-i*(i+1)/2 + (IN-1)*IN/2)), 2)} " for i in range (-IN, 0)]
                print("Los divisores de conversión a valor presente generados por cada pago son: VF = ",FCF2)
                time.sleep(1)
                print()
                FCF3 = [round(A/(1+r*(-i*(i+1)/2 + (IN-1)*IN/2)), 2) for i in range (-IN, 0)]
                print("Los valores presentes generados por cada pago son: VF = ",FCF3)
                time.sleep(1)
                print()
                j = 0
                for i in FCF3:
                    j += i
                FCF4 = j
                print("El valor presente de la suma de la serie es: VF = $",round(FCF4, 2))
                time.sleep(1)
            ecuaciónValorActualDeSerieConInterésSimpleConNúmerosConIntervalosDeTiempoDecrecientes()
            print()
    
            def gráficaValorActualDeSerieConInterésSimpleConLiteralesConIntervalosDeTiempoDecrecientes():
                print("SE TRAZA LA GRÁFICA CORRESPONDIENTE A LA SERIE DE LOS FLUJOS DE CAJA")
                print()
                print(27*" ","FK 0",29*"*")
                print(60*" ","*")
                for i in range(IN-1):
                    print(27*" ","FK",i+1,29*"*")
                    for j in range(i+2):
                        print(60*" ","*")
                print(27*" ","FK",IN,29*"*",29*"&","VA")
            gráficaValorActualDeSerieConInterésSimpleConLiteralesConIntervalosDeTiempoDecrecientes()
        else:
            print("No podemos ejecutar nada")
    else:
        print("Cantidad no permitida")
except:
    print("!Por favor, ingresa solamente un número!")

