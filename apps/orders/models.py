from django.db import models
from jsonfield import JSONField
from apps.galeria.models import Arte
from apps.customers.models import CustomerProfile


class Product(models.Model):
    #correlation of fields
    

    isCustomizeable = models.BooleanField(default=True)
    product_id = models.IntegerField()
    product_code = models.CharField(max_length=20)
    sku_id = models.IntegerField()
    product_name = models.CharField(max_length=255)
    product_name_html = models.CharField(max_length=255)
    product_total = models.DecimalField(max_digits=10, decimal_places=2)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_delivery_time = models.CharField(max_length=255,null=True)
    image = models.URLField()
    brand = models.CharField(max_length=255, null=True)
    category = models.CharField(max_length=255)
    external_id_product = models.IntegerField(null=True)
    external_id_sku = models.IntegerField(null=True)
    is_kit = models.BooleanField()
    products_kit = models.JSONField(null=True)
    sku_code = models.CharField(max_length=20, null=True)
    product_cross_docking = models.IntegerField()
    attributes = models.JSONField(null=True)
    # ... define other relevant fields for the product




    def __str__(self):    
        return f" { self.product_code} {self.product_name} {self.category}"
    
class Order(models.Model):
    #correlation of fields
    customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE, related_name='orders')

    #dados do pedido
    idQueue = models.IntegerField(null=True)
    order_deliveryTime = models.IntegerField(null=True)
    idOrder = models.IntegerField(null=True)
    dateOrder = models.DateTimeField(null=True)

    

    nameStatus = models.CharField(max_length=255, null=True)
    orderType = models.IntegerField(null=True)
    idShipping = models.IntegerField(null=True)
    idShippingHub = models.IntegerField(null=True)
    shippingCompany = models.CharField(max_length=255, null=True)
    shippingMode = models.CharField(max_length=255, null=True)
    group = models.CharField(max_length=255, null=True)
    order_crossDocking = models.IntegerField(null=True)
    nameShipping = models.CharField(max_length=255, null=True)
    historyListOrderStatus = JSONField(null=True)
    codigoExternoFrete = models.CharField(max_length=255, null=True)
    

    #dados financeiros
    order_total = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    totalShipping = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    totalDiscount = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    totalItens = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    totalInstallment = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    totalShoppingVoucher = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    numberOfInstallments = models.IntegerField(null=True)
    valueOfInstallment = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    interestValue = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    creditCardFlag = models.CharField(max_length=255, null=True)
    idPaymentBrand = models.IntegerField(null=True)
    orderPayment = JSONField(null=True)
    namePaymentMethodGateway = models.CharField(max_length=255, null=True)
    paymentDate = models.DateTimeField(null=True)
    paymentFormId = models.IntegerField(null=True)
    paymentFormDescription = models.CharField(max_length=255, null=True)



    #customer data
    idCustomer = models.IntegerField(null=True)
    typeCustomer = models.CharField(max_length=1, null=True)
    birthDate = models.DateField(null=True)
    gender = models.CharField(max_length=255, null=True)
    phone1 = models.CharField(max_length=255, null=True)
    phone2 = models.CharField(max_length=255, null=True)
    b2bB2c = models.IntegerField(null=True)
    idSeller = models.IntegerField(null=True)
    address = JSONField(null=True)
    billingAddress = JSONField(null=True)
    email = models.EmailField(null=True)
    nameCustomer = models.CharField(max_length=255, null=True)
    cpf_cnpj = models.CharField(max_length=255, null=True)
    rg_ie = models.CharField(max_length=255, null=True)

    #useless fields
    shippingRegister = models.CharField(max_length=255, null=True)
    externalId = models.IntegerField(null=True)
    idPaymentType = models.CharField(max_length=255, null=True)
    idAdminCard = models.CharField(max_length=255, null=True)
    cardAuthorizationCode = models.CharField(max_length=255, null=True)
    cardNsu = models.CharField(max_length=255, null=True)
    orderNotes = models.TextField(null=True)
    marketPlaceNumberOrder = models.CharField(max_length=255, null=True)
    marketPlaceID = models.IntegerField(null=True)
    marketPlaceName = models.CharField(max_length=255, null=True)
    marketPlaceDateCreated = models.DateTimeField(null=True)
    marketPlaceStore = models.CharField(max_length=255, null=True)
    billNumber = models.CharField(max_length=255, null=True)
    proofOfSale = models.CharField(max_length=255, null=True)
    originApp = models.BooleanField(null=True)
    orderZapcommerce = JSONField(null=True)
    orderCD = models.CharField(max_length=255, null=True)
    sellerCode = JSONField(null=True)
    codeBank = models.CharField(max_length=255, null=True)
    nameBank = models.CharField(max_length=255, null=True)
    agency = models.CharField(max_length=255, null=True)
    checkingAccount = models.CharField(max_length=255, null=True)
    deliveryShipping = models.DateTimeField(null=True)
    customerExternalId = models.IntegerField(null=True)
    paymentLink = models.CharField(max_length=255, null=True)
    metaData = models.TextField(null=True)
    idTypePayment = models.IntegerField(null=True)
    usefulDay = models.IntegerField(null=True)
    nameCarrying = models.CharField(max_length=255, null=True)
    trackingLink = models.CharField(max_length=255, null=True)
    recurrentCodePlan = models.CharField(max_length=255, null=True)
    recurrentSelectedTime = models.DateTimeField(null=True)
    descricaoDetalhada = models.TextField(null=True)
    expirationDate = models.DateTimeField(null=True)
   

    def __str__(self):
        return f"{self.idOrder}"
    

   
class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_products')
    customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE, related_name='OrderProduct')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    idOrderItem = models.IntegerField()
    artes = models.ManyToManyField(Arte)  

    def __str__(self):
        return f"{self.quantity} {self.product.product_code} {self.product.product_name}"

