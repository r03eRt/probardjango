from django import forms

from .models import Registrado


# Anadimos el modelo del form asignandolo al modelo existente
class RegistradoForm(forms.ModelForm):
    class Meta:
        model = Registrado
        # Campos del modelo que queremos utilizar
        fields = ["nombre", "email", "codigo_postal"]

    # Cuando se guardamos y seguimos para anadir otro ponemos ese valor en el formulario
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail" in email:
            raise forms.ValidationError("Por favor usa un email gmail")

        return email
