from django.db import models

class MyUser(models.Model):
    username = models.CharField('نام کاربری', max_length=50)
    password = models.CharField('گذرواژه', max_length=20)
    name = models.CharField(max_length=40, null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربر'


class CategoryChoices(models.TextChoices):
    SOCIAL = ('social', 'اجتماعی')
    SPORT = ('sport', 'ورزشی')

class Post(models.Model):
    title = models.CharField(max_length=40, blank=True)
    content = models.TextField(null=True, blank=True)
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_up = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=10, choices=CategoryChoices.choices, default=CategoryChoices.SOCIAL)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست'



# کار با دیتابیس مدلها
# نمایش اطلاعات به کاربر
# کار با فرمها در جنگو
# مدیریت کاربران