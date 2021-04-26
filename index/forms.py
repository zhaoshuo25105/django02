from django import forms

# 初始化数据为了控制选项
TOPIC_choice=(
    ('1','好评'),
    ('2','中平'),
    ('３','差评'),
)

class RemarkForm(forms.Form):
    subject = forms.CharField(label='标题')
    email = forms.EmailField(label='邮箱')
    message = forms.CharField(label='内容',widget=forms.Textarea)
    topic = forms.ChoiceField(label='级别',choices=TOPIC_choice)
    isSaved = forms.BooleanField(label='是否保存')
