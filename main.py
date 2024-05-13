from subprocess import PIPE, Popen
import requests, json, random, sys, os, time, signal, stat


greenColour = '\033[1;32m'
dark_green = '\033[0;32m'
endColour = '\033[39m'
redColour = '\033[1;31m'
dark_red = '\033[0;31m'
blueColour = '\033[1;34m'
yellowColour = '\033[1;33m'
purpleColour = '\033[1;35m'
grayColour = '\033[1;30m'
cyanColour = '\033[1;36m'


symbol = '{}[{}*{}]{}'.format(greenColour, redColour, greenColour, dark_green)
symbolTwo = '{}[{}!{}]{}'.format(greenColour, redColour, greenColour, grayColour)
error = '{}[x]{}'.format(redColour, endColour)


valid = '    {} Valido{}:{}'.format(symbol, redColour, greenColour)
numberTwo = '    {} Numero{}:{}'.format(symbol, redColour, greenColour)
local_format = '    {} Formato local{}:{}'.format(symbol, redColour, greenColour)
international_format = '    {} Formato Internacional{}:{}'.format(symbol, redColour, greenColour)
country_prefix = '    {} Codigo de pais{}:{}'.format(symbol, redColour, greenColour)
country_code = '    {} Nombre de pais abreviado{}:{}'.format(symbol, redColour, greenColour)
country_name = '    {} Nombre de pais{}:{}'.format(symbol, redColour, greenColour)
location = '    {} Localizacion{}:{}'.format(symbol, redColour, greenColour)
carrier = '    {} Operador de telefonia movil{}:{}'.format(symbol, redColour, greenColour)
line_type = '    {} Tipo de linea{}:{}'.format(symbol, redColour, greenColour)


def logo(color):
	logo = """{}
       .o oOOOOOOOo                                            OOOo
       Ob.OOOOOOOo  OOOo.      oOOo.                      .adOOOOOOO
       OboO0000000000000OOo. .oOOOOOo.    OOOo.oOOOOOo...000000000OO
       OOP.oOOOOOOOOOOO "POOOOOOOOOOOo.   `"OOOOOOOOOP,OOOOOOOOOOOB'
       `O'OOOO'     `OOOOo"OOOOOOOOOOO` .adOOOOOOOOO"oOOO'    `OOOOo
       .OOOO'            `OOOOOOOOOOOOOOOOOOOOOOOOOO'            `OO
       OOOOO                 '"OOOOOOOOOOOOOOOO"`                oOO
      oOOOOOba.                .adOOOOOOOOOOba               .adOOOOo.
     oOOOOOOOOOOOOOba.    .adOOOOOOOOOO@^OOOOOOOba.     .adOOOOOOOOOOOO
    OOOOOOOOOOOOOOOOO.OOOOOOOOOOOOOO"`  '"OOOOOOOOOOOOO.OOOOOOOOOOOOOO
    "OOOO"       "YOoOOOOMOIONODOO"`  .   '"OOROAOPOEOOOoOY"    "0OOO"
       Y           'OOOOOOOOOOOOOO: .oOOo. :OOOOOOOOOOO?'         Y
       :            .oO%OOOOOOOOOOo.OOOOOO.oOOOOOOOOOOOO?         :
                    oOOP"%OOOOOOOOoOOOOOOO?oOOOOO?OOOO"OOo
                    '%o  OOOO"%OOOO%"%OOOOO"OOOOOO"OOO':
                         `$"  `OOOO' `O"Y ' `OOOO'  o
                                OP"          : o
{}""".format(color, endColour)

	return logo


def credits():
    print ('{}          __             __           __        __        ___'.format(greenColour))
    print ('         |__) |     /\  /  ` |__/    |__) |__| /  \ |\ | |__')
    print ('         |__) |___ /~~\ \__, |  \    |    |  | \__/ | \| |___ {}v1.0{}'.format(redColour, greenColour))
    print ('    [{}+{}]{}============================================================{}[{}+{}]'.format(redColour, greenColour, redColour, greenColour, redColour, greenColour))
    print ('            Creado por    {}:{} Yovany Morales'.format(redColour, greenColour))
    print ('            Descripcion   {}:{} Obtiene informacion basica de numeros'.format(redColour, greenColour))
    print ('            Recomendacion {}:{} Solo use numeros con el codigo de pais'.format(redColour, greenColour))
    print ('            Nota          {}:{} Puede utiliza ctrl_c + Enter para salir'.format(redColour, greenColour))
    print ('            Contactó      {}:{} yovanymorales.contact@gmail.com'.format(redColour, greenColour))
    print ('            Github        {}:{} https://github.com/yovany-dev'.format(redColour, greenColour))
    print ('    [{}+{}]{}============================================================{}[{}+{}]{}'.format(redColour, greenColour, redColour, greenColour, redColour, greenColour, endColour))


