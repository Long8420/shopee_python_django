from django import forms
from product.models import ProductReview


class ProductReviewForm(forms.ModelForm):
    review = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Nhap binh luan'}))

    class Meta:
        model = ProductReview
        fields = ["review", "rating"]
