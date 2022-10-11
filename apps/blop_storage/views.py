from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import HttpResponse
from django.views.generic import FormView
from django import forms
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
import pandas as pd
from os import environ
from datetime import date

from apps.inventory.models import Inventory
from base_model.models import User, Branch, Product
from utils.azure_blop_storage.core import AzureBlobStorage


connect_str = environ['CONNECTION_STRING']


class BlobStorageForm(forms.Form):
    file = forms.FileField(
        label=_('File')
    )

    def __init__(self, *args, **kwargs):
        super(BlobStorageForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id_uploadForm'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_file'
        self.helper.add_input(Submit("submit", "Submit"))


class BlobStorageView(FormView):
    template_name = "blob_storage/index.html"
    form_class = BlobStorageForm
    success_url = '/blob_storage'
    azure_blob_storage = AzureBlobStorage(connect_str)

    @staticmethod
    def handle_file(file: InMemoryUploadedFile) -> pd:
        return pd.read_csv(file, sep=';')

    @staticmethod
    def validate_user(pk: int) -> None:
        user = User.objects.filter(pk=pk).first()
        if not user:
            User.objects.create(**{
               "gln_user": pk,
               "username": pk
            })

    @staticmethod
    def validate_branch(pk: int) -> None:
        branch = Branch.objects.filter(pk=pk).first()
        if not branch:
            Branch.objects.create(**{
                "gln_branch": pk
            })

    @staticmethod
    def validate_product(pk: int) -> None:
        product = Product.objects.filter(pk=pk).first()
        if not product:
            Product.objects.create(**{
                "gtin_product": pk
            })

    def validate_data(self, data: dict) -> None:
        self.validate_user(data['GLN_Cliente'])
        self.validate_branch(data['GLN_Sucursal'])
        self.validate_product(data['Gtin_Producto'])

    @staticmethod
    def update_or_create_inventory(data: dict, last_inventory_id: int) -> tuple[any, bool]:
        inventory_day, inventory_month, inventory_year = data['FechaInventario'].split(sep='/')

        return Inventory.objects.update_or_create(**{
            "id": last_inventory_id,
            "inventory_date": date(year=int(inventory_year), month=int(inventory_month), day=int(inventory_day)),
            "gln_user_id": data['GLN_Cliente'],
            "gln_branch_id": data['GLN_Sucursal'],
            "gtin_product_id": data['Gtin_Producto'],
            "quantity": data['Inventario_Final'],
            "unit_value": data['PrecioUnidad']
        })

    def create_containers(self) -> None:
        self.azure_blob_storage.create_container('processed')
        self.azure_blob_storage.create_container('unprocessed')

    def post(self, request, *args, **kwargs) -> HttpResponse:
        self.create_containers()
        handle_file = self.handle_file(self.request.FILES['file'])
        unprocessed_saved = False
        last_inventory_id = Inventory.objects.all().last().id

        for data in handle_file.to_dict('records'):
            last_inventory_id += 1

            if not unprocessed_saved:
                file_name = f"{data['GLN_Cliente']}_{now().day}_{now().month}_{now().year}_{last_inventory_id}"
                self.azure_blob_storage.upload_file_to_container(
                    container_name='unprocessed',
                    file_name=file_name,
                    file=handle_file,
                    client_id=data['GLN_Cliente']
                )
                unprocessed_saved = True

            self.validate_data(data)
            self.update_or_create_inventory(data, last_inventory_id)

        self.azure_blob_storage.upload_file_to_container(
            container_name='processed',
            file_name=file_name,
            file=handle_file,
            client_id=data['GLN_Cliente']
        )
        self.azure_blob_storage.delete_blob('unprocessed', file_name, data['GLN_Cliente'])

        return super(BlobStorageView, self).post(request, *args, **kwargs)
