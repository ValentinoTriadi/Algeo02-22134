<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/ValentinoTriadi/Algeo02-22134">
    <img src="img/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">GoMilk</h3>

  <p align="center">
    An Image retrieval website with CONTENT-BASED INFORMATION RETRIEVAL system 
    <br />
    <a href="https://github.com/ValentinoTriadi/Algeo02-22134"><strong>Explore the docs »</strong></a>
    ·
    <a href="https://github.com/ValentinoTriadi/Algeo02-22134/issues">Report Bug</a>
    <br/>
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
        <li><a href="#features">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#Project-Status">Project Status</a></li>
    <li><a href="#Room-for-Improvement">Room for Improvement</a></li>
    <li><a href="#Acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

GoMilk is Image Retrieval System Website with CONTENT-BASED INFORMATION RETRIEVAL system that based on application of vector algebra. This website can search all of the similiar dataset with the image input using a comparison with color or texture.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Next][Next.js]][Next-url]
* [![Tailwind][TailwindCSS]][Tailwind-url]
* [![Python][Python]][Python-url]
* [![FastAPI][FastAPI]][FastAPI-url]
* [![wkhtmltopdf][wkhtmltopdf]][wkhtmltopdf-url]

<br/>

### Features

* Image Retrieval by color similiarity
* Image Retrieval by texture similiarity
* Image Scraping
* Camera
* Export PDF Result
* Cache for better performance

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites
* npm
  ```sh
  npm install npm@latest -g
  ```
* Python Dependencies
  ```sh
  cd src/Frontend/tubes-algeo-02/app/api
  ```
  ```sh
  pip install -r requirement.txt
  ```
* wkhtmltopdf
  <a href= #WKHTMLTOPDF-INSTALLATION>How to Install WKHTMLTOPDF</a>

### Installation
1. Clone the repo
   ```sh
   git clone git@github.com:ValentinoTriadi/Algeo02-22134.git
   ```
2. ```sh
   cd src/Frontend/tubes-algeo-02
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Install Python dependencies
   ```sh
   cd Frontend/tubes-algeo-02/app/api
   ```
   ```sh
   pip install -r requirement.txt
   ```
4. Install WKHTMLTOPDF
  <a href="#WKHTMLTOPDF-INSTALLATION">How to Install WKHTMLTOPDF</a>

<br/>
<br/>

#### WKHTMLTOPDF INSTALLATION
1. Download wkhtmltopdf
  ```sh
  click https://wkhtmltopdf.org/downloads.html
  ```
2. Set Up Environment
  ```sh
  put '{Personal Path}\wkhtmltopdf\bin' in system environment path 
  ```
3. Check its version
  ```sh
  type 'wkhtmltopdf --version' in terminal
  ```
<br/>
<br/>
 
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

1. Run Next
  ```sh
  cd src/Frontend/tubes-algeo-02
  ```
  ```sh
  type 'npm run dev'
  ```
2. Run FastAPI
  ```sh
  cd src/Frontend/tubes-algeo-02/app/api
  ```
  ```sh
  type 'uvicorn main:app --reload'
  ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- PROJECT STATUS -->
## Project Status
Project status: _complete_ 
<br/>
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROOM FOR IMPROVEMENT -->
## Room for Improvement
Room for improvement:
- Improve speed of process using miltiprocessing
- Improve Frontend Responsiveness 
<br/>
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
* [Valentino Chryslie Triadi](https://github.com/ValentinoTriadi)
![LinkedIn](www.linkedin.com/in/valentino-triadi)
* [Atqiya Haydar Lukman](https://github.com/AtqiyaHaydar)
![LinkedIn](www.linkedin.com/in/atqiyahaydar/)
* [Shabrina Maharani](https://github.com/Maharanish)
![LinkedIn](www.linkedin.com/in/atqiyahaydar/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[TailwindCSS]: https://img.shields.io/badge/tailwind-000000?style=for-the-badge&logo=tailwindcss&logoColor=white
[Tailwind-url]: https://tailwindcss.com/
[Python-url]: https://www.python.org/
[Python]: https://img.shields.io/badge/python-000000?style=for-the-badge&logo=python&logoColor=white
[FastAPI-url]: https://fastapi.tiangolo.com/
[FastAPI]: https://img.shields.io/badge/fastapi-000000?style=for-the-badge&logo=fastapi&logoColor=white
[wkhtmltopdf]: https://img.shields.io/badge/wkhtmltopdf-000000?style=for-the-badge&logo=wkhtmltopdf&logoColor=white
[wkhtmltopdf-url]: https://wkhtmltopdf.org/