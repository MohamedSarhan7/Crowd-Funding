# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.core.validators import RegexValidator
# from django.core.validators import FileExtensionValidator
# from django.core.exceptions import ValidationError
# from django.utils.translation import gettext_lazy as _

# from django.conf import settings

# # Create your models here.

# class User(AbstractUser):
    
#     email = models.EmailField(_("email address"), blank=False,unique=True)
    
#     phone=models.CharField(max_length=11,
#         validators=[RegexValidator(r'^01[0125][0-9]{8}$')])

#     # need to confirm email 
#     is_active = models.BooleanField(
#         _("active"),
#         default=False,
#         help_text=_(
#             "Designates whether this user should be treated as active. "
#             "Unselect this instead of deleting accounts."
#         ),
#     )

#     REQUIRED_FIELDS = ['first_name','last_name','email',"picture","phone"]
    
#     # validate image fun
#     def validate_image(fieldfile_obj):
#         filesize = fieldfile_obj.file.size
#         megabyte_limit = 1.0
#         if filesize > megabyte_limit*1024*1024:
#             raise ValidationError("Max file size is %sMB" % str(megabyte_limit))
    
#     # image field
#     picture=models.ImageField(upload_to="picture/",
#             max_length=1024*1024,
#             validators=[validate_image,
#             FileExtensionValidator(allowed_extensions=settings.ALLOWED_IMAGE_EXTENSIONS)
#             ])
