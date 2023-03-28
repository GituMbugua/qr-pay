<div>
  <h3 align="center"> QR Pay </h3>

  <p align="center">
    A cashless payment system using QR codes and mobile money.
    <br />
  </p>
  <p align="center">
    Completed: December 2021
    <br />
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
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->

## About The Project

This project is a cashless payment system intended for public transport in Kenya. It is implemented using Django, Python and SQLite. 
QR Pay is managed by an admin who creates and posts QR codes with information such as routes and prices. When the QR code is scanned on
a mobile phone, it triggers an STK push notification which requests the customer's Mpesa password, thus completing the payment.

### Built With

* Django
* SQLite


<!-- GETTING STARTED -->
## Getting Started

To get this app running on your machine, simply clone the repository and ensure the following prerequisites are all installed.

### Prerequisites

Have the following prerequisites:
* Python (version 3.90)
* Pip (latest version)
* Django (version 3.2.9)
* Bootstrap 4

### Installation

1. Clone the repository
   ```
   git clone https://github.com/GituMbugua/qr-pay.git
   ```
2. Create a virtual environment

3. Install requirements
    ```
    (venv)$ pip install requirements.txt
    ```
4. Get your API key from the [Safaricom developer portal](https://developer.safaricom.co.ke/APIs)

5. Add your keys and secrets to a .env file
    ```
    CONSUMER_KEY=<consumer_key>
    CONSUMER_SECRET=<consumer_secret>
    PASSKEY=<passkey>
    ```
    
4. Run the server
    ```
    (venv)$ python manage.py runserver
    ```
   

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.


<!-- CONTACT -->
## Contact

Gitu Mbugua - gmbugua38@gmail.com

Project Link: [https://github.com/GituMbugua/qr-pay](https://github.com/GituMbugua/qr-pay)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
