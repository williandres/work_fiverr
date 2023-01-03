# Prueba de analista de datos
##### _Solucion_

Este repositorio contiene el desarrollo de la prueba de analista de datos. Con los datos otorgados, se evidencio que en ciertos casos los vehículos estan con registros en Cero, y en otros días no aparecen algunos de los vehiculos que en otros días si estan registrados. Por tal motivo, oriente el analisis en la fiabilidad y la certeza del funcionamiento de la telemetria en la flota.

Se analiza qué vehiculos se encuentran registrados en los datos y posterior se define el comportamiento de los datos día tras dia, se genera un archivo donde se almacena esa definicion, que esta comprendido por 4 estados.

- Sin registro: _Vehiculos que no aparecen en ese día con registros_
- Sin datos: _Vehiculos que si aparecen en ese día pero con registros en cero_
- Datos irregulares: _Vehiculos con intermitencia en valores entre 0 y distinto a 0_
- Dato correcto: _Vehiculos con mas del 90% de registros distintos a 0

Posterior a ello se realiza dashboard en la herramienta PowerBI, para poder visualizar y monitorear el comportamiento.

El diseño realizado permite analizar iterativamente la alimentación de mas datos para continuar a lo largo del tiempo el monitoreo.