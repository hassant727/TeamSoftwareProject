# from django import forms
# from .models import Post
# from multiupload.fields import MultiImageField

# class PostForm(forms.ModelForm):
# 	images = MultiImageField(min_num=1, max_num=10)

# 	class Meta:
# 		model = Post
# 		fields = ('title', 'content', 'images')

# 	def save(self, commit=True):
# 		image_upload = self.cleaned_data.pop('images')
# 		instance = super(PostForm, self).save()
# 		for each in image_upload:
# 			images = Image(image=each, post=instance)
# 			images.save()