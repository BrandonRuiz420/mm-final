# Generated by Django 3.2.8 on 2023-08-01 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MM', '0002_auto_20230731_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='cve_productofk',
            field=models.IntegerField(null=True, verbose_name='Clave del producto'),
        ),
        migrations.AlterField(
            model_name='almacen',
            name='idproductofk',
            field=models.IntegerField(null=True, verbose_name='Id de producto'),
        ),
        migrations.AlterField(
            model_name='almacen',
            name='tipoproducto',
            field=models.CharField(max_length=100, verbose_name='Tipo de producto'),
        ),
        migrations.AlterField(
            model_name='aparatos',
            name='cve_rutinafk',
            field=models.IntegerField(null=True, verbose_name='Clave rutina'),
        ),
        migrations.AlterField(
            model_name='aparatos',
            name='uso',
            field=models.CharField(max_length=100, verbose_name='Uso'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='ape_ma',
            field=models.CharField(max_length=100, verbose_name='Apellido Materno'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='ape_pa',
            field=models.CharField(max_length=100, verbose_name='Apellido paterno'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='certi_med',
            field=models.CharField(max_length=100, verbose_name='Certificado médico'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='edad',
            field=models.IntegerField(verbose_name='Edad'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='inscripcion',
            name='cve_clientefk',
            field=models.IntegerField(null=True, verbose_name='Clave cliente'),
        ),
        migrations.AlterField(
            model_name='inscripcion',
            name='fecha',
            field=models.DateField(verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='inscripcion',
            name='fecha_fin',
            field=models.DateField(verbose_name='Fecha de termino'),
        ),
        migrations.AlterField(
            model_name='inscripcion',
            name='fecha_inicio',
            field=models.DateField(verbose_name='Fecha de inicio'),
        ),
        migrations.AlterField(
            model_name='inscripcion',
            name='membresia',
            field=models.CharField(max_length=100, verbose_name='Membresia'),
        ),
        migrations.AlterField(
            model_name='inscripcion',
            name='monto',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Monto'),
        ),
        migrations.AlterField(
            model_name='inscripcion',
            name='tipo_inscrip',
            field=models.CharField(max_length=100, verbose_name='Tipo de inscripción'),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='cantidadventa',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Cantidad de venta'),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='consumo',
            field=models.IntegerField(verbose_name='Consumo'),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='cve_sociofk',
            field=models.IntegerField(null=True, verbose_name='Clave socio'),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='ganancia',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Ganancia'),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='productostotales',
            field=models.IntegerField(verbose_name='Productos totales'),
        ),
        migrations.AlterField(
            model_name='mm',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Precio'),
        ),
        migrations.AlterField(
            model_name='mm',
            name='producto',
            field=models.CharField(max_length=100, verbose_name='Producto'),
        ),
        migrations.AlterField(
            model_name='pe',
            name='costoserv',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Costo del servicio'),
        ),
        migrations.AlterField(
            model_name='pe',
            name='refaccion',
            field=models.CharField(max_length=100, verbose_name='Refaccion'),
        ),
        migrations.AlterField(
            model_name='pe',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='cantidad_ped',
            field=models.IntegerField(verbose_name='Cantidad pedido'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='idproductofk',
            field=models.IntegerField(null=True, verbose_name='Id de producto'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='numeropfk',
            field=models.IntegerField(null=True, verbose_name='Numero de producto'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='oferta_desc',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Descuento'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='servicioreqfk',
            field=models.IntegerField(null=True, verbose_name='Servicio'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='totalP',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='costo_extra',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Costo extra'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='cve_clientefk',
            field=models.IntegerField(null=True, verbose_name='Clave cliente'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='horario',
            field=models.DateTimeField(verbose_name='Horario'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='instructor',
            field=models.CharField(max_length=100, null=True, verbose_name='Instructor'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='rutina',
            field=models.CharField(max_length=100, verbose_name='Rutina'),
        ),
        migrations.AlterField(
            model_name='pp',
            name='costoproducto',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Costo del producto'),
        ),
        migrations.AlterField(
            model_name='pp',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total'),
        ),
        migrations.AlterField(
            model_name='proveedores',
            name='cve_productofk',
            field=models.IntegerField(null=True, verbose_name='Clave del producto'),
        ),
        migrations.AlterField(
            model_name='proveedores',
            name='direccion',
            field=models.CharField(max_length=100, verbose_name='Direccion'),
        ),
        migrations.AlterField(
            model_name='proveedores',
            name='servicioreqfk',
            field=models.IntegerField(null=True, verbose_name='Servicio requerido'),
        ),
        migrations.AlterField(
            model_name='proveedores',
            name='telefono',
            field=models.IntegerField(verbose_name='Telefono'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='cve_sociofk',
            field=models.IntegerField(null=True, verbose_name='Clave socio'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='telefono',
            field=models.IntegerField(verbose_name='Telefono'),
        ),
        migrations.AlterField(
            model_name='rutinas',
            name='cve_clientefk',
            field=models.IntegerField(null=True, verbose_name='Clave cliente'),
        ),
        migrations.AlterField(
            model_name='rutinas',
            name='descripcion',
            field=models.CharField(max_length=100, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='ape_ma',
            field=models.CharField(max_length=100, verbose_name='Apellido materno'),
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='ape_pa',
            field=models.CharField(max_length=100, verbose_name='Apellido paterno'),
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='cliente_asig',
            field=models.CharField(max_length=100, verbose_name='Cliente asignado'),
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='cve_clientefk',
            field=models.IntegerField(null=True, verbose_name='Clave cliente'),
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='edad',
            field=models.IntegerField(verbose_name='Edad'),
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='horario',
            field=models.DateTimeField(verbose_name='Horario'),
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='salario',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Salario'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='cve_clientefk',
            field=models.IntegerField(null=True, verbose_name='Clave cliente'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='cve_producto',
            field=models.CharField(max_length=100, verbose_name='Clave del producto'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateField(verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='idproductofk',
            field=models.IntegerField(null=True, verbose_name='Id de producto'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total'),
        ),
    ]