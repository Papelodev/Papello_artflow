import requests, os, json
from django_q.tasks import async_task
from dotenv import load_dotenv
from datetime import datetime
from django.contrib.auth.models import User
from apps.usuarios.models import MyUser
from django.conf import settings
from apps.orders.models import Order, Product, Attribute
from apps.customers.models import CustomerProfile


load_dotenv()

def oAuth2_orders():  
    
    url = "https://adm-produto-neo1.plataformaneo.com.br/api/v1/auth"

    payload = {
        "IntegrationKey":str(os.getenv('INTEGRATION_KEY')),
        "userName": str(os.getenv('USER_NAME')),
        "password": str(os.getenv('PASSWORD')),
        "storeID": str(os.getenv('STORE_ID')),
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        response_data = response.json()  # Parse the response as JSON
        #print(response_data.get('access_token'))
        eToken = response_data.get('access_token')
        get_queue(eToken)
    else:
        print('Error:', response.status_code)

def get_queue(eToken):

    url = "https://adm-pedido-neo1.plataformaneo.com.br/api/v1/adm_order/GetQueue"

    
    headers = {
        "accept": "application/json",
        "authorization": "Bearer "+ eToken
    }

    params ={
        "IntegrationKey":str(os.getenv('INTEGRATION_KEY')),
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        response_data = response.json()  # Parse the response as JSON
        
        #limita as execuções (REMOVER!!)
        response_data=response_data

        #print(response_data)

        # Parse the JSON response into a list of dictionaries
        #orders = json.loads(response_data)
        
        # Iterate over the orders and process each one
        for item in response_data:
            order_id = item['entity']['idOrder']
            print("Order ID:", order_id)

            order_items = item['entity']['orderItems']
            #for order_item in order_items:
                #product_id = order_item['idOrderItem']
                
                #print("Product ID:", product_id)
            order_data = item['entity']
            handle_order_created(order_data, order_items)
            break


    else:
        print('Error:', response.status_code)
        print(response.json().get('message'))
        
def handle_order_created(json_data, products):
    
    # Parse the JSON data
    order_data = json_data
    order_items = products

    # Modify the Date format
    birth_date_str = order_data.get('birthDate', '')  # Assuming the birthDate key is present in order_data
    order_date_str = order_data.get('dateOrder','')
    birth_date = None
    order_date = None
    if birth_date_str:
        try:
            birth_date = datetime.strptime(birth_date_str, '%Y-%m-%dT%H:%M:%S').date()
            
        except ValueError:
        # Handle the case where the date format is invalid
        # Set birth_date to None or a default value depending on your requirements
            pass

        if order_date_str:
            try:
                order_date = datetime.strptime(order_date_str, '%Y-%m-%dT%H:%M:%S').date()



            except:
                pass

    #customer data
    idCustomer=order_data['idCustomer'],
    nameCustomer=order_data['nameCustomer'],
    phone1=order_data['phone1'],
    phone2=order_data['phone2'],
    #birthDate=birth_date,
    typeCustomer=order_data['typeCustomer'],
    address=order_data['address'],
    billingAddress=order_data['billingAddress'],
    gender=order_data['gender'],
    cpf_cnpj=order_data['cpf_cnpj'],
    rg_ie=order_data['rg_ie'],
    customerExternalId=order_data['customerExternalId']
    customer_email = order_data.get("email")

    # Extract order details
    idQueue = order_data.get("idQueue")
    order_id = order_data.get("idOrder")
    dateOrder = order_date
    historyListOrderStatus = order_data.get("historyListOrderStatus")
    b2bB2c = order_data.get("b2bB2c")
    idSeller = order_data.get("idSeller")
    orderNotes = order_data.get("orderNotes")
    nameStatus = order_data.get("nameStatus")

    #delivery
    order_deliveryTime = order_data.get("deliveryTime")
    order_crossDocking = order_data.get("crossDocking")
    codigoExternoFrete = order_data.get("codigoExternoFrete")
    nameShipping = order_data.get("nameShipping")
    deliveryShipping = order_data.get("deliveryShipping")
    idShipping = order_data.get("idShipping")
    idShippingHub = order_data.get("idShippingHub")
    shippingCompany = order_data.get("shippingCompany")
    shippingMode = order_data.get("shippingMode")
    shippingRegister = order_data.get("shippingRegister")
    usefulDay = order_data.get("usefulDay")
    nameCarrying = order_data.get("nameCarrying")
    trackingLink = order_data.get("trackingLink")
    
    #payment
    paymentDate = order_data.get("paymentDate")
    order_total = order_data.get("total")
    totalShoppingVoucher = order_data.get("totalShoppingVoucher")
    totalItens = order_data.get("totalItens")
    totalInstallment = order_data.get("totalInstallment")
    totalShipping = order_data.get("totalShipping")
    totalDiscount = order_data.get("totalDiscount")
    numberOfInstallments = order_data.get("numberOfInstallments")
    valueOfInstallment = order_data.get("valueOfInstallment")
    namePaymentMethodGateway = order_data.get("namePaymentMethodGateway")
    idTypePayment = order_data.get("idTypePayment")
    orderPayment = order_data.get("orderPayment")
    paymentFormId = order_data.get("paymentFormId")
    paymentFormDescription = order_data.get("paymentFormDescription")
    idPaymentType = order_data.get("idPaymentType")
    idAdminCard = order_data.get("idAdminCard")
    cardAuthorizationCode = order_data.get("cardAuthorizationCode")
    cardNsu = order_data.get("cardNsu")
    billNumber = order_data.get("billNumber")
    proofOfSale = order_data.get("proofOfSale")
    idPaymentBrand = order_data.get("idPaymentBrand")
    codeBank = order_data.get("codeBank")
    nameBank = order_data.get("nameBank")
    agency = order_data.get("agency")
    checkingAccount = order_data.get("checkingAccount")
    creditCardFlag = order_data.get("creditCardFlag")
    paymentLink = order_data.get("paymentLink")
    recurrentCodePlan = order_data.get("recurrentCodePlan")
    recurrentSelectedTime = order_data.get("recurrentSelectedTime")
    interestValue = order_data.get("interestValue")
    

    #useless
    expirationDate = order_data.get("expirationDate")
    group = order_data.get("group")
    externalId = order_data.get("externalId")
    marketPlaceNumberOrder = order_data.get("marketPlaceNumberOrder")
    marketPlaceID = order_data.get("marketPlaceID")
    marketPlaceName = order_data.get("marketPlaceName")
    marketPlaceDateCreated = order_data.get("marketPlaceDateCreated")
    marketPlaceStore = order_data.get("marketPlaceStore")
    originApp = order_data.get("originApp")
    orderZapcommerce = order_data.get("orderZapcommerce")
    orderCD = order_data.get("orderCD")
    sellerCode = order_data.get("sellerCode")
    descricaoDetalhada = order_data.get("descricaoDetalhada")
    orderType = order_data.get("orderType")
   
    
    
    # ... extract other relevant information from the JSON data

    # Check if the customer already exists or create a new user and customer
    try:
        user = MyUser.objects.get(email=customer_email)
    except MyUser.DoesNotExist:
        # Create a new user
        user = MyUser.objects.create_user(
            username=customer_email,
            email=customer_email,
            password=settings.DEFAULT_USER_PASSWORD  # Set a default password
        )

    try:
        customer = CustomerProfile.objects.get(user=user)
    except CustomerProfile.DoesNotExist:
        # Create a new customer
        customer = CustomerProfile.objects.create(
            user=user,
            email=customer_email,
            idCustomer = idCustomer[0],
            nameCustomer = nameCustomer[0],
            phone1=phone1[0],
            phone2=phone2[0],
            birthDate=birth_date,
            typeCustomer=typeCustomer[0],
            address=address[0],
            billingAddress=billingAddress[0],
            gender=gender[0],
            cpf_cnpj=cpf_cnpj[0],
            rg_ie=rg_ie[0],
            customerExternalId=customerExternalId,
            #custom fields below
            
            )

    

    # Create a new instance of the order
    order = Order.objects.create(
        idOrder=order_id,
        #customer=customer,
        # ... set other order fields based on the extracted data
    )

    # Process the order items
    for order_item in order_items:
        product_data = order_item

         # Extract product details
        idOrderItem = product_data.get("idOrderItem")
        product_id = product_data.get("idProduct")
        productCode = product_data.get("productCode")
        product_name = product_data.get("name")
        nameProduct = product_data.get("nameProduct")
        idSku = product_data.get("idSku")
        quantity = product_data.get("quantity")
        unitPrice = product_data.get("unitPrice")
        product_total = product_data.get("total")
        product_deliveryTime = product_data.get("deliveryTime")
        image = product_data.get("image")
        brand = product_data.get("brand")
        category = product_data.get("category")
        externalIdProduct = product_data.get("externalIdProduct")
        externalIdSku = product_data.get("externalIdSku")
        isKit = product_data.get("isKit")
        productsKit = product_data.get("productsKit")
        skuCode = product_data.get("skuCode")
        product_crossDocking = product_data.get("crossDocking")
       
        
        # Create a new instance of the product and associate it with the order
        product = Product.objects.create(
            order=order,
            idOrderItem=idOrderItem,
            product_id=product_id,
            productCode=productCode,
            product_name=product_name,
            nameProduct=nameProduct,
            idSku=idSku,
            quantity=quantity,
            unitPrice=unitPrice,
            product_total=product_total,
            product_deliveryTime=product_deliveryTime,
            image=image,
            brand=brand,
            category=category,
            externalIdProduct=externalIdProduct,
            externalIdSku=externalIdSku,
            isKit=isKit,
            productsKit=productsKit,
            skuCode=skuCode,
            product_crossDocking=product_crossDocking,            

            # ... set other product fields based on the extracted data
        )
        order.products.add(product)

        attributes_data = order_item.get('attribute', [])
        for attribute_data in attributes_data:
            attribute = Attribute.objects.create(
                name=attribute_data.get('nameAttribute'),
                value=attribute_data.get('value'),
                description=attribute_data.get('description')
        )
            product.attributes.add(attribute)

    # Perform additional business logic or validations for the order
    # ... perform calculations, generate invoices, send notifications, etc.

    # Save the changes in the database
    order.save()

    # Trigger further actions or notifications if needed
    # ... notify the customer, update analytics, trigger downstream processes, etc.
