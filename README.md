# PRIMERA PARTE:
Objetivo

  El objetivo fundamental del proyecto es la realización de una página web alojada en una plataforma como servicio (PaaS)  y creada con el web framework python Flask, que utilizando algún servicio web proporcione una funcionalidad original.
  
  Sería muy interesante que buscaras una API (o APIs) de algún tema que te interese, para que te resulte más atractivo realizar la práctica. Al entender más del tema será más fácil entender la documentación y utilizar las distintas funciones que te ofrece.

Proceso
  
  Estudio y búsqueda de uno o varios servicios web (API Restful). Si se va a escoger una sola API se recomienda que la autentificación sea con key, si escoges dos API, una de ella puede ser sin autentificación.

Entrega

En redmine entrega los siguientes puntos:

    La/s URL/s de la docuementación del servicio web (o servicios) que vais a utilizar.
    La ejecución y salida de 3 peticiones a la API principal (si eliges dos API, solo a una de ella) utilizando curl. Estas peticiones se harán sobre URL con parámetros.
    3 programas python que muestren información de las consultas a la API (se pueden usar las mismas consultas que has utilizado en el punto anterior) utilizando la librería requests. 
    Una descripción de lo que va a hacer tu aplicación web utilizando estos servicios web.

# SEGUNDA PARTE:

El alumno decide que es lo que va a hacer la aplicación web, decide cuantas páginas va a tener, pero las características mínimas de la aplicación web que debes hacer serán las siguientes:

    La aplicación web debe tener una vista tipo lista, donde se vea una lista de recursos de la API.
    Debe tener también una vista detalle, donde se vea información concreta de algún recurso de la API.
    Debe tener al menos un formulario para filtrar la información que se muestra.
    La aplicación web debe tener hoja de estilo.
    La aplicación web debe estar desplegada en una plataforma como servicio (PaaS).

Posibles mejoras

    Utilizar más de una API. Combinar en vuestra aplicación información de varias APIS. O utilizar una API y más información que tengáis en algún fichero JSON.
    Añadir más elementos de los que se indican en el punto anterior: añadir más páginas, añadir más formularios, mostrar la información de alguna otra manera,…
    Utilizar alguna petición POST que permita cambiar el estado de la aplicación web y modifique su información. (Esta mejora se podrá realizar si la API escogida no lo permite, normalmente con API restful con key no suelen tener opción a modificar con peticiones del tipo POST).

¿Qué hay que entregar?

    ¿Qué mejoras crees que has añadido a tu aplicación?
    La URL del repositorio git
    La URL de la página desplegada en una plataforma como servicio
    Un pdf donde se explique y muestre el correcto funcionamiento de la aplicación
