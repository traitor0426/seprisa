from typing import Any
from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.views import generic

from django.db.models import QuerySet

from django.views import View

from contacts.models import Contact
from contacts.models import FormatoRecepcionMateriaAlergenos
from contacts.models import FormatoRecepcionMaterialEmpaque
from contacts.models import FormatoRecepcionMateriaPrima
from contacts.models import EtiquetaIdentificacionMateriales
from contacts.models import OrdenProduccion
from contacts.models import DetalleOrden
from contacts.models import FormatoBitacoraProductoTerminado
from contacts.models import FormatoSolicitudAnalisis
from contacts.models import KardexRecepcionMateriaPrimaAlmacen

from django.views.generic.detail import DetailView

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

# CONTACTOS ---------------------------------------------

class ContactListView(generic.ListView):
    model = Contact
    paginate_by = 5

    def get_queryset(self) -> QuerySet[Any]:
        q = self.request.GET.get('q')

        if q:
            return Contact.objects.filter(name__icontains=q)

        return super().get_queryset() 


class ContactCreateView(generic.CreateView): 
    model = Contact 
    fields = ('name', 'email', 'birth','phone',)
    success_url = reverse_lazy('contact_list')

class ContactUpdateView(generic.UpdateView):
    model = Contact
    fields = ('name', 'email', 'birth', 'phone',)
    success_url = reverse_lazy('contact_list')

class ContactDeleteView(generic.DeleteView):
    model = Contact
    success_url = reverse_lazy('contact_list')

class Menu(View):   
     def get(self, request, *args, **kwargs):
     	return render(request, 'contacts/menu.html')
     
# FORMATO RECEPCION MATERIA ALERGENOS -------------------------------
     
class FormatoRecepcionMateriaAlergenosView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contacts/formato_recepcion_materia.html')

class FormatoRecepcionMateriaAlergenosListView(generic.ListView):
    model = FormatoRecepcionMateriaAlergenos
    paginate_by = 5

    def get_queryset(self) -> QuerySet[Any]:
        q = self.request.GET.get('q')

        if q:
            return FormatoRecepcionMateriaAlergenos.objects.filter(name__icontains=q)

        return super().get_queryset() 

# FORMATO RECEPCION MATERIAL EMPAQUE --------------------------------

class FormatoRecepcionMaterialEmpaqueView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contacts/formato_recepcion_material_empaque.html')

class FormatoRecepcionMaterialEmpaqueListView(generic.ListView):
    model = FormatoRecepcionMaterialEmpaque
    paginate_by = 5

    def get_queryset(self) -> QuerySet[Any]:
        q = self.request.GET.get('q')

        if q:
            return FormatoRecepcionMaterialEmpaque.objects.filter(name__icontains=q)

        return super().get_queryset() 

# FORMATO RECEPCION MATERIA PRIMA ------------------------------------------------------

class FormatoRecepcionMateriaPrimaView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contacts/formato_recepcion_materia_prima.html')

class FormatoRecepcionMateriaPrimaListView(generic.ListView):
    model = FormatoRecepcionMateriaPrima
    paginate_by = 15
    template_name = 'contacts/formato_recepcion_materia_prima.html'

    def get_queryset(self) -> QuerySet[Any]:
        q = self.request.GET.get('q')

        if q:
            return FormatoRecepcionMateriaPrima.objects.filter(materiaprima__icontains=q)
        return super().get_queryset()

class FormatoRecepcionMateriaPrimaCreateView(generic.CreateView):
    model = FormatoRecepcionMateriaPrima 
    fields = ('materiaprima','loteseprisa','pesobruto','pesoneto','nocontenedores','claveproveedor','noanalisis','sku','noloteproveedor','fechacaducidad','recibe',)

    success_url = reverse_lazy('formato_recepcion_materia_prima')
    template_name='contacts/formato_recepcion_materia_prima_form.html'

class FormatoRecepcionMateriaPrimaUpdateView(generic.UpdateView):
    model = FormatoRecepcionMateriaPrima
    fields = ('materiaprima','loteseprisa','pesobruto','pesoneto','nocontenedores','claveproveedor','noanalisis','sku','noloteproveedor','fechacaducidad','recibe')
    success_url = reverse_lazy('formato_recepcion_materia_prima')
    template_name='contacts/formato_recepcion_materia_prima_form.html'