def banner():
    os.system('clear')
    l = logo(redColour)

    for x in l + '\n':
    	sys.stdout.write(x)
    	sys.stdout.flush()
    	time.sleep(0.001)

    for i in range(10):
        os.system('clear')
        time.sleep(0.005)
        print (logo(dark_red))
        credits()
        time.sleep(0.05)

        os.system('clear')
        time.sleep(0.005)
        print (logo(redColour))
        credits()
        time.sleep(0.05)


def signal_handler(signal, frame):
    print('\n{} Saliendo... {}'.format(symbolTwo, endColour))
    time.sleep(1)
    sys.exit()

signal.signal(signal.SIGINT, signal_handler)


def exit():
    print('\n{} Saliendo...{}'.format(symbolTwo, endColour))
    time.sleep(1)
    sys.exit()


def number_symbol(value):
    return '{}[{}{}{}]{}'.format(greenColour, redColour, value, greenColour, grayColour)


def random_useragent():
    with open("user_agents.json", 'r') as agents:
        user_agents = json.load(agents)["agents"]
    return random.choice(user_agents)


def check_connection():
    os.system('clear')
    print('{}Checando conexion a internet...\n'.format(redColour))
    try:
        request = requests.get('https://google.com/')
    except(requests.ConnectionError):
        print('{} Sin conexion a Internet'.format(error))
        exit()


def check_number():
    while True:
        os.system('clear')
        print (logo(redColour))
        print('\n\n    {} {}Puede salir utilizando ctrl_c + Enter'.format(symbolTwo, redColour))
        number = input('\n    {} {}Ingrese un numero telefonico{}: {}'.format(symbol, grayColour, redColour, greenColour)).replace(' ', '')
        try:
            number = int(number)
            return str(number)
        except ValueError:
            pass
 

def validate_apikey(user_apikey):
    test_number = '+573195976586'
    url_apikey = 'http://apilayer.net/api/validate?access_key={}&number={}&country_code=&format=1'.format(user_apikey, test_number)
    user_agent = {'User-Agent': random_useragent()}


    print('\n    {} Checando apikey, por favor espere...'.format(symbolTwo))
    time.sleep(1.5)
    try:
        re = requests.get(url_apikey, headers=user_agent)
        data = json.loads(re.text)
    except:
        print('\n{} Sin conexion a Internet.'.format(error))
        exit()

    try:
        if data['valid'] == True:
            print('\n    {} {}Su apikey es valido. Ya puede ejecutar de nuevo el script.{}'.format(symbol, greenColour, endColour))
            add = open('apikey.txt', 'w')
            add.write(user_apikey)
            add.close()

    except:
        return False


def open_web_browser(url):
    url_search = 'https://www.google.com/search?q={}'.format(url).replace('&', '%26')
    print('\n    {}Abriendo Google Chrome...{}'.format(greenColour, endColour))
    time.sleep(2)

    try:
        process = Popen(['termux-open', url_search])
    except:
        print('\n    {} {}No tiene Google Chrome instalado.{}'.format(error, redColour, endColour))


def telephone_company(data, number):
    print('\n\n    {} Desea saber mas informacion sobre el operador de telefonia del numero?'.format(symbolTwo))
    user = input('\t\tEscriba Y para aceptar, N para salir{}:{} '.format(redColour, greenColour)).upper()
    
    while user != 'Y' and user != 'N':
        information(data, number)
        print('\n\n    {} Desea saber mas informacion sobre el operador de telefonia del numero?'.format(symbolTwo))
        user = input('\t\tEscriba Y para aceptar, N para salir{}:{} '.format(redColour, greenColour)).upper()

    if user == 'Y':
        open_web_browser(data['carrier'])
    
    elif user == 'N':
        exit()


