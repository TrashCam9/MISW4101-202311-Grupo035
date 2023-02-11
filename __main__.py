import sys
from src.vista.InterfazCajaSeguridad import App_CajaDeSeguridad
from src.logica.LogicaMock import LogicaMock

if __name__ == '__main__':
    # Punto inicial de la aplicación

    logica = LogicaMock()

    app = App_CajaDeSeguridad(sys.argv, logica)
    sys.exit(app.exec_())