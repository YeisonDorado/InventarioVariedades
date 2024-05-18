from Modelos.ComprobanteVenta import ComprobanteVenta
from Modelos.Producto import Producto
from Modelos.Cliente import Cliente
from Repositorios.RepositorioComprobanteVenta import RepositorioComprobanteVenta
from Repositorios.RepositorioProducto import RepositorioProducto
from Repositorios.RepositorioCliente import RepositorioCliente

class ControladorComprobanteVenta():
    def __init__(self):
        self.repositorioComprobanteVenta = RepositorioComprobanteVenta()
        self.repositorioProductos = RepositorioProducto()
        self.repositorioClientes = RepositorioCliente()

    def index(self):
        return self.repositorioComprobanteVenta.findAll()

    """
    Asignacion CLIENTE y PRODUCTOS a COMPROBANTE VENTA
    """

    def create(self, infoComprobanteVenta, id_producto, id_cliente):
        nuevoComprobanteVenta = ComprobanteVenta(infoComprobanteVenta)
        elProducto = Producto(self.repositorioProductos.findById(id_producto))
        elCliente = Cliente(self.repositorioClientes.findById(id_cliente))
        nuevoComprobanteVenta.producto = elProducto
        nuevoComprobanteVenta.Cliente = elCliente
        return self.repositorioComprobanteVenta.save(nuevoComprobanteVenta)



    def show(self, id):
        elComproventaVenta = ComprobanteVenta(self.repositorioComprobanteVenta.findById(id))
        return elComproventaVenta.__dict__

    """
    Modificación de comprobante (producto y cliente)
    """

    def update(self, id, infoComprobanteVenta, id_producto, id_cliente):
        elComprobanteVenta = ComprobanteVenta(self.repositorioComprobanteVenta.findById(id))
        elComprobanteVenta.comp_numero = infoComprobanteVenta["comp_numero"]
        elComprobanteVenta.comp_fecha = infoComprobanteVenta["comp_fecha"]
        elComprobanteVenta.comp_item = infoComprobanteVenta["comp_item"]
        elComprobanteVenta.comp_cantidad_venta_prod = infoComprobanteVenta["comp_cantidad_venta_prod"]
        elComprobanteVenta.comp_precio_venta_prod = infoComprobanteVenta["comp_precio_venta_prod"]
        elComprobanteVenta.comp_valor_total_prod = infoComprobanteVenta["comp_valor_total_prod"]
        elComprobanteVenta.comp_total_pago = infoComprobanteVenta["comp_total_pago"]
        elComprobanteVenta.comp_nombre_vendedor = infoComprobanteVenta["comp_nombre_vendedor"]
        elComprobanteVenta.comp_forma_pago = infoComprobanteVenta["comp_forma_pago"]
        elProducto = Producto(self.repositorioProductos.findById(id_producto))
        elCliente = Cliente(self.repositorioClientes.findById(id_cliente))
        elComprobanteVenta.producto = elProducto
        elComprobanteVenta.cliente = elCliente
        return self.repositorioComprobanteVenta.save(elComprobanteVenta)



    def delete(self, id):
        return self.repositorioComprobanteVenta.delete(id)