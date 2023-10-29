titulo='****Tienda de Ordenadores****'
opciones='1.Ver Ratones\n2.Ver Teclados\n3.Ver Pantallas\n4.Ver Cascos\n5.Ver Microfonos\n6.Salir'
elegir='Elige una opcion: '
opciones2='1.Razer Cobra Pro inalámbrico\n2.Logitech G203 LIGHTSYNC alámbrico\n3.Pulsar Gaming Gears Xlite V2\n4.SteelSeries Rival 3\n5.CORSAIR M65 Pro RGB\n6.Volver atras'
opciones3='1.HyperX Alloy Origins\n2.Razer BlackWidow V4 Pro\n3.Patriot Memory Viper V765\n4.Roccat Vulcan II Max\n5.SteelSeries Apex Pro TKL Wireless\n6.Volver atras'
opciones4='1.Viewsonic VX Series VX2468-PC-MHD 24 LED FullHD 165Hz\n2.LG UltraGear 27GN800-B 27 LED IPS QuadHD 144Hz FreeSync\n3.Gigabyte M32UC\n4.Asus TUF Gaming VG289Q\n5.Samsung Odyssey OLED G9\n6.Volver atras'
opciones5='1.HyperX Cloud Stinger\n2.Corsair HS50 Pro Stereo\n3.HyperX Cloud Alpha\n4.Razer Kraken Tournament Edition\n5.Logitech G Pro X\n6.Volver atras'
opciones6='1.Blue Yeti X\n2.Elgato Wave:3\n3.Razer Seiren X\n4.HyperX QuadCast S\n5.AUNA MIC-900B\n6.Volver atras'
flag1=True
flag2=True
flag3=True
flag4=True
flag5=True
flag6=True

while flag1:
    print(titulo)
    print(opciones)
    opcion = int(input(elegir))
    if opcion==1:
        flag1= False
        flag2= True
        while flag2:
            print(titulo)
            print(opciones2)
            opcion = int(input(elegir))
            if opcion==1:
                print('Estas en la opcion 1')
            elif opcion==2:
                print('Estas en la opcion 2')
            elif opcion==3:
                print('Estas en la opcion 3')
            elif opcion==4:
                print('Estas en la opcion 4')
            elif opcion==5:
                print('Estas en la opcion 5')
            elif opcion==6:
                flag2= False
                flag1= True
            else:
                print('El valor no sirve')
    elif opcion==2:
        flag1= False
        flag3= True
        while flag3:
            print(titulo)
            print(opciones3)
            opcion = int(input(elegir))
            if opcion==1:
                print('Estas en la opcion 1')
            elif opcion==2:
                print('Estas en la opcion 2')
            elif opcion==3:
                print('Estas en la opcion 3')
            elif opcion==4:
                print('Estas en la opcion 4')
            elif opcion==5:
                print('Estas en la opcion 5')
            elif opcion==6:
                flag3= False
                flag1= True
            else:
                print('El valor no sirve')
    elif opcion==3:
        flag1= False
        flag4= True
        while flag4:
            print(titulo)
            print(opciones4)
            opcion = int(input(elegir))
            if opcion==1:
                print('Estas en la opcion 1')
            elif opcion==2:
                print('Estas en la opcion 2')
            elif opcion==3:
                print('Estas en la opcion 3')
            elif opcion==4:
                print('Estas en la opcion 4')
            elif opcion==5:
                print('Estas en la opcion 5')
            elif opcion==6:
                flag4= False
                flag1= True
            else:
                print('El valor no sirve')
    elif opcion==4:
        flag1= False
        flag5= True
        while flag5:
            print(titulo)
            print(opciones5)
            opcion = int(input(elegir))
            if opcion==1:
                print('Estas en la opcion 1')
            elif opcion==2:
                print('Estas en la opcion 2')
            elif opcion==3:
                print('Estas en la opcion 3')
            elif opcion==4:
                print('Estas en la opcion 4')
            elif opcion==5:
                print('Estas en la opcion 5')
            elif opcion==6:
                flag5= False
                flag1= True
            else:
                print('El valor no sirve')
    elif opcion==5:
        flag1= False
        flag6= True
        while flag6:
            print(titulo)
            print(opciones6)
            opcion = int(input(elegir))
            if opcion==1:
                print('Estas en la opcion 1')
            elif opcion==2:
                print('Estas en la opcion 2')
            elif opcion==3:
                print('Estas en la opcion 3')
            elif opcion==4:
                print('Estas en la opcion 4')
            elif opcion==5:
                print('Estas en la opcion 5')
            elif opcion==6:
                flag6= False
                flag1= True
            else:
                print('El valor no sirve')
    elif opcion==6:
        flag1=False
    else: 
        print('Valor incorrecto')   