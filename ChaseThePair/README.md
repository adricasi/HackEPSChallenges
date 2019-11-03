# Chase The Pair

## Importante

Una vez completado el reto debe actualizar el campo de su perfil de usuario de la HackEPS con el link a su repositorio. No se tendrán en cuenta todos aquellos repositorios que no sean presentados como link en el perfil de usuario de la hackEPS2019.

## Descripción

Dado un número (número A) obtén el par de números más cercano (número B y número C) provenientes de dos sets formados por números aleatorios. Cuando existen dos números provinientes de un mismo set que se encuentran a la misma distancia del resultado puede devolver cualquiera de los dos. 

## Ejemplo
Dados dos sets de valores numericos (SetA y SetB)

    SetA: [1,23,45,66,84,113,145,178,205,210,221,250,264,300]
    SetB: [5,31,40,52,73,103,126,162,195,214,225,241,256,267]

Dado un valor numérico aleatorio (toChase) contenido dentro de los dos sets (No tiene porqué existir dentro de estos)

    toChase: 231
    WHERE toChase >= min(SetA, SetB) && toChase <= max(SetA, SetB)

Encontrar aquella pareja de valores numéricos más cercanos a _toChase_ (dónde cada valor de esta pareja pertenece a un Set distinto)

    Result: [221, 225]
    
En este caso podemos apreciar como ```221``` pertenece al SetA y ```225``` pertenece al SetB.

### Notas
- Los sets A y B pueden considerarse de la misma longitud.
- Si dos valores dentro de un mismo set se encuentran a la misma distancia de _toChase_, cualquiera de los dos es perfectamente valido como resultado.
- En caso de encontrar el valor _toChase_ dentro del set, este es un resultado perfectamente valido.
- Debe usarse el generador de sets que ofrecemos en este mísmo repositorio:
  
        ChaseThePair/resources/setsGenerator

- El tiempo de lectura del archivo se puede obviar del total transcurrido.
- Se pueden usar algoritmos de _sort_ para ordenar los datos y sacarles partido para llegar a una solución más optima [pista].
- Teniendo en cuenta los anteriores puntos notificados, todas las técnicas de programación (legales) están permitidas si con ellas conseguís un mejor tiempo.

## Recursos
El reto aporta un generador de sets además de una aplicación funcional que ejecuta la versión más costosa del algoritmo (a modo de guía para saber el estado de vuestro algoritmo). 

Cualquier duda, ejecute el generador o la aplicación con el flag "--info".

Se recomienda ejecutar los progrmas en entornos linux. En caso de suponer un problema, recomendamos el uso de [Git for Windows](https://gitforwindows.org/). No solo será util para este reto sinó también de cara a la Hackathon.

    # Example application
    ./example

    # Sets Generator
    ./setsGenerator

Se ha añadido una amplia variedad de ejecutables para satisfacer las necesidades de tantos equipos como sea posible. Tened en cuenta que todos ellos se encuentran en el apartado [Release](https://github.com/LleidaHack/HackEPSChallenges/releases) de este mísmo repositorio.

Recordad proveer el archivo de permisos de ejecución si usáis un sistema operativo como Linux, mediante:

``` $bash
chmod +x archivo
```

## Plantilla README
Este reto incluye una plantilla para poder usarla como README en vuestro proyecto. Esta incluye información básica para poderos identificar como participantes de la HackEPS.

    ChaseThePair/resources/template.md

## Información

- Group name: HackaNoobs

- Cost:

- Time expend:

- Sets size:
