import requests, os, json
from django_q.tasks import async_task
from dotenv import load_dotenv
from datetime import datetime
from django.contrib.auth.models import User
from django.conf import settings
from apps.orders.models import Order, Product
from apps.customers.models import CustomerProfile
from datetime import datetime
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
        
        #print(response_data)

        # Parse the JSON response into a list of dictionaries
        #orders = json.loads(response_data)
        
        # Iterate over the orders and process each one
        for item in response_data:
            order_id = item['entity']['idOrder']

            order_items = item['entity']['orderItems']
            #for order_item in order_items:
                #product_id = order_item['idOrderItem']
                
                #print("Order ID:", order_id)
                #print("Product ID:", product_id)

            order_data = item['entity']
            handle_order_created(order_data, order_items)


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
    birthDate=birth_date,
    typeCustomer=order_data['typeCustomer'],
    address=order_data['address'],
    billingAddress=order_data['billingAddress'],
    gender=order_data['gender'],
    cpf_cnpj=order_data['cpf_cnpj'],
    rg_ie=order_data['rg_ie'],
    customerExternalId=order_data['customerExternalId']

    # Extract order details
    idQueue = order_data.get("idQueue")
    order_id = order_data.get("idOrder")
    dateOrder = order_date
    historyListOrderStatus = order_data.get("historyListOrderStatus")
    b2bB2c = order_data.get("b2bB2c")
    idSeller = order_data.get("idSeller")
    orderNotes = order_data.get("orderNotes")
    nameStatus = order_data.get("nameStatus")
    customer_email = order_data.get("email")

    #delivery
    deliveryTime = order_data.get("deliveryTime")
    crossDocking = order_data.get("crossDocking")
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
    total = order_data.get("total")
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
        user = User.objects.get(email=customer_email)
    except User.DoesNotExist:
        # Create a new user
        user = User.objects.create_user(
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
            idCustomer = idCustomer,
            nameCustomer = nameCustomer,
            phone1=phone1,
            phone2=phone2,
            birthDate=birthDate,
            typeCustomer=typeCustomer,
            address=address,
            billingAddress=billingAddress,
            gender=gender,
            cpf_cnpj=cpf_cnpj,
            rg_ie=rg_ie,
            customerExternalId=customerExternalId,
            #custom fields below
            
            )

    

    # Create a new instance of the order
    order = Order.objects.create(
        idOrder=order_id,
        customer=customer,
        # ... set other order fields based on the extracted data
    )

    # Process the order items
    for order_item in order_items:
        product_data = order_item

        # Create a new instance of the product and associate it with the order
        product = Product.objects.create(
            order=order,
            # ... set other product fields based on the extracted data
        )

        # ... process other nested JSON data if needed

    # Perform additional business logic or validations for the order
    # ... perform calculations, generate invoices, send notifications, etc.

    # Save the changes in the database
    order.save()

    # Trigger further actions or notifications if needed
    # ... notify the customer, update analytics, trigger downstream processes, etc.