def information(data, number):
    os.system('clear')

    print (logo(redColour))
    print ('')
    print ('    {} {}Esta es la informacion recolectada del numero {}'.format(symbolTwo, greenColour, number))
    print ('')
    print (valid, data['valid'])
    print (numberTwo, data['number'])
    print (local_format, data['local_format'])
    print (international_format, data['international_format'])
    print (country_prefix, data['country_prefix'])
    print (country_name, data['country_name'])
    print (country_code, data['country_code'])
    print (location, data['location'])
    print (carrier, data['carrier'])
    print (line_type, data['line_type'])


def osint():
    number = check_number()

    try:
        apikey = open('apikey.txt', 'r')
        content = apikey.read()
        apikey.close()

    except FileNotFoundError:
        print('\n    {} {}El archivo apikey.txt no existe, se recomienda elegir la opcion 2 o 4 del menu.{}'.format(error, redColour, endColour))
        exit()
    
    url = 'http://apilayer.net/api/validate?access_key={}&number={}&country_code=&format=1'.format(content, number)
    userAgent = {'User-Agent': random_useragent()}


    print('\n\n\t{} {}Recolectando informacion...'.format(symbolTwo, greenColour))
    try:
        r = requests.get(url, headers = userAgent)
        data = json.loads(r.text)
    except:
        print('\n{} Sin conexion a Internet.'.format(error))
        sys.exit()
        
    time.sleep(1.5)
    information(data, number)

    if data['carrier']:
        telephone_company(data, number)
    else:
        print('{}'.format(endColour))


def add_apikey():
    os.system('clear')
    print (logo(greenColour))

    print('\n\n    {} {}Puede salir utilizando ctrl_c + Enter'.format(symbolTwo, redColour))
    user_apikey = input('\n    {} {}Ingrese un apikey valido: {}'.format(symbol, grayColour, redColour))
    
    while validate_apikey(user_apikey) == False:
        os.system('clear')
        print(logo(greenColour))
        print('\n\n    {} {}Apikey no valido, puede salir utilizando ctrl_c + Enter'.format(error, redColour))
        user_apikey = input('\n    {} {}Ingrese un apikey valido: {}'.format(symbol, grayColour, redColour))


def how_work():
    os.system('clear')
    print("""{} {}Como se usa el Script?{}
Para que el Script funcione de forma correcta utilice numeros con su codigo de pais correspondiente
Ejemplo: +52 81 3273 3710""".format(symbol, redColour, dark_green))
    print('\n\n')
    print("""{} {}Como funciona el Script?{}
Este Script funciona atraves de una API gratuita que proporciona la empresa Numverify, esta API solo podra hacer 250 solicitudes a numeros telefonicos, esto quiere decir que solo puede recoletar informacion de 250 numeros y los de mas usuarios pueden agotar la API, mientras mas la utilicen mas se agotara pero no tiene porque procuparse ya que el creador del Script estara checando y agregando APIS nuevas constantemente.""".format(symbol, redColour, dark_green))
    print('\n\n')
    print("""{} {}Como se si la API se agoto?{}
Se dara cuenta cuando el Script deja de recolectar informacion de numeros y mostrara un tipo de mensaje de error.""".format(symbol, redColour, dark_green))
    print('\n\n')
    print("""{} {}Que hago si la API se agota?{}
Simplemente debe elegir la opcion 4 del menu para actualizar el Script, puede que el creador ya haya agregado una API nueva, si no, solo vuelva a intentarlo mas tarde

Tambien puede elegir la opcion 2 del menu para agregar una API esto quiere decir que podra usar el Script para 250 numeros usted solo (a) sin que nadie mas agote la API.""".format(symbol, redColour, dark_green))
    print('\n\n')
    print("""{} {}Donde consigo una API?{}
Las APIS las puede conseguir de forma gratuita en esta pagina: {}https://numverify.com/signup?plan=17{}
Solo debe crearse una cuenta con el plan gratuito y copiar su "Apikey" o "Clave de acceso de la API" en el apartodo de "Upgrade" o "Potenciar" de la pagina web y luego ir a la opcion 2 del Script y agregarla.""".format(symbol, redColour, dark_green, redColour, dark_green))
    print('\n\n')
    print("""{} {}Como se si mi API se esta agotando?{}
Solo tiene que ir al apartado de "API Usage" o "Uso de API" de su cuenta de Numverify y le mostrara cuantas solicitudes lleva haciendo asu API.""".format(symbol, redColour, dark_green))
    print('\n\n')
    print("""{} {}Que pasa cuando actualizo el Script?{}
Cuando actualice el Script la API que estaba se eliminara y el creador del Script agregara una API nueva pero si agrego un API y no quiere que se elimine puede elegirlo desde la misma opcion 4 del menu al momento de actualizar.""".format(symbol, redColour, dark_green))
    print('\n\n')
    print("""{} {}Que hago si actualice el Script y no conserve mi API?{}
Si usted actualizo el programa y no conservo su API simplemente debe ir de nuevo a su cuenta de Numverify y copiar su "Apikey" y agregar de nuevo en la opcion 2 del menu.""".format(symbol, redColour, dark_green))