class FormatoRecepcionMateriaPrimaDeleteView(generic.DeleteView):
    model = FormatoRecepcionMateriaPrima
    success_url = reverse_lazy('formato_recepcion_materia_prima')
    template_name='contacts/formato_recepcion_materia_prima_confirm_delete.html'

# LOGIN ----------------------------------

class LoginView(View):

    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'contacts/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Menu') 
            else:
                messages.error(request, 'Credenciales incorrectas')
        return render(request, 'contacts/login.html')
    
# ETIQUETAS IDENTIFICACION MATERIALES ---------------------------------------------
class EtiquetaIdentificacionMaterialesView(View):
    def get(self, request, *args, **kwargs):
        search_query = request.GET.get('q', '')
        etiquetas = FormatoRecepcionMateriaPrima.objects.filter(materiaprima__icontains=search_query) if search_query else FormatoRecepcionMateriaPrima.objects.all()

        id = request.GET.get('id')
        etiqueta = get_object_or_404(FormatoRecepcionMateriaPrima, id=id) if id else None

        context = {
            'etiquetas': etiquetas,
            'etiqueta': etiqueta,
        }
        return render(request, 'contacts/etiqueta_identificacion_materiales.html', context)

class EtiquetaIdentificacionMaterialesListView(generic.ListView):
    model = EtiquetaIdentificacionMateriales
    template_name = 'contacts/etiqueta_identificacion_materiales.html'  # Cambia esto al nombre de tu plantilla

    def get_queryset(self) -> QuerySet[Any]:
        q = self.request.GET.get('q')

        if q:
            return Contact.objects.filter(name__icontains=q)

        return super().get_queryset() 
    
    
class EtiquetaIdentificacionMaterialesCreateView(generic.CreateView): 
    model = EtiquetaIdentificacionMateriales
    fields = ('material','noanalisis','proveedorclientesku','noloteproveedor','noloteinterno','pbruto','ptara','pneto','sku','contenedor','de','realizo','verifico',)
    success_url = reverse_lazy('etiqueta_identificacion_materiales')

