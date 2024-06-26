# Ex.05 Design a Website for Server Side Processing
## Date: 10/04/24

## AIM:
To design a website to find surface area of a Right Cylinder in server side.

## FORMULA:
Surface Area = 2Πrh + 2Πr<sup>2</sup>
<br>r --> Radius of Right Cylinder
<br>h --> Height of Right Cylinder

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```
math.html

<html>

<head>
    <body align="center">
        <h1>
            <font color="blue"><b>CHANDRAMOHAN S(212221223002)</b></font>
        </h1>
    </body>
    <meta charset='utf-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <title>Surface Area Of Cylinder</title>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
            color: white;
        }

        .edge {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .box {
            background-color: #5c5fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            padding: 20px;
            width: 300px;
        }

        h1 {
            text-align: center;
            color: #333;
        }

        form {
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .formelt {
            margin-bottom: 15px;
        }

        input[type="text"],
        input[type="submit"] {
            width: 100%;
            padding: 8px;
            margin-top: 5px;
            margin-bottom: 10px;
            box-sizing: border-box;
        }

        input[type="submit"] {
            background-color: rgb(175, 83, 76);
            color: white;
            cursor: pointer;
            border: none;
            padding: 10px 20px;
            border-radius: 3px;
        }

        input[type="submit"]:hover {
            background-color: rgba(175, 83, 76,0.8);
        }
    </style>
</head>

<body>
    <div class="edge">
        <div class="box">
            <h1>Surface Area of Cylinder</h1>
            <form method="POST">
                {% csrf_token %}
                <div class="formelt">
                    Radius : <input type="text" name="radius" value="{{r}}"></input>(in m)<br />
                </div>
                <div class="formelt">
                    Height : <input type="text" name="height" value="{{h}}"></input>(in m)<br />
                </div>
                <div class="formelt">
                    <input type="submit" value="Calculate"></input><br />
                </div>
                <div class="formelt">
                     Surface Area : <input type="text" name="area" value="{{area}}"></input>(in m)<br />
                </div>
            </form>
        </div>
    </div>
</body>

</html>

url.py

from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('surfaceareaofcylinder/',views.surfacearea,name="surfaceareaofcylinder"),
    path('',views.surfacearea,name="surfaceareaofcylinderroot")
]    

views.py

from django.shortcuts import render

def surfacearea(request):
    context={}
    context['area'] = "0"
    context['r'] = "0"
    context['h'] = "0"
    if request.method == 'POST':
        print("POST method is used")
        r = request.POST.get('radius','0')
        h = request.POST.get('height','0')
        print('request=',request)
        print('Radius=',r)
        print('Height=',h)
        area = 2*3.14*int(r)*(int(h)+int(r))
        context['area'] = area
        context['r'] = r
        context['h'] = h
        print('Surface Area =',area)
    return render(request,'mathapp/math.html',context)

```
## SERVER SIDE PROCESSING:

![alt text](<exp5/mathapp/templates/mathapp/Screenshot 2024-04-10 084224.png>)


## HOMEPAGE:

![alt text](<exp5/mathapp/templates/mathapp/Screenshot 2024-04-10 084209.png>)



## RESULT:
The program for performing server side processing is completed successfully.
