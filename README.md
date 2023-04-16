# SX_to_cointracking

Descripción: Coge el fichero csv que descargamos de Soutxchange y lo adapta para cargarlo en cointracking.

En este version solo funciona son SX y cointracking en español, pero detectará si existen tipos no soportados para poder actualizarlo.

Para utilizarlo, poner el csv de Soutxchange en el mismo directorio que el script y ejecutar

python3 sx_parser.py

Generará un fichero sx_cointracking.csv para subir.

Está probado con mi propio fichero, por lo que si teneis operaciones diferentes de las mias, o en otro idioma, dará un error.

El resultado no tiene ninguna garantía de ser correcto, así que revisad exhaustivamente los resultados antes de usarlos.

----------------------------------------------------------------------------------------------------

Donations welcome:

SCP: 29397f5ac09162c48aeea537c4950d90a6b370899a2c8054a71e82ab4954228bb63e59c56464

----------------------------------------------------------------------------------------------------

v0.1.4

Added fee calculation

v0.1.3

Bug: fees where not added to transactions

v0.1.2

Added detection of not suported transaction types