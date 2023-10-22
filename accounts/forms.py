from django import forms
from django.contrib.auth import get_user_model, authenticate


User = get_user_model()



class LoginForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("email", "password")
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control", "placeholder": f"{name.capitalize()}"})
    


    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        user = authenticate(email=email, password=password)

        if not user:
            raise forms.ValidationError("Email or password is wrong")
        
        if not user.is_active:
            raise forms.ValidationError("This account is not activated")
        
        return self.cleaned_data
