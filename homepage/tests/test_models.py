from django.test import TestCase
from django.utils import timezone
from homepage.models import Author, Item, _FileType, Item_Image, RTI_File, Planes

class TestModels(TestCase):
    def setUp(self):    
        self.author = Author.objects.create(
            Last_Name="Doe",
            First_Name="John",
            Email="test@test.com") 
        self.item = Item.objects.create(
            Title='Image_Title',
            Author=self.author,
            Upload_Date = timezone.now(),
            Miniature_Image='test_img.jpg',
            Media=1
        )
        self.item_image = Item_Image.objects.create(
            Item=self.item,
            Image='test_image.jpg',
            View_Detail='Test View Detail',
            Index=1
        )
        self.rti_file = RTI_File.objects.create(
            Has_DZI=True,
            Has_TZI=False,
            Has_Image=True,
            Info_File='info.json',
            Item=self.item
        )
        self.planes = Planes.objects.create(
            File="plane_file.jpg",
            RTI_File=self.rti_file
        )

    def test_author_name(self):
        author_name = self.author.Name
        self.assertEqual(author_name, "Doe John")

    def test_author_str(self):
        author_str = str(self.author)
        self.assertEqual(author_str, "John Doe")
    
    def test_item_str(self):
        item_str = str(self.item)
        self.assertEqual(item_str, "Item Image_Title")

    def test_item_image_uploadDirectoryPath(self):
        directory_Path = self.item_image.uploadDirectoryPath('test_image.jpg')
        self.assertEqual(directory_Path, 'Image_Title/test_image.jpg')

    def test_item_image_str(self):
        item_image_str = str(self.item_image)
        self.assertEqual(item_image_str, "Item_Image test_image.jpg")

    def test_plane_str(self):
        plane_str = str(self.planes)
        self.assertEqual(plane_str, "plane_file.jpg")

