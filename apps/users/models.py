from django.db.models import CharField, EmailField, ImageField, BooleanField, DateTimeField, ForeignKey, CASCADE
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from simple_history.models import HistoricalRecords
from rest_framework_simplejwt.tokens import RefreshToken

roles_choices = (
    ('regular', 'Regular'),
    ('admin', 'Admin'),
)

status_choices = (
    ('activo', 'Activo'),
    ('inactivo', 'Inactivo'),
    ('bloqueado', 'Bloqueado'),
    ('eliminado', 'Eliminado'),
)

statuscredential_choices = (
    ('revision', 'Revision'),
    ('denegada', 'Denegada'),
    ('aceptado', 'Aceptado'),
    ('eliminado', 'Eliminado'),
)
class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None, **other_fields):
        if not email:
            raise ValueError('Debe proporcionar una dirección de correo electrónico')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **other_fields)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        # other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, name, password, **other_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = EmailField('Correo electronico', max_length=50 ,unique=True, null=False, blank=False,db_index=True)
    name = CharField('Nombre', max_length=50, null=False, blank=False)
    role = CharField('Rol', choices=roles_choices ,max_length=50,blank=False, default='regular')
    status = CharField('Estatus', choices=status_choices, max_length=10, blank=False, default='activo')
    statuscredential = CharField('Estatus de credencial', choices=statuscredential_choices, max_length=10, blank=False, default='revision')
    created_at = DateTimeField('Creado', auto_now_add=True)
    updated_at = DateTimeField('Actualizado', auto_now=True)

    is_staff = BooleanField(default=True)
    is_superuser = BooleanField(default=True)

    historical = HistoricalRecords()
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name
    
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return{
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        }

    def has_role(self, role):
        return self.role == role