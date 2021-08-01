from django import forms

from manager.models import Inventory, Member


class MemberForm(forms.ModelForm):
    inventory = forms.ModelChoiceField(queryset=Inventory.objects.all())

    class Meta:
        model = Member
        exclude = ['booking_count', 'date_joined']

    def clean(self):
        cleaned_data = super(MemberForm, self).clean()
        existing_instance = Member.objects.filter(
            name=cleaned_data['name'], surname=cleaned_data['surname']).first()
        if existing_instance and existing_instance.booking_count >= 2:
            self.add_error('name', 'Booking limit reach to its maximum of 2.')
        return cleaned_data

    def save(self, commit=True):
        existing_instance = Member.objects.filter(
            name=self.instance.name, surname=self.instance.surname).first()
        if existing_instance:
            self.instance = existing_instance
        self.instance.booking_count += 1
        return super().save(commit=commit)
