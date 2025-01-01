"""
URL configuration for GYM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GymFit - Transform Your Body</title>
    <link rel="stylesheet" href="styles.css">
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
            color: #333;
        }
        header {
            background: url('gym-background.jpg') no-repeat center center/cover;
            color: white;
            text-align: center;
            padding: 100px 20px;
        }
        header h1 {
            font-size: 3em;
            margin: 0;
        }
        header p {
            font-size: 1.5em;
            margin: 10px 0;
        }
        .cta-button {
            background-color: #ff5733;
            color: white;
            padding: 15px 30px;
            text-decoration: none;
            border-radius: 5px;
            font-size: 1.2em;
            margin-top: 20px;
            display: inline-block;
        }
        .cta-button:hover {
            background-color: #e04e2c;
        }
        .features {
            display: flex;
            justify-content: space-around;
            padding: 50px 20px;
            background-color: #fff;
        }
        .feature {
            text-align: center;
            max-width: 300px;
        }
        .feature img {
            width: 100px;
            margin-bottom: 20px;
        }
        .contact {
            text-align: center;
            padding: 50px 20px;
            background-color: #333;
            color: white;
        }
        .contact a {
            color: #ff5733;
            text-decoration: none;
        }
    </style>
</head>
<body>
    <header>
        <h1>Welcome to GymFit</h1>
        <p>Your Journey to Fitness Starts Here</p>
        <a href="#services" class="cta-button">Join Now</a>
    </header>

    <section class="features">
        <div class="feature">
            <img src="personal-training.png" alt="Personal Training">
            <h3>Personal Training</h3>
            <p>Get customized workout plans from expert trainers.</p>
        </div>
        <div class="feature">
            <img src="group-classes.png" alt="Group Classes">
            <h3>Group Classes</h3>
            <p>Stay motivated with dynamic group sessions.</p>
        </div>
        <div class="feature">
            <img src="modern-equipment.png" alt="Modern Equipment">
            <h3>Modern Equipment</h3>
            <p>Train with the latest fitness machines and tools.</p>
        </div>
    </section>

    <section class="contact">
        <h2>Contact Us</h2>
        <p>Location: 123 Fitness Ave, Wellness City</p>
        <p>Email: <a href="mailto:info@gymfit.com">info@gymfit.com</a></p>
        <p>Phone: <a href="tel:+1234567890">+123 456 7890</a></p>
    </section>
</body>
</html>

    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include("HOME.urls"))
]
