from django import forms


class SubmissionForm(forms.Form):
    code = forms.CharField(
        label="",
        widget=forms.Textarea(
            attrs={
                "rows": 18,
                "class": "code-editor",
                "placeholder": "Введите решение...",
                "spellcheck": "false",
                "autocapitalize": "none",
                "autocomplete": "off",
                "wrap": "off",
            }
        ),
    )
