import hashlib
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Category, ComponentDocumentLink, Component, DocumentType, Document, LocationType, Location, Manufacturer, Package, PurchaseDetail, Purchase, Supplier, StockMovement

class CategoryModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.category = Category.objects.create(name='Test Category', user=self.user)

    def test_category_creation(self):
        self.assertEqual(str(self.category), self.category.name)

class ComponentDocumentLinkModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.document_type = DocumentType.objects.create(name='Test Document Type', user=self.user)
        self.document = Document.objects.create(name='Test Document', title='Test Title', document_type=self.document_type, user=self.user, content='Test Content')
        self.component = Component.objects.create(model='Test Model', manufacturer=Manufacturer.objects.create(name='Test Manufacturer'), category=Category.objects.create(name='Test Category', user=self.user), package=Package.objects.create(name='Test Package', user=self.user), location=Location.objects.create(name='Test Location', location_type=LocationType.objects.create(name='Test Location Type', user=self.user)), user=self.user)

    def test_component_document_link_creation(self):
        link = ComponentDocumentLink.objects.create(document=self.document, component=self.component, user=self.user)
        self.assertEqual(link.document, self.document)
        self.assertEqual(link.component, self.component)

class ComponentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.component = Component.objects.create(model='Test Model', manufacturer=Manufacturer.objects.create(name='Test Manufacturer'), category=Category.objects.create(name='Test Category', user=self.user), package=Package.objects.create(name='Test Package', user=self.user), location=Location.objects.create(name='Test Location', location_type=LocationType.objects.create(name='Test Location Type', user=self.user)), user=self.user)

    def test_component_creation(self):
        self.assertEqual(str(self.component), self.component.model)

    def test_component_slug_creation(self):
        self.assertEqual(self.component.slug, 'test-model')

    def test_get_user_components(self):
        user_components = Component.get_user_components(self.user)
        self.assertIn(self.component, user_components)

class DocumentTypeModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.document_type = DocumentType.objects.create(name='Test Document Type', user=self.user)

    def test_document_type_creation(self):
        self.assertEqual(str(self.document_type), self.document_type.name)

class DocumentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.document_type = DocumentType.objects.create(name='Test Document Type', user=self.user)
        self.document = Document.objects.create(name='Test Document', title='Test Title', document_type=self.document_type, user=self.user, content='Test Content')

    def test_document_creation(self):
        self.assertEqual(str(self.document), self.document.name)

    def test_document_hash_value_creation(self):
        hash_object = hashlib.md5(self.document.content.encode())
        expected_hash_value = hash_object.hexdigest()
        self.assertEqual(self.document.hash_value, expected_hash_value)

class LocationTypeModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.location_type = LocationType.objects.create(name='Test Location Type', user=self.user)

    def test_location_type_creation(self):
        self.assertEqual(str(self.location_type), self.location_type.name)

class LocationModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.location_type = LocationType.objects.create(name='Test Location Type', user=self.user)
        self.location = Location.objects.create(name='Test Location', location_type=self.location_type, user=self.user)

    def test_location_creation(self):
        self.assertEqual(str(self.location), self.location.name)

class ManufacturerModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.manufacturer = Manufacturer.objects.create(name='Test Manufacturer', user=self.user)

    def test_manufacturer_creation(self):
        self.assertEqual(str(self.manufacturer), self.manufacturer.name)

class PackageModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.package = Package.objects.create(name='Test Package', user=self.user)

    def test_package_creation(self):
        self.assertEqual(str(self.package), self.package.name)

class PurchaseDetailModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.component = Component.objects.create(model='Test Model', manufacturer=Manufacturer.objects.create(name='Test Manufacturer'), category=Category.objects.create(name='Test Category', user=self.user), package=Package.objects.create(name='Test Package', user=self.user), location=Location.objects.create(name='Test Location', location_type=LocationType.objects.create(name='Test Location Type', user=self.user)), user=self.user)
        self.purchase = Purchase.objects.create(date='2024-01-29', supplier=Supplier.objects.create(name='Test Supplier', user=self.user), user=self.user)
        self.purchase_detail = PurchaseDetail.objects.create(purchase=self.purchase, component=self.component, quantity=10, user=self.user)

    def test_purchase_detail_creation(self):
        self.assertEqual(str(self.purchase_detail), f'{self.purchase_detail.purchase} - {self.purchase_detail.component}')

class PurchaseModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.supplier = Supplier.objects.create(name='Test Supplier', user=self.user)
        self.purchase = Purchase.objects.create(date='2024-01-29', supplier=self.supplier, user=self.user)

    def test_purchase_creation(self):
        self.assertEqual(str(self.purchase), f'{self.purchase.date} - {self.purchase.supplier}')

class SupplierModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.supplier = Supplier.objects.create(name='Test Supplier', user=self.user)

    def test_supplier_creation(self):
        self.assertEqual(str(self.supplier), self.supplier.name)

class StockMovementModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.component = Component.objects.create(model='Test Model', manufacturer=Manufacturer.objects.create(name='Test Manufacturer'), category=Category.objects.create(name='Test Category', user=self.user), package=Package.objects.create(name='Test Package', user=self.user), location=Location.objects.create(name='Test Location', location_type=LocationType.objects.create(name='Test Location Type', user=self.user)), user=self.user)
        self.source_location = Location.objects.create(name='Source Location', location_type=LocationType.objects.create(name='Test Location Type', user=self.user), user=self.user)
        self.destination_location = Location.objects.create(name='Destination Location', location_type=LocationType.objects.create(name='Test Location Type', user=self.user), user=self.user)
        self.stock_movement = StockMovement.objects.create(component=self.component, quantity=5, source_location=self.source_location, destination_location=self.destination_location, user=self.user)

    def test_stock_movement_creation(self):
        self.assertEqual(str(self.stock_movement), f'{self.stock_movement.source_location} -> {self.stock_movement.destination_location}')

