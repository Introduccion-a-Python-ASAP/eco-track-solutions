<a id="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="#">
    <img src="https://pnghq.com/wp-content/uploads/png-image-of-python-logo-no-text-included-7.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Curso Jóvenes Profesionales UTN
  </h3>

  <p align="center">
    🪴 Propuesta EcoTrack Solutions 🪴
    <br />
    <a href="#"><strong></strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues/new?labels=bug&template=bug-report---.md">Documentación</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues/new?labels=enhancement&template=feature-request---.md">Contacto</a>
  </p>
</div>

<!-- ABOUT THE PROJECT -->

## Acerca del Proyecto

<a href="#">
    <img src="https://i.ibb.co/NsYpBs0/Default-vibrant-logo-for-Eco-Track-Solutions-a-startup-dedicate-2.jpg" alt="Logo" width="100%" height="auto">
</a>


Este repositorio contiene el código del sistema desarrollado para EcoTrack, una startup dedicada a la monitorización ambiental. El sistema está diseñado para procesar y analizar datos de sensores de calidad del aire instalados en una ciudad. Con un total de 500 sensores y un volumen de datos de 1 millón de lecturas diarias, el sistema proporciona informes detallados y visualizaciones de tendencias.

EcoTrack ha desplegado 500 sensores en una ciudad, recolectando datos cada minuto. Estos sensores miden diferentes contaminantes y condiciones climáticas como PM2.5, PM10, NO2, O3, temperatura y humedad. Los datos se reciben en un formato CSV con las siguientes columnas:


<br>

| 🌍 **Campo**       | 🌱 **Descripción**                                     |
|-------------------|------------------------------------------------------|
| 🕒 **timestamp**   | Fecha y hora de la lectura                           |
| 🆔 **sensor_id**   | Identificador único del sensor                       |
| 🌫️ **PM2.5**       | Concentración de partículas finas                    |
| 🌫️ **PM10**        | Concentración de partículas inhalables               |
| 🌁 **NO2**         | Concentración de dióxido de nitrógeno                |
| ☁️ **O3**          | Concentración de ozono                               |
| 🌡️ **temperatura** | Temperatura ambiente en grados Celsius               |
| 💧 **humedad**     | Humedad relativa en porcentaje                       |


<br>


### Ejemplo de una fila de datos:
  ```js
  2024-07-08 14:30:00,ECO-123,15.2,32.7,21.5,48.9,28.5,65
  ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Comenzando

Instrucciones para ejecutar el proyecto

### Requisitos Previos

- Instalar dependencias
  ```sh
  pip install requeriments.txt
  ```

### Ejecutar el Ambiente

1. Activar VENV
   ```sh
   . .venv/bin/activate
   ```
2. Iniciar servidor de Flask
   ```sh
   flask run --debug
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ACCESS  -->
## Accesso

Podes acceder a la aplicacion utilizando el siguient enlace:

* Backend App: http://localhost:5173


<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Stack Tecnológico

 [![Python]][Python-url]
 [![Html]][Html-url]
 [![Flask]][Flask-url]
![PostgreSQL Badge](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=fff&style=for-the-badge)
![Jinja Badge](https://img.shields.io/badge/Jinja-B41717?logo=jinja&logoColor=fff&style=for-the-badge)
![Bootstrap Badge](https://img.shields.io/badge/Bootstrap-7952B3?logo=bootstrap&logoColor=fff&style=for-the-badge)
![Plotly Badge](https://img.shields.io/badge/Plotly-3F4F75?logo=plotly&logoColor=fff&style=for-the-badge)
![pandas Badge](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=fff&style=for-the-badge)


<!-- CONTACT -->
## Contacto

Pantanetti Nazarena - [@nazapantanetti](https://github.com/nazapantanetti/) - nazapantanetti@gmai.com  
[![LinkedIn][linkedin-shield]][linkedin-url]

Santiago dos Santos - [@santidossantos](https://github.com/santidossantos/) - santiiagodossantos@icloud.com  
[![LinkedIn][linkedin-shield]][linkedin-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/santiago-dos-santos/
[product-screenshot]: images/screenshot.png

[Python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/

[Html]: https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white
[Html-url]: https://html5.org/


[Flask]: https://img.shields.io/badge/Flask-000?logo=flask&logoColor=fff&style=for-the-badge
[Flask-url]: https://flask.palletsprojects.com/en/3.0.x/