def update():
    os.system('clear')
    print(logo(redColour))
    print('\n\n    {} {}Actualizando Script, por favor espere...'.format(symbolTwo, greenColour))
    print('\n    \t{}Esto puede demorar dependiendo de su conexion a internet.'.format(grayColour))
    os.chmod('update.sh', stat.S_IRWXU)
    os.system('./update.sh')


def update_and_keep_apikey():
    try:
        apikey_default = open('apikey.txt', 'r')
        copy = apikey_default.read()
        apikey_default.close()
    
    except FileNotFoundError:
        print('\n\n    {} {}El archivo apikey no existe{}'.format(error, redColour, endColour))
        exit()


    apikey_user = open('apikey_user.txt', 'w')
    write = apikey_user.write(copy)
    apikey_user.close()
    print('\n    {} {}Se guardo su API'.format(symbol, greenColour))
    time.sleep(4)
    update()


def check_if_apikey_user_exists():
    try:
        overwrite = open('apikey_user.txt', 'r')
        content = overwrite.read()
        overwrite.close()
        return content

    except FileNotFoundError:
        return False


def overwrite_apikey():
    value = check_if_apikey_user_exists()

    if value == False:
        pass

    else:
        magic = open('apikey.txt', 'w')
        new = magic.write(value)
        magic.close()
        os.system('rm apikey_user.txt')


def update_program():
    while True:
        os.system('clear')
        print(logo(grayColour))
        print('    {} {}Cuidado, Puede salir utilizando ctrl_c + Enter{}'.format(error, redColour, greenColour))
        print('    Al momento de actualizar el Script se eliminara su API')
        print('    Si es que ya lo agrego antes, sino agrego ninguna API')
        print('    Solo elija "N" para continuar. (Sin comillas)')

        print('\n    {} {}Desea conservar su API?'.format(symbolTwo, dark_green))
        preserve_api = input('\t"Y" para aceptar y continuar, "N" para rechazar y continuar{}: {}'.format(redColour, greenColour)).upper()

        if preserve_api == 'Y':
            return update_and_keep_apikey()
        
        elif preserve_api == 'N':
            return update()
        
        else:
            continue


def menu():
    print('')
    print('    {} Obtener informacion de un numero'.format(number_symbol(1)))
    print('    {} Agregar una API'.format(number_symbol(2)))
    print('    {} Como funciona el Script?'.format(number_symbol(3)))
    print('    {} Actualizar el Script'.format(number_symbol(4)))
    print('    {} Salir'.format(number_symbol(5)))
    print('')


def main():
    # check_connection()
    overwrite_apikey()
    banner()
    menu()
    option = input('    {}{} Seleccione una opcion{}: {}'.format(redColour, number_symbol('~'), redColour, greenColour))

    while option != '1' and option != '2' and option != '3' and option != '4' and option != '5':
        os.system('clear')
        print (logo(redColour))
        credits()
        menu()
        option = input('    {}{} Seleccione una opcion{}: {}'.format(redColour, number_symbol('~'), redColour, greenColour))

    if option == '1':
        osint()

    elif option == '2':
        add_apikey()

    elif option == '3':
        how_work()
    
    elif option == '4':
        update_program()
    
    elif option == '5':
        exit()



if __name__ == '__main__':
    main()
