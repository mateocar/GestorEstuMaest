#creamos el error 
from fastapi.responses import JSONResponse



class StudenNotExist(Exception):
    message: str = "El estudiante no encontrado "

class TeacherNotExist(Exception):
    message: str = "El profesor no encontrado "
    

class CourseComplete(Exception):
    message: str = "El curso esta completo "
    
    
def studen_not_exist_handler(_, exc: Exception): # manejadores de errores 
    return JSONResponse(status_code = 404, content = {"message": exc.message})

def teacher_not_exist_handler(_, exc: Exception):
    return JSONResponse(status_code = 404, content = {"message": exc.message})

def course_complete_handler(_, exc: Exception):
    return JSONResponse(status_code = 405, content = {"message": exc.message})

def registrer_error_handlers(app):
    app.add_exception_handler(StudenNotExist, studen_not_exist_handler)
    app.add_exception_handler(TeacherNotExist, teacher_not_exist_handler)
    app.add_exception_handler(CourseComplete, course_complete_handler)
    
    


