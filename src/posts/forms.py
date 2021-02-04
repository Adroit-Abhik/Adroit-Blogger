from django import forms
from tinymce import TinyMCE
from.models import Post, Comments


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = Post
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['name', 'email', 'content']

        widgets = {
            'name': forms.TextInput(attrs={'calss': 'form-control', 'placeholder': 'Name', 'id': 'username'}),
            'email': forms.EmailInput(attrs={'calss':'form-control', 'placeholder': "Email Address (will not be published)", 'id': 'useremail', 'size': 40}),
            'content': forms.Textarea(attrs={'calss':'form-control', 'rows': 4, 'placeholder': "Type your comment", 'id': 'usercomment'})
        }
