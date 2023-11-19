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

[![Home Page][home-screenshot]](https://github.com/ValentinoTriadi/Algeo02-22134)
[![About][about-screenshot]](https://github.com/ValentinoTriadi/Algeo02-22134)
[![Tools][tools-screenshot]](https://github.com/ValentinoTriadi/Algeo02-22134)

Welcome to GoMilk, where the world of images becomes effortlessly accessible through cutting-edge Content-Based Image Retrieval (CBIR) technology and the application of vector algebra. We are not just a platform; we are your go-to solution for finding visually similar images with precision and speed.

<br/>
<strong>Our Mission</strong>

At GoMilk, we are on a mission to redefine how you interact with images online. Our primary goal is to provide an intuitive and powerful image retrieval system that seamlessly integrates the principles of CBIR, making the search for visually analogous images a breeze.

<br/>
<strong>The Power of CBIR and Vector Algebra</strong>

Imagine a world where finding images is not just about keywords but about the visual essence. GoMilk leverages the robust methodology of CBIR, which allows you to search for images based on their visual content rather than relying solely on textual descriptions. We have incorporated vector algebra to enhance the accuracy and efficiency of our image retrieval process, ensuring you get the most relevant results.

<br/>
<strong>Key Features:</strong>

* Precision Matching : Our advanced CBIR algorithm ensures precise image matching by analyzing visual content, leading to accurate search results.
* Similarity Percentage : GoMilk doesn't just find similar images; it quantifies the similarity, providing you with a percentage match to gauge relevance.
* User-Friendly Interface : Navigating through our website is a delightful experience. Our user-friendly interface makes image retrieval a simple and enjoyable task.
* Visual Display : Results are not just numbers; they are beautifully displayed images, allowing you to visually confirm the relevance of your search.

<br/>
<strong>Why GoMilk?</strong>

* Efficiency : Save time by finding visually similar images quickly and accurately.
* Innovation : We are at the forefront of image retrieval technology, continuously evolving to meet your needs.
* User-Centric Approach : GoMilk is designed with you in mind, ensuring a seamless and enjoyable experience.

Your visual adventure begins here at GoMilk – where every image tells a story, and we're here to help you find it.
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
  ```sh
  npx shadcn-ui@latest init
  ```
* Python Dependencies
  ```sh
  cd src/tubes-algeo-02/app/api
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
   cd src/tubes-algeo-02
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
3. Install NPX shadcn
   ```sh
   npx shadcn-ui@latest init
   ```
   with this following configuration
   ```sh
   Would you like to use TypeScript (recommended)? yes
   Which style would you like to use? › Default
   Which color would you like to use as base color? › Slate
   Where is your global CSS file? › › app/globals.css
   Do you want to use CSS variables for colors? › yes
   Where is your tailwind.config.js located? › tailwind.config.js
   Configure the import alias for components: › @/components
   Configure the import alias for utils: › @/lib/utils
   Are you using React Server Components? › yes
   Write configuration to components.json. Proceed? » (Y/n) yes
   ```
4. Install Python dependencies
   ```sh
   cd src/tubes-algeo-02/app/api
   ```
   <a href="#Virtual-Environment">Create virtual env (optional)</a>
   
   ```sh
   pip install -r requirements.txt
   ```
4. Install WKHTMLTOPDF
  <a href="#WKHTMLTOPDF-INSTALLATION">How to Install WKHTMLTOPDF</a>

<br/>
<br/>

#### Virtual Environment
1. Install virtualenv
   ```sh
   pip install virtualenv
   ```
2. Create venv
   ```sh
   type 'virtualenv venv'
   ```
3. activate venv
   ```sh
   type 'venv/Scripts/activate'
   ```

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
  cd src/tubes-algeo-02
  ```
  ```sh
  type 'npm run dev'
  ```
2. Run FastAPI
  ```sh
  cd src/tubes-algeo-02/app/api
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

[![LinkedIn][linkedin-shield-valen]][linkedin-valen]
* [Atqiya Haydar Lukman](https://github.com/AtqiyaHaydar)

[![LinkedIn][linkedin-shield-qiya]][linkedin-qiya]
* [Shabrina Maharani](https://github.com/Maharanish)

[![LinkedIn][linkedin-shield-maha]][linkedin-maha]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[home-screenshot]: img/Home.png
[tools-screenshot]: img/Tools.png
[about-screenshot]: img/About.png
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
[linkedin-shield-valen]: https://img.shields.io/badge/Linkedin-Valentino%20Triadi-000000?style=for-the-badge&logo=linkedin&logoColor=white
[linkedin-valen]: https://linkedin.com/in/valentino-triadi
[linkedin-shield-qiya]: https://img.shields.io/badge/Linkedin-Atqiya%20Haydar-000000?style=for-the-badge&logo=linkedin&logoColor=white
[linkedin-qiya]: https://linkedin.com/in/atqiyahaydar
[linkedin-shield-maha]: https://img.shields.io/badge/Linkedin-Shabrina%20Maharani-000000?style=for-the-badge&logo=linkedin&logoColor=white
[linkedin-maha]: https://www.linkedin.com/in/shabrina-maharani-671728161/