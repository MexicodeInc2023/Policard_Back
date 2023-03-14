from django.db.models import CharField, ImageField, DateField, IntegerField,  CASCADE, Model, ForeignKey, OneToOneField,DateTimeField, AutoField
from apps.users.models import User


statustudent_choices = (
    ('estudiante', 'Estudiante'),
    ('egresado', 'Egresado'),
    ('inactivo', 'Inactivo'),
)


statusStudentGrades_choices = (
    ('ninguno', 'Ninguno'),
    ('10a', '10A'),
    ('10b', '10B'),
    ('9a', '9A'),
    ('9b', '9B'),
    ('8a', '8A'),
    ('8b', '8B'),
    ('7a', '7A'),
    ('7b', '7B'),
    ('6a', '6A'),
    ('6b', '6B'),
    ('5a', '5A'),
    ('5b', '5B'),
    ('4a', '4A'),
    ('4b', '4B'),
    ('3a', '3A'),
    ('3b', '3B'),
    ('2a', '2A'),
    ('2b', '2B'),
    ('1a', '1A'),
    ('1b', '1B'),
)

statuscareer_choices = (
    ('activa', 'Activa'),
    ('inactiva', 'Inactiva'),
)

statusrequestreason_choices = (
    ('revision', 'Revision'),
    ('denegada', 'Denegada'),
    ('aceptado', 'Aceptado'),
    ('eliminado', 'Eliminado'),
)
statusinfo_choices = (
    ('en uso', 'En Uso'),
    ('eliminado', 'Eliminado'),
)

class careers(Model):
    nameCareers = CharField('nameCareers', max_length=50)
    status = CharField('status', choices=statuscareer_choices, max_length=10, blank=False, default='activa')
    created_at = DateTimeField('created_at', auto_now_add=True)
    updated_at = DateTimeField('updated_at', auto_now_add=True)
    
    class Meta:
        db_table = 'careers'
        verbose_name = 'careers'
        verbose_name_plural = 'careers'    

    def __str__(self):
        return f'{self.nameCareers.__str__()}'
    
class emergency_info(Model):
    emergency_name = CharField('emergency_name', max_length=100)
    emergency_phone = CharField('emergency phone', max_length=20)
    emergency_phone2 = CharField('emergency phone 2', max_length=20,null=True, blank=True)
    blood_type = CharField('blood type', max_length=10)
    status = CharField('status', choices=statusinfo_choices, max_length=10, blank=False, default='en uso')
    allergy = CharField('allergy', max_length=100)
    allergy2 = CharField('allergy 2', max_length=100,null=True, blank=True)
 
    class Meta:
        db_table = 'emergency_info'
        verbose_name = 'emergency_info'
        verbose_name_plural = 'emergency_infos'
    
    def __str__(self):
        return f' {self.status.__str__()}'
         

class student(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    id_careers = ForeignKey(careers, on_delete=CASCADE, verbose_name='careers',default=1)
    id_emInfo = ForeignKey(emergency_info, on_delete=CASCADE, verbose_name='emergency_info',default=1)
    personalName = CharField('personalName', max_length=100, null=False, blank=False)
    lastname = CharField('lastname', max_length=100)
    license = CharField('license', max_length=20,)
    birthday = DateField('birthday', null=True, blank=True)
    grade = CharField('grade', choices=statusStudentGrades_choices, max_length=10, blank=False, default='ninguno')
    city = CharField('city', max_length=100, null=False, blank=False)
    status = CharField('status', choices=statustudent_choices, max_length=15, blank=False, default='estudiante')
    photo = ImageField('photo',upload_to="alumn/photo", null=True, blank=True, default="alumn/logouni.jpg")
    class Meta:
        db_table = 'student'
        verbose_name = 'student'
        verbose_name_plural = 'students'
        
    def __str__(self):
        return self.user.name

    def get_email(self):
        return self.user.email

class request_reason(Model):
    id_st = ForeignKey(student, on_delete=CASCADE, verbose_name='student',default=1)
    reason = CharField('reason', max_length=500, null=False, blank=False)
    status = CharField('status', max_length=10, choices=statusrequestreason_choices, default='activa')
    class Meta:
        db_table = 'request_reason'
        verbose_name = 'request_reason'
        verbose_name_plural = 'request_reasons'    
        
    def __str__(self):
        return f' {self.id_st.__str__()} '