import sys
from src.vista.InterfazCajaSeguridad import App_CajaDeSeguridad
from src.logica.FachadaCajaDeSeguridad import FachadaCajaDeSeguridad

if __name__ == '__main__':
    # Punto inicial de la aplicación

    logica = FachadaCajaDeSeguridad()

    app = App_CajaDeSeguridad(sys.argv, logica)
    sys.exit(app.exec_())