<!-- PROJECT LOGO -->
<br />
<div align="center">
    <a href="https://nexustest1.azurewebsites.net/api/docs">View Demo</a>
    ·
    <a href="https://github.com/sasierra98/nexos_test/issues">Report Bug</a>
    ·
    <a href="https://github.com/sasierra98/nexos_test/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Local Installation</a></li>
      </ul>
    </li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is an application created in Python 3.9 and Django 4.1.2 whichs use azure cloud to connect an app service, an Azure Database for PostgreSQL flexible servers, and a BlopStorage. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![Django][Django.com]][Django-url]
* [![Postgres][Postgres.com]][Postgres-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

* Python 3.9
* Django 4.1.2
* Postgres 14+

### Local Installation

1. Create enviroment
  * Windows: 
   ```sh
   python -m venv c:\ruta\al\entorno\virtual
   ```
  * Mac OS / Linux
   ```sh
   python -m venv ruta/al/entorno/virtual
   ```
2. Activate enviroment
  * Windows: 
   ```sh
   c:\ruta\al\entorno\virtual\scripts\activate.bat
   ```
  * Mac OS / Linux
   ```sh
   source ruta/al/entorno/virtual/bin/activate
   ```
3. Install requirements
   ```sh
   pip install -r requirements.txt
   ```
3. Make migrations to database
   ```sh
   python manage.py migrate
   ```
4. Run server
   ```sh
   python manage.py runserver
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Jose Andres Sierra Arrieta - joseandresmayo@gmail.com

Project Link: [https://https://github.com/sasierra98/nexos_test](https://github.com/sasierra98/nexos_test)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[product-screenshot]: images/screenshot.png
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[Django.com]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://docs.djangoproject.com/en/4.1/
[Postgres.com]: https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white
[Postgres-url]: https://www.postgresql.org/
