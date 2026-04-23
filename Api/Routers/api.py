from fastapi import FastAPI, Depends, Request, HTTPException, status, Cookie
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="Frontend/Static"), name="static")
templates = Jinja2Templates(directory="./Frontend/templates")

@app.get("/Home", response_class=HTMLResponse)
async def get_login(request: Request):
    return templates.TemplateResponse(
        request=request, name="Home.html", context={"request": request}
    )

@app.get("/Menu", response_class=HTMLResponse)
async def get_register(request: Request):
    return templates.TemplateResponse(
        request=request, name="menu.html", context={"request": request}
    )
# @app.post("/Register/")
# async def post_register(
#     request: Request,
#     user_data: UsuarioCreate = Depends(UsuarioCreate.as_form),
#     db: Session = Depends(get_db)
# ):
#     resultado = RegistrarNuevoUsuario(user_data, db) 
#     return templates.TemplateResponse(
#             "Login.html", 
#             {"request": request, "resultado": resultado}
#             )
    
# async def obtener_usuario_actual(
#     request: Request, 
#     access_token: str = Cookie(None), 
#     db: Session = Depends(get_db)
# ):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="No autorizado",
#         headers={"WWW-Authenticate": "Bearer"},
#     )

#     if not access_token:
#         raise credentials_exception 

#     try:
#         token_limpio = access_token.replace("Bearer ", "") if access_token.startswith("Bearer ") else access_token
#         payload = verificar_token(token_limpio)
        
#         user_id = payload.get("sub")
#         if user_id is None:
#             raise credentials_exception
            
#     except Exception:
#         raise credentials_exception

#     usuario = db.query(Usuario).filter(Usuario.id_usuario == user_id).first()
    
#     if usuario is None:
#         raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
#     return usuario

# @app.get("/Home", response_class=HTMLResponse)
# async def get_home(
#     request: Request, 
#     db: Session = Depends(get_db),
#     usuario_actual: Usuario = Depends(obtener_usuario_actual)
# ):
#     return templates.TemplateResponse("Home.html", {
#         "request": request, 
#         "usuario": usuario_actual.nombre_usuario 
#     })

# @app.post("/Home", response_class=HTMLResponse)
# async def post_Login(
#     request: Request,
#     user_data: LoginValidacion = Depends(LoginValidacion.as_form),
#     db: Session = Depends(get_db)
# ):
#     resultado = VerificarUsuario(user_data, db) 
    
#     if not resultado["auth"]:
#         return templates.TemplateResponse("Login.html", {
#             "request": request, 
#             "error": resultado["message"]
#         })

#     response = templates.TemplateResponse("Home.html", {
#         "request": request, 
#         "usuario": resultado["usuario"] 
#     })
    
#     # Guardamos el JWT en la cookie
#     response.set_cookie(
#         key="access_token", 
#         value=f"Bearer {resultado['token']}", 
#         httponly=True,
#         samesite="Lax",
#         secure= False,
#         max_age=3600
#     )
    
#     return response


# @app.post("/VisualizacionDatos")
# async def visualizar_datos(
#     datos: SubirPdf = Depends(SubirPdf.as_form), 
#     db: Session = Depends(get_db),
#     usuario_actual: Usuario = Depends(obtener_usuario_actual)
# ):
#     service = InforPdfService(db=db)
#     # El service ahora recibe 'datos' que tiene el 'RegistroSelect' (ID de vacante)
#     resultado = await service.procesar_subida_pdf(datos, usuario_id=usuario_actual.id_usuario)
#     return resultado

# @app.post("/CrearRegistroPostulacion")
# async def post_crear_registro(
#     request: Request,
#     registro_data: CrearRegistro = Depends(CrearRegistro.as_form), 
#     db: Session = Depends(get_db),
#     usuario_actual: Usuario = Depends(obtener_usuario_actual) 
# ):
#     try:
#         RegistrarNuevoRegistro(registro_data, db, id_usuario_logueado=usuario_actual.id_usuario)
#         return RedirectResponse(url="/Home", status_code=303)
#     except Exception as e:
#         return templates.TemplateResponse("Home.html", {"request": request, "error": str(e)})
    
# @app.get("/RegistroVacante", response_class=HTMLResponse)
# async def get_register(
#     request: Request, 
#     db: Session = Depends(get_db),
#     usuario_actual: Usuario = Depends(obtener_usuario_actual) 
# ):
#     registros = get_registros_by_user_id(db, usuario_id=usuario_actual.id_usuario)
    
#     return templates.TemplateResponse(
#         "RegistrosVacantes.html", 
#         {"request": request, "resultado": registros}
#     )

# # RUTA POST 
# @app.post("/BuscarRegistro")
# async def buscar_usuario(
#     request: Request,
#     form_data: BuscaRegistro = Depends(BuscaRegistro.as_form), 
#     db: Session = Depends(get_db),
#     usuario_actual: Usuario = Depends(obtener_usuario_actual)
# ):
#     if not form_data.search_id or form_data.search_id.strip() == "":
        
#         registros = get_registros_by_user_id(db, usuario_id=usuario_actual.id_usuario)
#         documentRegistro = get_registros_by_document_id(db, usuario_id=usuario_actual.id_usuario)
        
#     else:
#         registros = get_registros_by_user_service(db, search_data=form_data, id_usuario=usuario_actual.id_usuario)
#         documentRegistro = get_registros_by_document_id(db, usuario_id=usuario_actual.id_usuario)
        
#     return templates.TemplateResponse(
#         "RegistrosVacantes.html", 
#         {"request": request, "resultado": registros, "documentRegistro": documentRegistro}
#     )
# @app.get("/Candidatos/{registro_id}")
# async def api_obtener_candidatos(registro_id: int, db: Session = Depends(get_db)):
#     candidatos = get_registros_by_document_id(db, registro_id=registro_id)
    
#     # Retornamos los datos para que el JS los reciba
#     return candidatos

# @app.get("/SubirDocumentos", response_class=HTMLResponse)
# async def get_upload_view(
#     request: Request, 
#     db: Session = Depends(get_db),
#     usuario_actual: Usuario = Depends(obtener_usuario_actual)
# ):
#     # USAMOS LA FUNCIÓN QUE TRAE TODO DEL USUARIO
#     # (Asegúrate de que 'get_registros_by_user_id' esté importada)
#     registros = get_registros_by_user_id(db, usuario_id=usuario_actual.id_usuario)
    
#     return templates.TemplateResponse(
#         "SubirPdf.html", 
#         {
#             "request": request, 
#             "usuario": usuario_actual, 
#             "resultado": registros 
#         } 
#     )