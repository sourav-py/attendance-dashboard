from import_export import resources
from .models import SampleModel

class SampleModelResource(resources.ModelResource):
    class Meta:
        model = SampleModel
    