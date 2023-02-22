
from xml.dom import ValidationErr
from django import forms
from django.utils.safestring import  mark_safe
from .models import The_member,BStudyMember

class Bible_SleaderForm(forms.Form):
    set_bs_leader=forms.BooleanField(label="",widget=forms.CheckboxInput(attrs={"class":"choose"}))


class InputForm(forms.Form):
    group_size=forms.IntegerField(initial=6,max_value=2)

class MemberForm(forms.ModelForm):
    class Meta:
        model=The_member
        fields=[
             "year_of_study",
             "gender",
            "leader_status",
        ]
        
        widgets={
            "year_of_study":forms.TimeInput(attrs={"class":"hello"})
        }
        labels={
            "year_of_study":""
        }


    #Clean the fields 
    # make sure that a field has a specific word

    def clean_gender(self,*args,**kwargs):
        gender=self.cleaned_data.get('gender')
        print(gender)
        return gender

    def clean_year_of_study(self,*args, **kwargs):
        year_of_study=self.cleaned_data.get('year_of_study')
      
        if year_of_study!=None:
            if year_of_study > 6 or year_of_study < 1:
                raise forms.ValidationError('This is not a valid level!')
            return year_of_study
        else:
            raise ValidationErr("Please fill the year of study field")


# Horizontal renderer
#class HorizontalRadioRenderer(forms.RadioSelect.renderer):
#    def render(self):
#        return mark_safe(u'\n'.join([u'%sn'% w for w in self]))
class BibleStudyMemberRegisterForm(forms.ModelForm):
    class Meta:
        model=BStudyMember
        fields=[
             "level",
             "gender",
            "leader_status",
            "first_name",
            "middle_name",
            "sir_name",
            "phone_number"
        ]

        widgets={
            "level":forms.NumberInput(attrs={"class":"input-field","placeholder":"year of study"}),
            #"gender":forms.RadioSelect(attrs={"class":"input-field"}),
           # "leader_status":forms.CheckboxInput(attrs={"class":"input-field","placeholder":"Want to be a bs leader?"}),
            "first_name":forms.TextInput(attrs={"class":"input-field","placeholder":"first name"}),
            "middle_name":forms.TextInput(attrs={"class":"input-field","placeholder":"middle name"}),
            "sir_name":forms.TextInput(attrs={"class":"input-field","placeholder":"sir name"}),
            "phone_number":forms.TextInput(attrs={"class":"input-field","placeholder":"Phone number"})

        }
        

        labels={
            
            "first_name":"",
            "middle_name":"",
            "level":"",
            "sir_name":"",
            "phone_number":"",
            "leader_status":"Want to be BS leader? "
        }
    def clean_level(self,*args, **kwargs):
         level=self.cleaned_data.get('level')
         if level!=None:
             if level > 6 or level < 1:
                 print(level)
                 raise forms.ValidationError('This is not a valid level!')
             return level
         else:
             raise ValidationErr(f"Please fill the year of study field")

