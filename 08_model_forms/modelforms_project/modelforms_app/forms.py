from django import forms
from django.core import validators

# if you want to make custom validators
# create a function outside of the class
# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError("name needs to start with Z")

class FormName(forms.Form):
    # name = forms.CharField(validators=[check_for_z])
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Verify Email:')
    text = forms.CharField(widget=forms.Textarea)
    # https://docs.djangoproject.com/en/4.1/ref/forms/widgets/#built-in-widgets

    # hidden fields - remains in the html but 
    # is hidden from the user, this can be used 
    # to catch bots on our server

    # when we have this field it will not show up to the user

    # if a bot visits your page they will not look at the website,
    # they'll try to look at the html and fill in values,
    # and then submit the form that way. 
    # we will validate the input the most basic method a clean function

    # django has built in tools but this will just be a custom validator
    # name it clean_{name of whats being cleaned}
    # this is whithin a class so use self
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     # so if a bot filled out that field
    #     if len(botcatcher) > 0:
    #         # raise an error
    #         raise forms.ValidationError("This action is not permitted")
    #     return botcatcher

    # you can use djangos built in validators
    botcatcher = forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])

    # if you want to clean the entire form use clean
    def clean(self):
        # if you use super you will grab all of the data at once
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError('Emails do not match!')

    # more documentation here https://docs.djangoproject.com/en/4.1/ref/forms/validation/
 
    # we've seen how we can use Django Forms to grab information 
    # from the user and then do something with it, like print it 
    # to the console, but what if we wanted to save it to a model?

    # Instead of inheriting from the forms.Forms class, we will use forms.ModelForm in our forms.py file
    # This helper class allows us to create a form from a pre-existing model
    # - We then add an inline class(something we haven't seen before) called Meta
    # - This Meta class provides information connecting the model to the form

    # Example:

    # from django import forms
    # from myapp.models import MyModel

    # class MyNewForm(forms.ModelForm):
    #   #Form Fields go here

    #   class Meta:
    #       # form fields go here /with validators params
    #       model = MyModel
    #       fields = #lets see the options!

            # the fields attribute will connect to the model
            # there are many ways to make that connection
            # you first need to think about security for the fields,
            # its common to not provide any addtional field info, 
            # since you're already matching up the form to match up with the model
            # exactly, you don't actually need to specify those fields,
            # so typically you'll just see the inline Meta class after the forms class

            # the methods to work with the fields attribute that's inside of the inline Meta class
            # option 1) set it the special keyword "__all__" - this grabs all the fields from the model and you're going to place them into the form
            # option 2) specify the fields that you actually want to exclude

            # from django import forms
            # from myapp.models import Mymodel
            # class MyNewForm(forms.ModelForm):
                # Form Fields go here
                # class Meta:
                    # model = MyModel
         # (option 2) exclude = ["field1","field2"]

            # option 3) list the included fields
            # fields = ("field1","field2")

            # 4:54