class etiquetas(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contacts/etiqueta_identificacion_materiales.html')

def buscar_etiqueta_identificacion_materiales(request):
    etiqueta = ' '
    if 'q' in request.GET:
        query = request.GET['q']
        etiqueta = FormatoRecepcionMateriaPrima.objects.filter(materiaprima__icontains=query).first()
    
    return render(request, 'contacts/etiqueta_identificacion_materiales.html', {'etiqueta': etiqueta})

class GuardarEtiquetaView(View):
    def post(self, request, *args, **kwargs):
        formato_id = request.POST.get('id')
        formato_recepcion = get_object_or_404(FormatoRecepcionMateriaPrima, id=formato_id)

        etiqueta = EtiquetaIdentificacionMateriales(
            material=formato_recepcion.materiaprima,
            proveedorclientesku=formato_recepcion.claveproveedor,
            noloteproveedor=formato_recepcion.noloteproveedor,
            noloteinterno=formato_recepcion.loteseprisa,
            sku=formato_recepcion.sku,
            noanalisis=request.POST.get('no_analisis'),
            pbruto=request.POST.get('pbruto'),
            ptara=request.POST.get('ptara'),
            pneto=request.POST.get('pneto'),
            contenedor=request.POST.get('contenedor'),
            de=request.POST.get('de'),
            realizo=request.POST.get('realizo'),
            verifico=request.POST.get('verifico'),
        )
        etiqueta.save()
        try:
            etiqueta.save()
        except Exception as e:
            print("Error al guardar la etiqueta:", e)


        return redirect('etiquetas')
    
class orden_produccion(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contacts/orden_produccion.html')
    
class orden_produccion2(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contacts/orden_produccion2.html')
    

from django.shortcuts import get_object_or_404

def tu_vista_guardar(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        if id:
            etiqueta = get_object_or_404(EtiquetaIdentificacionMateriales, id=id)
        else:
            etiqueta = EtiquetaIdentificacionMateriales()

        materia_prima = request.POST.get('material')
        recepcion = FormatoRecepcionMateriaPrima.objects.filter(materiaprima=materia_prima).first()

        if recepcion:
            etiqueta.material = recepcion.materiaprima
            etiqueta.proveedorclientesku = recepcion.claveproveedor
            etiqueta.noloteproveedor = recepcion.noloteproveedor
            etiqueta.noloteinterno = recepcion.loteseprisa 
            etiqueta.sku = recepcion.sku

        etiqueta.noanalisis = request.POST.get('no_analisis')
        etiqueta.pbruto = request.POST.get('pbruto')
        etiqueta.ptara = request.POST.get('ptara')
        etiqueta.pneto = request.POST.get('pneto')
        etiqueta.contenedor = request.POST.get('contenedor')
        etiqueta.de = request.POST.get('de')
        etiqueta.realizo = request.POST.get('realizo')
        etiqueta.verifico = request.POST.get('verifico')

        etiqueta.save()
        return redirect('listar_etiquetas')  

    return redirect('buscar_etiqueta') 

# ETIQUETA CUARENTENA -------------------------------------------------------

class Etiqueta_cuarentena(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contacts/etiqueta_cuarentena.html')

class EtiquetaCuarentenaView(View):
    def get(self, request, *args, **kwargs):
        search_query = request.GET.get('q', '')
        if search_query:
            etiquetas = FormatoRecepcionMateriaPrima.objects.filter(materiaprima__icontains=search_query)
        else:
            etiquetas = FormatoRecepcionMateriaPrima.objects.all()
        
        id = request.GET.get('id')
        etiqueta = None
        if id:
            etiqueta = get_object_or_404(FormatoRecepcionMateriaPrima, id=id)
        
        context = {
            'etiquetas': etiquetas,
            'etiqueta': etiqueta,
        }
        return render(request, 'contacts/etiqueta_identificacion_materiales.html', context)    

class GuardarEtiquetaCuarentenaView(View):
    def post(self, request, *args, **kwargs):
        id = request.POST.get('id')
        data = {
            'materiaprima': request.POST.get('material'),
            'noanalisis': request.POST.get('no_analisis'),
            'firma': request.POST.get('firma'),
        }

        if id:
            etiqueta = get_object_or_404(FormatoRecepcionMateriaPrima, id=id)
            for key, value in data.items():
                setattr(etiqueta, key, value)
            etiqueta.save()
        else:
            FormatoRecepcionMateriaPrima.objects.create(**data)
        
        return redirect('tu_vista_listado')
    
    def post(self, request, *args, **kwargs):
        id = request.POST.get('id')
        data = {
            'nombre': request.POST.get('nombre'),
            'noanalisis': request.POST.get('no_analisis'),
            'firma': request.POST.get('firma'),
        }

        if id:
            etiqueta = get_object_or_404(FormatoRecepcionMateriaPrima, id=id)
            for key, value in data.items():
                setattr(etiqueta, key, value)
            etiqueta.save()
        else:
            FormatoRecepcionMateriaPrima.objects.create(**data)
        
        return redirect('tu_vista_listado')
        
class ListadoEtiquetaCuarentenaView(View):
    def get(self, request, *args, **kwargs):
        etiquetas = FormatoRecepcionMateriaPrima.objects.all()
        return render(request, 'contacts/etiqueta_cuarentena_list.html', {'etiquetas': etiquetas})

# FORMATO SOLICITUD ANALISIS -------------------------------------------------

class FormatoSolicitudAnalisisView(View): 
    def get(self, request, *args, **kwargs):
        search_query = request.GET.get('q', '')
        if search_query:
            etiquetas = FormatoSolicitudAnalisis.objects.filter(materiaprima__icontains=search_query)
        else:
            etiquetas = FormatoSolicitudAnalisis.objects.all()
        
        id = request.GET.get('id')
        etiqueta = ' '
        if id:
            etiqueta = get_object_or_404(FormatoSolicitudAnalisis, id=id)
        
        context = {
            'etiquetas': etiquetas,
            'etiqueta': etiqueta,
        }
        return render(request, 'contacts/formato_solicitud_analisis.html', context)

class Formato_solicitud_analisis(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contacts/formato_solicitud_analisis.html')

def buscar_solicitud_analisis(request):
    etiqueta = ' '
    if 'q' in request.GET:
        query = request.GET['q']
        etiqueta = FormatoSolicitudAnalisis.objects.filter(materiaprima__icontains=query).first()
    
    return render(request, 'contacts/formato_solicitud_analisis.html', {'etiqueta': etiqueta})

class GuardarSolicitudAnalisisView(View):
    def post(self, request, *args, **kwargs):
        id = request.POST.get('id')
        data = {
            'materiaprima': request.POST.get('materiaprima'),
            'productoterminado': request.POST.get('productoterminado'),
            'materialempaque': request.POST.get('materialempaque'),
            'noanalisis': request.POST.get('noanalisis'),
            'fechahoraentrada': request.POST.get('fechahoraentrada'),
            'nolote': request.POST.get('nolote'),
            'cantidadrecibida': request.POST.get('cantidadrecibida'),
            'nocontenedores': request.POST.get('nocontenedores'),
            'producto': request.POST.get('producto'),
            'solicitante': request.POST.get('solicitante'),
            'recibecc': request.POST.get('recibecc'),
            'muestreo': request.POST.get('muestreo'),
            'fechahoramuestreo': request.POST.get('fechahoramuestreo'),
            'observaciones': request.POST.get('observaciones'),
            'analista': request.POST.get('analista'),
            'fechahoradictamen': request.POST.get('fechahoradictamen'),
            'dictamen': request.POST.get('dictamen'),
            'aprobado': request.POST.get('aprobado'),
            'rechazado': request.POST.get('rechazado'),
            'observaciones': request.POST.get('observaciones'),
            'fechahoraentregaresultados': request.POST.get('fechahoraentregaresultados'),
            'enteradoresultado': request.POST.get('enteradoresultado'),



        }

        if id:
            etiqueta = get_object_or_404(FormatoSolicitudAnalisis, id=id)
            for key, value in data.items():
                setattr(etiqueta, key, value)
            etiqueta.save()
        else:
            FormatoSolicitudAnalisis.objects.create(**data)
        
        return redirect('tu_vista_listado')

class ListadoSolicitudAnalisisView(View):
    def get(self, request, *args, **kwargs):
        etiquetas = FormatoSolicitudAnalisis.objects.all()
        return render(request, 'contacts/formato_solicitud_analisis_list.html', {'etiquetas': etiquetas})
    


from django.http import JsonResponse 
from .models import FormatoRecepcionMateriaPrima

def get_materia_prima_details(request):
    query = request.GET.get('materiaprima', '')
    if query:
        try:
            item = FormatoRecepcionMateriaPrima.objects.get(materiaprima=query)
            data = {
                'materiaprima': item.materiaprima,
                'proveedor': item.proveedor,  
                'sku': item.sku,              
                'lote_interno': item.lote_interno,  
                'lote_proveedor': item.lote_proveedor,  
            }
            return JsonResponse(data)
        except FormatoRecepcionMateriaPrima.DoesNotExist:
            return JsonResponse({'error': 'No se encontró el registro'}, status=404)
    return JsonResponse({'error': 'No se proporcionó un nombre de materia prima'}, status=400)

# EXPORTAR DOCUMENTOS PDF ----------------------------------------------

from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa
from io import BytesIO

def export_contacts_pdf(request):
    contacts = Contact.objects.all()
    
    template_path = 'contacts/contacts_pdf.html'
    context = {'contacts': contacts}

    template = get_template(template_path)
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="contacts.pdf"'

    result = BytesIO()
    pisa_status = pisa.CreatePDF(BytesIO(html.encode("UTF-8")), dest=result)
    
    if pisa_status.err:
        return HttpResponse('Error generando el PDF', status=500)

    response.write(result.getvalue())
    return response

def export_etiqueta_identificacion_materiales_pdf(request):
    etiquetas = EtiquetaIdentificacionMateriales.objects.all()[:15]
    
    template_path = 'contacts/etiqueta_identificacion_materiales_pdf.html'
    context = {'etiquetas': etiquetas}

    template = get_template(template_path)
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="EtiquetaIdentificacionMateriales.pdf"'

    result = BytesIO()
    pdf = pisa.CreatePDF(BytesIO(html.encode("UTF-8")), dest=result)

    if pdf.err:
        return HttpResponse('Error generando el PDF', status=500)

    response.write(result.getvalue())
    return response

def export_etiqueta_cuarentena_pdf(request):
    FormatoRecepcionMateriaPrimax = FormatoRecepcionMateriaPrima.objects.all()[:15]
    
    template_path = 'contacts/etiqueta_cuarentena_pdf.html'
    context = {'FormatoRecepcionMateriaPrimax': FormatoRecepcionMateriaPrimax}

    template = get_template(template_path)
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="EtiquetaCuarentena.pdf"'

    result = BytesIO()
    pdf = pisa.CreatePDF(BytesIO(html.encode("UTF-8")), dest=result)

    if pdf.err:
        return HttpResponse('Error generando el PDF', status=500)

    response.write(result.getvalue())
    return 

def export_formato_solicitud_analisis_pdf(request):
    FormatoRecepcionMateriaPrimax = FormatoRecepcionMateriaPrima.objects.all()[:1]
    
    template_path = 'contacts/formato_solicitud_analisis_pdf.html'
    context = {'FormatoRecepcionMateriaPrimax': FormatoRecepcionMateriaPrimax}

    template = get_template(template_path)
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="FormatoSolicitudAnalisis.pdf"'

    result = BytesIO()
    pdf = pisa.CreatePDF(BytesIO(html.encode("UTF-8")), dest=result)

    if pdf.err:
        return HttpResponse('Error generando el PDF', status=500)

    response.write(result.getvalue())
    return response

def export_formato_recepcion_materia_prima_pdf(request):
    FormatoRecepcionMateriaPrimax = FormatoRecepcionMateriaPrima.objects.all()[:15]
    
    template_path = 'contacts/formato_recepcion_materia_prima_pdf.html'
    context = {'FormatoRecepcionMateriaPrimax': FormatoRecepcionMateriaPrimax}

    template = get_template(template_path)
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="FormatoRecepcionMateriaPrima.pdf"'

    result = BytesIO()

    pisa_status = pisa.CreatePDF(
        BytesIO(html.encode("UTF-8")),
        dest=result,
        show_error_as_pdf=True,
        encoding='UTF-8',
    )

    if pisa_status.err:
        return HttpResponse('Error generando el PDF', status=500)

    response.write(result.getvalue())
    return response

def export_orden_produccion_pdf(request):
    FormatoRecepcionMateriaPrimax = FormatoRecepcionMateriaPrima.objects.all()[:15]
    
    template_path = 'contacts/orden_produccion_pdf.html'
    context = {'FormatoRecepcionMateriaPrimax': FormatoRecepcionMateriaPrimax}

    template = get_template(template_path)
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="OrdendeProduccion.pdf"'

    result = BytesIO()
    pdf = pisa.CreatePDF(BytesIO(html.encode("UTF-8")), dest=result)

    if pdf.err:
        return HttpResponse('Error generando el PDF', status=500)

    response.write(result.getvalue())
    return response

def export_orden_produccion2_pdf(request):
    FormatoRecepcionMateriaPrimax = FormatoRecepcionMateriaPrima.objects.all()[:15]
    
    template_path = 'contacts/orden_produccion2_pdf.html'
    context = {'FormatoRecepcionMateriaPrimax': FormatoRecepcionMateriaPrimax}

    template = get_template(template_path)
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="OrdendeProduccion2.pdf"'

    result = BytesIO()
    pdf = pisa.CreatePDF(BytesIO(html.encode("UTF-8")), dest=result)

    if pdf.err:
        return HttpResponse('Error generando el PDF', status=500)

    response.write(result.getvalue())
    return response

def export_kardex_pdf(request):
    FormatoRecepcionMateriaPrimax = FormatoRecepcionMateriaPrima.objects.all()[:15]
    
    template_path = 'contacts/kardex_pdf.html'
    context = {'FormatoRecepcionMateriaPrimax': FormatoRecepcionMateriaPrimax}

    template = get_template(template_path)
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Kardex.pdf"'

    result = BytesIO()
    pdf = pisa.CreatePDF(BytesIO(html.encode("UTF-8")), dest=result)

    if pdf.err:
        return HttpResponse('Error generando el PDF', status=500)

    response.write(result.getvalue())
    return response

# ORDEN DE PRODUCCION ----------------------------------------------------------------

class OrdenProduccionView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contacts/orden_produccion.html')
    
class OrdenProduccionCreateView(generic.CreateView): 
    def get(self, request):
        return render(request, 'contacts/orden_produccion.html')

    def post(self, request):
        data = {
            'producto': request.POST.get('producto'),
            'claveskumaquila': request.POST.get('clavesku_maquila'),
            'presentacion': request.POST.get('presentacion'),
            'noordenproduccion': request.POST.get('noorden_produccion'),
            'numerolote': request.POST.get('numero_lote'),
            'fechacaducidad': request.POST.get('fecha_caducidad'),
            'fechainicioproceso': request.POST.get('fechainicio_proceso'),
            'fechaterminoproceso': request.POST.get('fechatermino_proceso'),
            'rendimientoteorico': request.POST.get('rendimiento_teorico'),
            'rendimientoreal': request.POST.get('rendimiento_real'),
        }

        OrdenProduccion.objects.create(**data)

        return redirect('orden_produccion_view')    
    
class OrdenProduccionListView(generic.ListView):
    model = DetalleOrden
    paginate_by = 5
    template_name = 'contacts/orden_produccion.html'

    def get_queryset(self) -> QuerySet[Any]:
        q = self.request.GET.get('q')

        if q:
            return DetalleOrden.objects.filter(material__icontains=q)
        
        return super().get_queryset() 

class OrdenProduccionCreateListView(generic.CreateView):
    model = DetalleOrden 
    fields = ('orden', 'skump', 'material', 'nolote', 'unidad', 'cantidad', 'surtio', 'verifico')
    success_url = reverse_lazy('ordenproduccion_list')
    template_name = 'contacts/formato_recepcion_materia_prima_form.html'


class OrdenProduccionUpdateView(generic.UpdateView):
    model = DetalleOrden
    fields = ('skump', 'material', 'nolote', 'unidad','cantidad','surtio','verifico',)
    success_url = reverse_lazy('ordenproduccion_list')
    template_name='contacts/orden_produccion_form.html'

class OrdenProduccionDeleteView(generic.DeleteView):
    model = DetalleOrden
    success_url = reverse_lazy('ordenproduccion_list')
    template_name='contacts/orden_produccion_form.html'



def buscar_orden_produccion(request):
    OrdenProduccion = ' '
    if 'q' in request.GET:
        query = request.GET['q']
        OrdenProduccion = OrdenProduccion.objects.filter(noordenproduccion__icontains=query).first()
    
    return render(request, 'contacts/orden_produccion.html', {'OrdenProduccion': OrdenProduccion})

def buscar_material(request):
    
    OrdenProduccion = ' '
    if 'q' in request.GET:
        query = request.GET['q']
        OrdenProduccion = OrdenProduccion.objects.filter(material__icontains=query).first()
    
    return render(request, 'contacts/orden_produccion.html', {'OrdenProduccion': OrdenProduccion})

def orden_produccion_view(request):
    return render(request, 'orden_produccion.html')



class ControlAseguramientoView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contacts/control_aseguramiento_calidad.html')
    
def export_control_aseguramiento_pdf(request):
    FormatoRecepcionMateriaPrimax = FormatoRecepcionMateriaPrima.objects.all()[:15]
    
    template_path = 'contacts/control_aseguramiento_calidad_pdf.html'
    context = {'FormatoRecepcionMateriaPrimax': FormatoRecepcionMateriaPrimax}

    template = get_template(template_path)
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="ControlAseguramiento.pdf"'

    result = BytesIO()
    pdf = pisa.CreatePDF(BytesIO(html.encode("UTF-8")), dest=result)

    if pdf.err:
        return HttpResponse('Error generando el PDF', status=500)

    response.write(result.getvalue())
    return response

def export_control_aseguramiento2_pdf(request):
    FormatoRecepcionMateriaPrimax = FormatoRecepcionMateriaPrima.objects.all()[:15]
    
    template_path = 'contacts/control_aseguramiento_calidad_pdf2.html'
    context = {'FormatoRecepcionMateriaPrimax': FormatoRecepcionMateriaPrimax}

    template = get_template(template_path)
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="ControlAseguramiento2.pdf"'

    result = BytesIO()
    pdf = pisa.CreatePDF(BytesIO(html.encode("UTF-8")), dest=result)

    if pdf.err:
        return HttpResponse('Error generando el PDF', status=500)

    response.write(result.getvalue())
    return response
    
class MenuPView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contacts/menu copy 2.html')
    
class MenuPrView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contacts/menuprueba3.html')
    
class FormatoBitacoraProductoTerminadoView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contacts/formato_bitacora_producto_terminado.html')
    
def export_bitacora_producto_terminado_pdf(request):
    FormatoBitacoraProductoTerminadox = FormatoBitacoraProductoTerminado.objects.all()[:15]
    
    template_path = 'contacts/formato_bitacora_producto_terminado_pdf.html'
    context = {'FormatoBitacoraProductoTerminadox': FormatoBitacoraProductoTerminadox}

    template = get_template(template_path)
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="BitacoraProductoTerminado.pdf"'

    result = BytesIO()
    pdf = pisa.CreatePDF(BytesIO(html.encode("UTF-8")), dest=result)

    if pdf.err:
        return HttpResponse('Error generando el PDF', status=500)

    response.write(result.getvalue())
    return response

class FormatoBitacoraProductoTerminadoView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contacts/formato_bitacora_producto_terminado.html')

class FormatoBitacoraProductoTerminadoListView(generic.ListView):
    model = FormatoBitacoraProductoTerminado
    paginate_by = 15
    template_name = 'contacts/formato_bitacora_producto_terminado.html'

    def get_queryset(self) -> QuerySet[Any]:
        q = self.request.GET.get('q')

        if q:
            return FormatoBitacoraProductoTerminado.objects.filter(producto__icontains=q)
        return super().get_queryset()

class FormatoBitacoraProductoTerminadoCreateView(generic.CreateView):
    model = FormatoBitacoraProductoTerminado
    fields = ('fechaentrada','producto','lote','sku','presentacion','contenedores','cliente','noanalisis','fechacaducidad','recibe','contenedores',)

    success_url = reverse_lazy('bitacora_producto_terminado_view')
    template_name='contacts/formato_bitacora_producto_terminado_form.html'

class FormatoBitacoraProductoTerminadoUpdateView(generic.UpdateView):
    model = FormatoRecepcionMateriaPrima
    fields = ('fechaentrada','producto','lote','sku','presentacion','contenedores','cliente','noanalisis','fechacaducidad','recibe','contenedores',)
    success_url = reverse_lazy('bitacora_producto_terminado_view')
    template_name='contacts/formato_bitacora_producto_terminado_form.html'

class FormatoBitacoraProductoTerminadoDeleteView(generic.DeleteView):
    model = FormatoRecepcionMateriaPrima
    success_url = reverse_lazy('bitacora_producto_terminado_view')
    template_name='contacts/formato_bitacora_producto_terminado_confirm_delete.html'

class kardex(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contacts/kardex.html')
    

from django.shortcuts import render
from .models import KardexRecepcionMateriaPrimaAlmacen

# def buscar_kardex(request):
#     query = request.GET.get('q', '')
#     if query:
#         # Aquí asumimos que 'materiaprima' es un campo de texto o tiene un método __str__ que se puede comparar
#         resultados = KardexRecepcionMateriaPrimaAlmacen.objects.filter(materiaprima__materiaprima__icontains=query)
#     else:
#         resultados = KardexRecepcionMateriaPrimaAlmacen.objects.all()

#     return render(request, 'kardex.html', {'resultados': resultados, 'query': query})

# def buscar_kardex(request):
#     query = request.GET.get('q', '')  # Obtener el término de búsqueda
#     if query:
#         # Filtrar los objetos según la materia prima o SKU
#         resultados = KardexRecepcionMateriaPrimaAlmacen.objects.filter(
#             materiaprima__materiaprima__icontains=query
#         )
#         if resultados.exists():
#             # Obtener el primer resultado y rellenar los campos del formulario con esos valores
#             primer_resultado = resultados.first()
#             return render(request, 'contacts/kardex.html', {
#                 'resultados': resultados,
#                 'query': query,
#                 'etiqueta': primer_resultado
#             })
#     else:
#         resultados = KardexRecepcionMateriaPrimaAlmacen.objects.all()

#     return render(request, 'contacts/kardex.html', {'resultados': resultados, 'query': query})

def buscar_kardex(request):
    etiqueta = ' '
    if 'q' in request.GET:
        query = request.GET['q']
        etiqueta = FormatoRecepcionMateriaPrima.objects.filter(materiaprima__icontains=query).first()
    
    return render(request, 'contacts/kardex.html', {'etiqueta': etiqueta})

# def buscar_kardex(request):
#     query = request.GET.get('q', '')  # Obtener el término de búsqueda
#     if query:
#         # Filtrar por materia prima o SKU y mostrar los datos correspondientes
#         resultados = KardexRecepcionMateriaPrimaAlmacen.objects.filter(
#             materiaprima__materiaprima__icontains=query
#         )
#         if resultados.exists():
#             primer_resultado = resultados.first()
#             # Al devolver los resultados, aseguramos que los campos relacionados con la materia prima se completen en el formulario
#             return render(request, 'contacts/kardex.html', {
#                 'resultados': resultados,
#                 'query': query,
#                 'etiqueta': primer_resultado  # Este es el objeto que se va a usar para llenar el formulario
#             })
#     else:
#         resultados = KardexRecepcionMateriaPrimaAlmacen.objects.all()

#     return render(request, 'contacts/kardex.html', {'resultados': resultados, 'query': query})

from .models import KardexRecepcionMateriaPrimaAlmacen, FormatoRecepcionMateriaPrima

from django.shortcuts import render, redirect
from .models import KardexRecepcionMateriaPrimaAlmacen, FormatoRecepcionMateriaPrima
from datetime import datetime


from django.shortcuts import render, redirect, get_object_or_404
from .models import KardexRecepcionMateriaPrimaAlmacen, FormatoRecepcionMateriaPrima

class GuardarKardexView(View):
    def post(self, request, *args, **kwargs):
        formato_id = request.POST.get('id')
        
        if not formato_id:
            return render(request, 'contacts/kardex.html', {'error': 'ID de formato no encontrado.'})

        formato_recepcion = get_object_or_404(FormatoRecepcionMateriaPrima, id=formato_id)

        fechasalida = request.POST.get('fecha_salida', None)
        if not fechasalida:
            return render(request, 'contacts/kardex.html', {'error': 'La fecha de salida es obligatoria.'})
        
        try:
            kardex = KardexRecepcionMateriaPrimaAlmacen(
                materiaprima=formato_recepcion.materiaprima,  
                fechacaducidad=formato_recepcion.fechacaducidad,
                noloteseprisa=formato_recepcion.loteseprisa,
                fechaentrada=formato_recepcion.fechaentrada,
                cantidadneto=formato_recepcion.pesoneto,
                codigoproveedorcliente=formato_recepcion.claveproveedor,
                sku=formato_recepcion.sku,

                fechasalida=fechasalida,  
                clienteusointerno=request.POST.get('cliente_usointerno', ''),
                noloteproveedor=request.POST.get('lote_proveedor', ''),
                cantidadsale=request.POST.get('cantidad_sale', 0),  
                cantidadqueda=request.POST.get('cantidad_queda', 0),
                realizo=request.POST.get('realizo', ''),
                observaciones=request.POST.get('observaciones', ''), 

                formato_recepcion=formato_recepcion
            )
            kardex.save()
            return redirect('kardex_list') 
        except Exception as e:
            return render(request, 'contacts/kardex.html', {'error': f'No se pudo guardar el kardex: {e}'})


class KardexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contacts/kardex.html')
    
def buscar_kardex(request):
    etiqueta = ' '
    if 'q' in request.GET:
        query = request.GET['q']
        etiqueta = FormatoRecepcionMateriaPrima.objects.filter(materiaprima__icontains=query).first()

    return render(request, 'contacts/kardex.html', {'etiqueta': etiqueta})

class KardexListView(generic.ListView):
    model = KardexRecepcionMateriaPrimaAlmacen
    paginate_by = 15
    template_name = 'contacts/kardex.html'

    def get_queryset(self) -> QuerySet[Any]:
        R = self.request.GET.get('q')

        if R:
            return KardexRecepcionMateriaPrimaAlmacen.objects.filter(clienteusocliente__icontains=R)
        return super().get_queryset()

class KardexCreateView(generic.CreateView):
    model = KardexRecepcionMateriaPrimaAlmacen
    fields = (
        'materiaprima', 'fechacaducidad', 'noloteseprisa', 'fechaentrada', 
        'cantidadneto', 'codigoproveedorcliente', 'sku', 
        'fechasalida', 'clienteusointerno', 'noloteproveedor', 
        'cantidadsale', 'cantidadqueda', 'realizo', 'observaciones'
    )
    success_url = reverse_lazy('kardex_list')
    template_name = 'contacts/kardex_form.html'
    

class KardexUpdateView(generic.UpdateView):
    model = KardexRecepcionMateriaPrimaAlmacen
    fields = ('fechasalida','clienteusointerno','loteproveedor','cantidadsale','cantidadqueda','realizo','observaciones')
    success_url = reverse_lazy('kardex_list')
    template_name='contacts/kardex_form.html'

class KardexDeleteView(generic.DeleteView):
    model = KardexRecepcionMateriaPrimaAlmacen
    success_url = reverse_lazy('kardex_list')
    template_name='contacts/kardex_confirm_delete.html'




