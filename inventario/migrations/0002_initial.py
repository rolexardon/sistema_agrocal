# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'bodega'
        db.create_table(u'inventario_bodega', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigo', self.gf('django.db.models.fields.CharField')(unique=True, max_length='20')),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length='50')),
            ('descripcion', self.gf('django.db.models.fields.TextField')(max_length='250')),
            ('encargado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empleados.Empleado'], unique=True)),
        ))
        db.send_create_signal(u'inventario', ['bodega'])

        # Adding model 'producto_bodega'
        db.create_table(u'inventario_producto_bodega', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['producto.Producto'])),
            ('bodega', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventario.bodega'])),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
            ('transaccion', self.gf('django.db.models.fields.IntegerField')(default=2)),
        ))
        db.send_create_signal(u'inventario', ['producto_bodega'])

        # Adding unique constraint on 'producto_bodega', fields ['producto', 'bodega']
        db.create_unique(u'inventario_producto_bodega', ['producto_id', 'bodega_id'])

        # Adding model 'compra'
        db.create_table(u'inventario_compra', (
            ('orden_compra', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('proveedor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='compra_proveedor', to=orm['proveedores.Proveedor'])),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('pagada', self.gf('django.db.models.fields.BooleanField')()),
            ('fecha_creacion', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('usuario_creador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('costo_flete', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=12, decimal_places=2)),
            ('subtotal_compra', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=12, decimal_places=2)),
            ('total_compra', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=12, decimal_places=2)),
        ))
        db.send_create_signal(u'inventario', ['compra'])

        # Adding model 'compra_producto'
        db.create_table(u'inventario_compra_producto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('compra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventario.compra'])),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['producto.Producto'])),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
            ('costo', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
        ))
        db.send_create_signal(u'inventario', ['compra_producto'])

        # Adding unique constraint on 'compra_producto', fields ['compra', 'producto']
        db.create_unique(u'inventario_compra_producto', ['compra_id', 'producto_id'])

        # Adding model 'producto_transferencia'
        db.create_table(u'inventario_producto_transferencia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['producto.Producto'])),
            ('bodega_origen', self.gf('django.db.models.fields.related.ForeignKey')(related_name='bodega', to=orm['inventario.bodega'])),
            ('bodega_destino', self.gf('django.db.models.fields.related.ForeignKey')(related_name='bodega_destino', to=orm['inventario.bodega'])),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
            ('total_origen', self.gf('django.db.models.fields.IntegerField')()),
            ('total_destino', self.gf('django.db.models.fields.IntegerField')()),
            ('fecha_creacion', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('usuario_creador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'inventario', ['producto_transferencia'])


    def backwards(self, orm):
        # Removing unique constraint on 'compra_producto', fields ['compra', 'producto']
        db.delete_unique(u'inventario_compra_producto', ['compra_id', 'producto_id'])

        # Removing unique constraint on 'producto_bodega', fields ['producto', 'bodega']
        db.delete_unique(u'inventario_producto_bodega', ['producto_id', 'bodega_id'])

        # Deleting model 'bodega'
        db.delete_table(u'inventario_bodega')

        # Deleting model 'producto_bodega'
        db.delete_table(u'inventario_producto_bodega')

        # Deleting model 'compra'
        db.delete_table(u'inventario_compra')

        # Deleting model 'compra_producto'
        db.delete_table(u'inventario_compra_producto')

        # Deleting model 'producto_transferencia'
        db.delete_table(u'inventario_producto_transferencia')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'empleados.empleado': {
            'Meta': {'object_name': 'Empleado'},
            'direccion': ('django.db.models.fields.TextField', [], {'max_length': "'250'"}),
            'e_civil': ('django.db.models.fields.CharField', [], {'max_length': "'1'"}),
            'f_nacimiento': ('django.db.models.fields.DateField', [], {}),
            'fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'genero': ('django.db.models.fields.CharField', [], {'max_length': "'1'"}),
            'habilitado': ('django.db.models.fields.CharField', [], {'max_length': "'2'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identidad': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': "'15'"}),
            'p_apellido': ('django.db.models.fields.CharField', [], {'max_length': "'125'"}),
            'p_nombre': ('django.db.models.fields.CharField', [], {'max_length': "'125'"}),
            's_apellido': ('django.db.models.fields.CharField', [], {'max_length': "'125'", 'blank': 'True'}),
            's_nombre': ('django.db.models.fields.CharField', [], {'max_length': "'125'", 'blank': 'True'}),
            't_fijo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            't_movil': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': "'1'"}),
            'usuario_creador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        u'inventario.bodega': {
            'Meta': {'object_name': 'bodega'},
            'codigo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': "'20'"}),
            'descripcion': ('django.db.models.fields.TextField', [], {'max_length': "'250'"}),
            'encargado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empleados.Empleado']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': "'50'"})
        },
        u'inventario.compra': {
            'Meta': {'object_name': 'compra'},
            'costo_flete': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '12', 'decimal_places': '2'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'orden_compra': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pagada': ('django.db.models.fields.BooleanField', [], {}),
            'proveedor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'compra_proveedor'", 'to': u"orm['proveedores.Proveedor']"}),
            'subtotal_compra': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '12', 'decimal_places': '2'}),
            'total_compra': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '12', 'decimal_places': '2'}),
            'usuario_creador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'inventario.compra_producto': {
            'Meta': {'unique_together': "(('compra', 'producto'),)", 'object_name': 'compra_producto'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'compra': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventario.compra']"}),
            'costo': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['producto.Producto']"})
        },
        u'inventario.producto_bodega': {
            'Meta': {'unique_together': "(('producto', 'bodega'),)", 'object_name': 'producto_bodega'},
            'bodega': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventario.bodega']"}),
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['producto.Producto']"}),
            'transaccion': ('django.db.models.fields.IntegerField', [], {'default': '2'})
        },
        u'inventario.producto_transferencia': {
            'Meta': {'object_name': 'producto_transferencia'},
            'bodega_destino': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'bodega_destino'", 'to': u"orm['inventario.bodega']"}),
            'bodega_origen': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'bodega'", 'to': u"orm['inventario.bodega']"}),
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['producto.Producto']"}),
            'total_destino': ('django.db.models.fields.IntegerField', [], {}),
            'total_origen': ('django.db.models.fields.IntegerField', [], {}),
            'usuario_creador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'producto.producto': {
            'Meta': {'object_name': 'Producto'},
            'codigo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': "'125'"}),
            'descripcion': ('django.db.models.fields.TextField', [], {'max_length': "'250'"}),
            'fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'habilitado': ('django.db.models.fields.CharField', [], {'max_length': "'2'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': "'125'"}),
            'precio_costo': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'precio_preferencial': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'precio_venta_max': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'precio_venta_med': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'precio_venta_min': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'proveedor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['proveedores.Proveedor']"}),
            'usuario_creador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'proveedores.proveedor': {
            'Meta': {'object_name': 'Proveedor'},
            'codigo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': "'125'"}),
            'credito': ('django.db.models.fields.CharField', [], {'max_length': "'2'"}),
            'direccion': ('django.db.models.fields.TextField', [], {'max_length': "'250'"}),
            'habilitado': ('django.db.models.fields.CharField', [], {'max_length': "'2'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'n_contacto': ('django.db.models.fields.CharField', [], {'max_length': "'50'", 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': "'125'"}),
            'pais': ('django.db.models.fields.CharField', [], {'max_length': "'25'"}),
            'tel_contacto': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tel_proveedor': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['inventario']