from django.test import TestCase, RequestFactory, Client
from homepage.models import Author, Item, Item_Image, _FileType
from homepage.views import detail_page, searchFunction, sortFunction, home, uploadItemFunction, uploadImageFunction
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime

class SearchPageTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            Last_Name="Doe",
            First_Name="John",
            Email="test@test.com")  
        self.item0 = Item.objects.create(
            Title="Image Title 0",
            Author=self.author,
            Miniature_Image="test_miniatureImg0.jpg",
            Upload_Date="2024-04-01",
            Media=1
        )
        self.image = Item_Image.objects.create(
            Item=self.item0,
            Image="test_image.jpg",
            View_Detail="Test View Detail",
            Index=1
        )
        self.item1 = Item.objects.create(
            Title="Image Title 1",
            Author=self.author,
            Miniature_Image="test_miniatureImg1.jpg",
            Upload_Date="2024-04-04",
            Media=1,
        )
        self.item2 = Item.objects.create(
            Title="Image Title 2",
            Author=self.author,
            Miniature_Image="test_minitureImg2.jpg",
            Upload_Date="2024-04-10",
            Media=1,
        )
        self.item3 = Item.objects.create(
            Title="Image Title 3",
            Author=self.author,
            Miniature_Image="test_minitureImg3.jpg",
            Upload_Date="2024-04-14",
            Media=1,
        )
        self.image1 = Item_Image.objects.create(
            Item=self.item1,
            Image="test_image1.jpg",
            View_Detail="Test View Detail 1",
            Index=1
        )
        self.image2 = Item_Image.objects.create(
            Item=self.item2,
            Image="test_image2.jpg",
            View_Detail="Test View Detail 2",
            Index=1
        )
        self.image3 = Item_Image.objects.create(
            Item=self.item3,
            Image="test_image3.jpg",
            View_Detail="Test View Detail 3",
            Index=1
        )
        self.search_condition = {
            "title": "Image Title 2",
            "files_Still_Images": "",
            "file_RTI": "",
            "datefrom": "2024-04-10",
            "dateto": "2024-04-11",
            "author": "John Doe",
            }

    def test_results_items(self):
        filtered_data = searchFunction(Item.objects.all(), self.search_condition)
        self.assertEqual(len(filtered_data[1]), 1)

    def test_results_title(self):    
        filtered_data = searchFunction(Item.objects.all(), self.search_condition)
        self.assertEqual(filtered_data[1][0].Title, "Image Title 2")

    def test_results_minitureImg(self):
        filtered_data = searchFunction(Item.objects.all(), self.search_condition)        
        self.assertEqual(filtered_data[1][0].Miniature_Image, "test_minitureImg2.jpg")

    def test_results_author(self):
        filtered_data = searchFunction(Item.objects.all(), self.search_condition)
        self.assertEqual(filtered_data[1][0].Author, self.author)

    def test_results_media(self):
        filtered_data = searchFunction(Item.objects.all(), self.search_condition)  
        self.assertEqual(filtered_data[1][0].Media, 1)
    
    def test_results_date(self):
        filtered_data = searchFunction(Item.objects.all(), self.search_condition)  
        self.assertEqual(str(filtered_data[1][0].Upload_Date), "2024-04-10")

