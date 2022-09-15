from django import forms
from django.forms import ModelForm
from .models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = (
            'product_code',
            'product_name',
            'description',
            'category',
            'image',
            'color',
            'size',
            'quantity',
        )
        labels={
                'product_code':'Product Code',
                'product_name':'Product Name',
                'description':'Description',
                'category':'Category',
                'image':'Image',
                'color':'Color',
                'Size':'size',
                'quantity':'Quantity',
        }
        widgets={
            'product_code' : forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Input Code',
                
                }
            ),
            'product_name' : forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Input Name',
                },
            ),
            'description' : forms.Textarea(
                attrs={
                    'class':'form-control',
                    'rows':'4',
                }
            ),
            'category' : forms.Select(
                attrs={
                    'class':'form-control',
                }
            ),
            'image' : forms.FileInput(
                attrs={
                    'class':'form-control',
                }
            ),
            'color' : forms.TextInput(
                attrs={
                    'class':'form-control',
                }
            ),
            'size' : forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'input Size',
                }
            ),
            'quantity' : forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'input Quantity',
                }
            ),
        }