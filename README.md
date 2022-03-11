# Trilateración #

Este algoritmo devuelve las coordenadas de un punto P en el espacio, a través de las coordenadas de los puntos C1, C2 y C3 y sus respectivas distancias del punto P.
Este algoritmo se ejecutará a través de una lambda en AWS.

### Cálculo de la trilateración ###

Hay varios algoritmos que resuelven el problema de multilateración de rango verdadero cartesiano 3-D directamente (es decir, en forma cerrada), por ejemplo, Fang. Además, se pueden adoptar algoritmos de forma cerrada desarrollados para multilateración de pseudo rango . El algoritmo de Bancroft (adaptado) emplea vectores, lo que es una ventaja en algunas situaciones.

<div style="text-align:center">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/3D_Trilat_Scenario_2019-0116.jpg/330px-3D_Trilat_Scenario_2019-0116.jpg" />
</div>


Fig. 1 Escenario de multilateración de rango verdadero en 3D. C1, C2 y C3 son centros conocidos de esferas en el plano x,y. P es el punto cuyas coordenadas (x,y,z) se desean en función de sus rangos a C1, C2 y C3.

El algoritmo más simple corresponde a los centros de esfera en la Fig. 1. La figura 'página' es el plano que contiene C1 , C2 y C3 . Si P es un 'punto de interés' (por ejemplo, un vehículo) en{\ estilo de visualización (x, y, z)}(x, y, z), entonces el teorema de Pitágoras produce los rangos de inclinación entre P y los centros de las esferas:

<div style="text-align:center">
    <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/c79d1b3b07b4a53e3567564dd212e76f1146473e" />
</div>

Así, las coordenadas de P son:

<div style="text-align:center">
    <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/715674038798e46a3b424495c8c82a92dfbbd931" />
</div>

[Three Cartesian dimensions, three measured slant ranges](https://en.wikipedia.org/wiki/True-range_multilateration#Three_Cartesian_dimensions,_three_measured_slant_ranges)

### Dockerfile ###

Instala las librerías necesarias para el funcionamiento del modelo y construye la imagen para ser desplegada como una lambda en AWS.

### Proceso de despliegue ###

1. Crear la imagen de docker: 
```
docker build -t quasar-fire-get-position .
```
2. Login a AWS a través de la consola de comandos, la url hace referencia al repositorio de imagenes en AWS (ECR):
```
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin accountNumber.dkr.ecr.us-east-1.amazonaws.com
```
3. Asigna tag a la imagen ya creada:
```
docker tag npl-model:latest accountNumber.dkr.ecr.us-east-1.amazonaws.com/quasar-fire-get-position:latest
```
4. Hacer push de la imagen a ECR:
```
docker push accountNumber.dkr.ecr.us-east-1.amazonaws.com/quasar-fire-get-position:latest
```

Con estos pasos la imagen ya se encuentra en ECR de AWS y está listo para la creación y ejecución de lambdas.