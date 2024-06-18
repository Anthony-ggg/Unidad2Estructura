from flask import Blueprint, jsonify, abort, request, render_template, redirect, make_response
from controls.facturaDaoControl import FacturaDaoControl
from controls.personaDaoControl import PersonaDaoControl
from flask_cors import CORS

from models.enumTipoIdentificacion import EnumTipoIdentificacion
router = Blueprint('router', __name__)


#GET es para presentar datos
#POST guardar datos, modificar datos y el inicio de sesion
#
@router.route('/')
def home():
    return render_template("template.html")
    
#lista personas
@router.route('/personas')
def lista_personas():
    pd = PersonaDaoControl()
    list = pd._list()
    list.sort_models("_apellidos", 2)
    return render_template("nene/lista.html",lista=pd.to_dic_lista(list))


@router.route('/personas/<tipo>/<attr>/<metodo>')
def lista_personas_ordenar(tipo ,attr, metodo):
    #pd = PersonaDaoControl()
    pd = PersonaDaoControl()
    list = pd._list()
    list.sort_models(attr, int(tipo),metodo)
   # return render_template("nene/lista.html",lista=pd.to_dic_lista(list))
    return make_response(
        jsonify({"msg":"OK", "code": 200, "data": pd.to_dic_lista(list)}),
        200
    )


#Lista personasa
#@router.route ('/personas/<tipo>/<attr>')
#def lista_personas_ordenar (tipo ,attr):
#   pd = PersonaDaoControl()
 #   list = pd._list()
  #  list.sort_models(attr, int(tipo))
   # return render_template("nene/lista.html",lista=pd.to_dic_lista(list))

#Lista personas
@router.route('/personas/ver')
def ver_guardar():
    return render_template("nene/guardar.html")

#editar personas
@router.route('/personas/editar/<pos>')
def ver_editar(pos):
    pd = PersonaDaoControl()
    nene = pd._list().get(int(pos) -1)
    print(nene)
    return render_template("nene/editar.html", data = nene )


#guardar personas
@router.route('/personas/guardar', methods=["POST"])
def guardar_personas():
    pd = PersonaDaoControl()
    data = request.form
    
    if not "apellido" in data.keys():
        abort(400)
        
    #TODO ...Validar
    pd._persona._apellidos = data["apellido"]
    pd._persona._nombres = data["nombre"]
    pd._persona._direccion = data["dir"]
    pd._persona._dni = data["dni"]
    pd._persona._telefono = data["fono"]
    pd._persona._tipoIdentificacion = "CEDULA"
    pd.save
    return redirect("/personas", code=302)

@router.route('/personas/modificar', methods=["POST"])
def modificar_personas():
    pd = PersonaDaoControl()
    data = request.form
    pos = data["id"]
    nene = pd._list().get(int(data["id"]))
    if not "apellido" in data.keys():
        abort(400)
        
    #TODO ...Validar
    pd._persona = nene
    pd._persona._apellidos = data["apellido"]
    pd._persona._nombres = data["nombre"]
    pd._persona._direccion = data["dir"]
    pd._persona._dni = data["dni"]
    pd._persona._telefono = data["fono"]
    pd._persona._tipoIdentificacion = "CEDULA"
    pd.merge(int(pos) -1)
    return redirect("/personas", code=302)


@router.route('/personas/eliminar', methods=["POST"])
def eliminar_personas():
    pd = PersonaDaoControl()
    pos = request.form["id"]
    pd._delete(int(pos))
    return redirect("/personas", code=302)


#lista facturas
@router.route('/facturas')
def lista_facturas():
    pd = FacturaDaoControl()
    return render_template("factura/lista.html", lista=pd.to_dict())

@router.route('/facturas/<tipo>/<attr>/<metodo>')
def lista_facturas_buscar(tipo ,attr, metodo):
    #pd = FacturaDaoControl()
    pd = FacturaDaoControl()
    list = pd._lista
    aux = list.search_models(attr, tipo, metodo)
    return make_response(
        jsonify({"msg":"OK", "code": 200, "data": pd.to_dic_lista(aux)}),
        200
    )

    #return render_template("factura/lista.html", lista=pd.to_dict())



#guardar facturas
@router.route('/factura/guardar', methods=["GET", "POST"])
def guardar_factura():
    pd = PersonaDaoControl()
    tipos_identificacion = [tipo.value for tipo in EnumTipoIdentificacion]
    
    if request.method == "POST":
        pd_f = FacturaDaoControl()
        data = request.form

        pd_f._factura._fecha = data["fecha"]
        pd_f._factura._precio = data["precio"]
        pd_f._factura._tipo = data["tipo_identificacion"]
        pd_f._factura._retencion = data["retencion"]
        lista=pd.to_dict()
        for persona in lista:
            if persona["id"]==int(data["persona"]):
                pd_f._factura._persona=persona
                break

        pd_f._factura._ruc = data["ruc"]
        pd_f._factura._subtotal = data["subtotal"]
        pd_f.save
        return redirect("/facturas", code=302)
    return render_template("factura/guardar.html", lista=pd.to_dict(), tipos_identificacion=tipos_identificacion)
    
#editar facturas
@router.route('/factura/editar/<id>', methods=["GET", "POST"])
def editar_factura(id):
    pd_persona = PersonaDaoControl()
    tipos_identificacion = [tipo.value for tipo in EnumTipoIdentificacion]
    pd_f= FacturaDaoControl()

    if request.method == "POST":
        data = request.form
        pd_f._factura._id = data["id"]
        pd_f._factura._fecha = data["fecha"]
        pd_f._factura._precio = data["precio"]
        pd_f._factura._tipo = data["tipo_identificacion"]
        pd_f._factura._retencion = data["retencion"]
        pos= int(data["pos"])
        lista=pd_persona.to_dict()
        for persona in lista:
            if persona["id"]==int(data["persona"]):
                pd_f._factura._persona=persona
                break
        pd_f._factura._ruc = data["ruc"]
        pd_f._factura._subtotal = data["subtotal"]
        pd_f.merge(pos)
        return redirect("/facturas", code=302)

    
    lista=pd_f.to_dict()
    f_en=None
    pos=None
    for indice, factura in enumerate(lista):
        if factura["id"]==int(id):
            f_en=factura
            pos=indice
            break

    return render_template("factura/editar.html",pos=pos ,f_en = f_en,lista=pd_persona.to_dict(),tipos_identificacion=tipos_identificacion)

#eliminar facturas
@router.route('/factura/eliminar/<id>')
def eliminar_factura(id):
    pd_f= FacturaDaoControl()

    lista=pd_f.to_dict()
    pos=None
    fact=None
    for indice, factura in enumerate(lista):
        if factura["id"]==int(id):
            fact=factura
            pos=indice
            break
    pd_f.delete(pos)
    return redirect("/facturas", code=302)