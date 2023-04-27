from django.db import models
import uuid
from django.core.validators import MinLengthValidator , MaxLengthValidator , MaxValueValidator , MinValueValidator
# Create your models here.
class BaseModel(models.Model):
    id=models.UUIDField(primary_key=True , default=uuid.uuid4 , editable=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract=True
        



    
class Teacher(BaseModel):
    name=models.CharField(max_length=100)
    qualification=models.CharField(max_length=200)
    
    class Meta:
        verbose_name_plural='Techers'
    
    def __str__(self):
        return self.name    
        
        


class Students(BaseModel):
    # book choides class
    class Books(models.TextChoices):
        ENG='eng' ,'eng'
        URDU='URDU' ,'URDU'
        MATH='MATH' ,'MATH'
        PHY='PHY' ,'PHY'
    
    name=models.CharField(max_length=100 , blank=True , null=True)
    age=models.PositiveIntegerField(default=10 , validators=[MinValueValidator(10) , MaxValueValidator(100) ] , null=True) 
    
    fee=models.DecimalField(max_digits=5 , decimal_places=2)
    url=models.SlugField()
    books=models.CharField(max_length=200, choices=Books.choices)
    teacher=models.ManyToManyField(Teacher)
    
    
    class Meta:
        verbose_name_plural='Students'
        
    def __str__(self):
        return f'{self.age}'
    
    