class SortFunctionTest(TestCase):
    def setUp(self):
        self.author0 = Author.objects.create(
            Last_Name="Doe",
            First_Name="John",
            Email="test@test.com")
        self.author1 = Author.objects.create(
            Last_Name="John",
            First_Name="John",
            Email="test@test.com")
        self.author2 = Author.objects.create(
            Last_Name="Johnston",
            First_Name="John",
            Email="test@test.com")
        self.author3 = Author.objects.create(
            Last_Name="name",
            First_Name="test",
            Email="test@test.com")  
        self.item0 = Item.objects.create(
            Title="Image Title 0",
            Author=self.author0,
            Miniature_Image="test_miniatureImg0.jpg",
            Upload_Date="2024-03-30",
            Media=1
        )
        self.image = Item_Image.objects.create(
            Item=self.item0,
            Image="test_image.jpg",
            View_Detail="Test View Detail",
            Index=1
        )
        self.item1 = Item.objects.create(
            Title="Image Title 1",
            Author=self.author1,
            Miniature_Image="test_miniatureImg1.jpg",
            Upload_Date="2024-04-04",
            Media=1,
        )
        self.item2 = Item.objects.create(
            Title="Image Title 2",
            Author=self.author2,
            Miniature_Image="test_minitureImg2.jpg",
            Upload_Date="2024-04-10",
            Media=1,
        )
        self.item3 = Item.objects.create(
            Title="Image Title 3",
            Author=self.author3,
            Miniature_Image="test_minitureImg3.jpg",
            Upload_Date="2024-04-14",
            Media=1,
        )
        self.image1 = Item_Image.objects.create(
            Item=self.item1,
            Image="test_image1.jpg",
            View_Detail="Test View Detail 1",
            Index=1
        )
        self.image2 = Item_Image.objects.create(
            Item=self.item2,
            Image="test_image2.jpg",
            View_Detail="Test View Detail 2",
            Index=1
        )
        self.image3 = Item_Image.objects.create(
            Item=self.item3,
            Image="test_image3.jpg",
            View_Detail="Test View Detail 3",
            Index=1
        )

    def test_sort_year_old_to_new(self):
        data = Item.objects.all()
        sortFunction_data = sortFunction(data, "year-old-to-new")
        expected_data = [Item.objects.get(Title=title) for title in ["Image Title 0", "Image Title 1", "Image Title 2", "Image Title 3"]]
        self.assertEqual(list(sortFunction_data), expected_data)

    def test_sort_year_desc(self):
        data = Item.objects.all()
        sortFunction_data = sortFunction(data, "year-new-to-old")
        print("sorted dates:", list(data.order_by("-Upload_Date")))
        expected_data = [Item.objects.get(Title=title) for title in ["Image Title 3", "Image Title 2", "Image Title 1", "Image Title 0"]]
        print("recieved dates:", sortFunction_data)
        self.assertEqual(expected_data, list(sortFunction_data))

    def test_sort_author_asc(self):
        data = Item.objects.all()
        sortFunction_data = sortFunction(data, "author-asc")
        expected_data = [Item.objects.get(Title=title) for title in ["Image Title 0", "Image Title 1", "Image Title 2", "Image Title 3"]]
        self.assertEqual(expected_data, list(sortFunction_data))

    def test_sort_author_des(self):
        data = Item.objects.all()
        sortFunction_data = sortFunction(data, "author-des")
        expected_data = [Item.objects.get(Title=title) for title in ["Image Title 3", "Image Title 2", "Image Title 1", "Image Title 0"]]
        self.assertEqual(expected_data, list(sortFunction_data))

    def test_sort_title_asc(self):
        data = Item.objects.all()
        sortFunction_data = sortFunction(data, "title-asc")
        expected_data = [Item.objects.get(Title=title) for title in ["Image Title 0", "Image Title 1", "Image Title 2", "Image Title 3"]]
        self.assertEqual(expected_data, list(sortFunction_data))

    def test_sort_title_des(self):
        data = Item.objects.all()
        sortFunction_data = sortFunction(data, "title-des")
        expected_data = [Item.objects.get(Title=title) for title in ["Image Title 3", "Image Title 2", "Image Title 1", "Image Title 0"]]
        self.assertEqual(expected_data, list(sortFunction_data))

class UploadItemFunctionTests(TestCase):
    def test_uploadItemFunction(self):
        authorName = 'John Doe'
        title = 'Test Item'
        images = ['test_image.jpg', 'another_image.jpg']
        uploadDate = datetime.now()
        email = 'test@test.com'
        details = ['Detail 1', 'Detail 2']

        new_item = uploadItemFunction(authorName, title, images, uploadDate, email, details)
        self.assertIsInstance(new_item, Item)
        self.assertEqual(new_item.Title, title)
        self.assertEqual(new_item.Media, len(images))
        item_images = Item_Image.objects.filter(Item=new_item)
        self.assertEqual(len(item_images), len(images))
        imagesList = enumerate(item_images)
        for i, item_image in imagesList:
            index = i+1
            self.assertEqual(item_image.View_Detail, details[i])
            self.assertEqual(item_image.Index, index)

class UploadImageFunctionTests(TestCase):
    def setUp(self):
        author = Author.objects.create(
            Last_Name="Doe",
            First_Name="John",
            Email="test@test.com")
        self.item = Item.objects.create(
            Title="Image Title",
            Author=author,
            Miniature_Image="miniture.jpg",
            Media=1
        )
    def test_uploadImageFunction(self):
        image = 'test_image.jpg'
        detail = 'Test Detail'
        index = 1

        item_image = uploadImageFunction(self.item, image, detail, index)
        self.assertIsInstance(item_image, Item_Image)
        self.assertEqual(item_image.Item, self.item)
        self.assertEqual(item_image.Image, image)
        self.assertEqual(item_image.View_Detail, detail)
        self.assertEqual(item_image.Index, index)

