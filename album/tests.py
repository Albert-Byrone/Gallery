from django.test import TestCase
from .models import Category,Image,Location

class TestImage(TestCase):
    def setUp(self):
        self.location = Location(name="Nairobi")
        self.location.save_location()

        self.category = Category(name="food")
        self.category.save_category()

        self.image_test =Image(id=1,name='image',description='this is a test image',location=self.location,category=self.category)
        self.image_test.save_image()

    def test_instance(self):
        self.assertTrue(isinstance(self.image_test,Image))

    def test_save_image(self):
        self.image_test.save_image()
        retrieve = Image.objects.all()
        self.assertTrue(len(retrieve)>0)

    def test_delete_image(self):
        self.image_test.delete_image()
        images =Image.objects.all()
        self.assertTrue(len(images) == 0)

    def test_update_image(self):
        self.image_test.save_image()
        self.image_test.update_image(self.image_test.id,'images/test,jpeg')
        updated_image=Image.objects.filter(image='images/test,jpeg')
        self.assertTrue(len(updated_image) >0)

    def test_get_image_by_id(self):
        found_image = self.image_test.get_image_by_id(self.image_test.id)
        image = Image.objects.filter(id=self.image_test.id)
        self.assertTrue(found_image,Image)

    def test_search_image_by_location(self):
        self.image_test.save_image()
        founded_images = self.image_test.filter_by_location(location='Nairobi')
        self.assertTrue(len(founded_images) == 1 )

    def test_search_image_by_category(self):
        category='food'
        found_image = self.image_test.search_by_category(category)
        self.assertTrue(len(found_image)> 0)

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()



class TestLocation(TestCase):
    def setUp(self):    
        self.location = Location(name ="Nairibi")
        self.location.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))

    def test_save_location(self):
        self.location .save_location()
        locations = Location.get_locations()
        self.assertTrue(len(locations)> 0)

    def test_get_location(self):
        self.location .save_location()
        locations = Location.get_locations()
        self.assertTrue(len(locations)> 0)

    def test_update_location(self):
        new_location = "Mombasa"
        self.location.update_location(self.location.id,new_location)
        changed_location = Location.objects.filter(name= 'Mombasa')
        self.assertTrue(len(changed_location)> 0)

    def test_delete_location(self):
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)

class TestCategory(TestCase):
    def setUp(self):
        self.category = Category(name= "Food")
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_by_category(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)> 0 )

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)