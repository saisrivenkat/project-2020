from django.contrib import admin

from .models.studentinfo import Student

from .models.stddetail import Stdind
from .models.stddetail import Stdacd
from .models.stddetail import Stdpro
from .models.stddetail import Stdcour
# Register your models here.
admin.site.register(Student)

admin.site.register(Stdind)
admin.site.register(Stdcour)
admin.site.register(Stdacd)
admin.site.register(Stdpro)