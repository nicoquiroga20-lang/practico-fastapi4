from pydantic import BaseModel, Field
from typing import Annotated

# metadatos reutilizables 
STR_NOMBRE = Annotated[str, Field(max_length=50, description='Nombre del articulo')]
PRECIO_VALOR = Annotated[float, Field(gt=0, lt=1000000, description='Precio del articulo')]
BOOL_ACTIVO = Annotated[bool, Field(description='¿El articulo se encuentra activo?')]

# modelo gral
class ArticuloSchema(BaseModel):
    id: Annotated[int, Field(gt=0, description='ID del articulo')]
    nombre_articulo: STR_NOMBRE
    precio: PRECIO_VALOR
    activo: BOOL_ACTIVO = True

# modelo para las vistas de edicion/actualizacion 
class ArticuloUpdateSchema(BaseModel):
    nombre_articulo: STR_NOMBRE
    precio: PRECIO_VALOR