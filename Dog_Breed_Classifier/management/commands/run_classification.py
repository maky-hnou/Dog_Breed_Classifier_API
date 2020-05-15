from django.core.management.base import BaseCommand
from Dog_Breed_Classifier.core.classification import Dog_Classifier
from Dog_Breed_Classifier.models import ImageModel


class Command(BaseCommand):
    def run_classifier(self, image):
        classifier = Dog_Classifier(image)
        classifier.get_dog_category()

    def handle(self, *args, **kwargs):
        non_processed = ImageModel.objects.filter(processed=False)[:2]
        for image in non_processed:
            self.run_classifier(image)
