<!-- Crear una página que emita los datos del usuario -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resultado del formulario</title>
</head>
<body>
    {%block content%}
    <h1>Gracias por rellenar el formulario</h1>
    <p>Tu nombre: {{ name }}</p>
    <p>Tu email: {{ email }}</p>
    <p>Tu direccion: {{ address }}</p>
    <p>Tu fecha: {{ date }}</p>
    
    with open('form.txt', 'a',) as f:
    f.write(#Variable + '\
')
    {%endblock%}
</body>
</html>
