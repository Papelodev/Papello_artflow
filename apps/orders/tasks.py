import requests, os, json
from django_q.tasks import async_task
from dotenv import load_dotenv
from apps.orders.models import Order
load_dotenv()
from datetime import datetime

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
        print(response_data.get('access_token'))
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
        
        print(response_data)

        # Parse the JSON response into a list of dictionaries
        #orders = json.loads(response_data)
        
        # Iterate over the orders and process each one
        for item in response_data:
            order_id = item['entity']['idOrder']

            order_items = item['entity']['orderItems']
            for order_item in order_items:
                product_id = order_item['idOrderItem']
                
                print("Order ID:", order_id)
                print("Product ID:", product_id)

            order_data = item['entity']



            # Modify the birthDate format
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
                    order_date = datetime.strptime(birth_date_str, '%Y-%m-%dT%H:%M:%S').date()
                except:
                    pass
                         

            # Create an Order object with the JSON data
            order = Order.objects.create(
                idQueue=item['idQueue'],
                idOrder=order_data['idOrder'],
                idCustomer=order_data['idCustomer'],
                orderItems=order_data['orderItems'],
                dateOrder=order_date,
                total=order_data['total'],
                namePaymentMethodGateway=order_data['namePaymentMethodGateway'],
                totalShoppingVoucher=order_data['totalShoppingVoucher'],
                idTypePayment=order_data['idTypePayment'],
                orderPayment=order_data['orderPayment'],
                codigoExternoFrete=order_data['codigoExternoFrete'],
                deliveryTime=order_data['deliveryTime'],
                expirationDate=order_data['expirationDate'],
                nameCustomer=order_data['nameCustomer'],
                phone1=order_data['phone1'],
                phone2=order_data['phone2'],
                birthDate=birth_date,
                typeCustomer=order_data['typeCustomer'],
                address=order_data['address'],
                billingAddress=order_data['billingAddress'],
                email=order_data['email'],
                gender=order_data['gender'],
                cpf_cnpj=order_data['cpf_cnpj'],
                paymentDate=order_data['paymentDate'],
                paymentFormId=order_data['paymentFormId'],
                paymentFormDescription=order_data['paymentFormDescription'],
                totalItens=order_data['totalItens'],
                totalInstallment=order_data['totalInstallment'],
                historyListOrderStatus=order_data['historyListOrderStatus'],
                idShipping=order_data['idShipping'],
                idShippingHub=order_data['idShippingHub'],
                shippingCompany=order_data['shippingCompany'],
                shippingMode=order_data['shippingMode'],
                shippingRegister=order_data['shippingRegister'],
                group=order_data['group'],
                b2bB2c=order_data['b2bB2c'],
                externalId=order_data['externalId'],
                idPaymentType=order_data['idPaymentType'],
                idAdminCard=order_data['idAdminCard'],
                cardAuthorizationCode=order_data['cardAuthorizationCode'],
                cardNsu=order_data['cardNsu'],
                orderNotes=order_data['orderNotes'],
                marketPlaceNumberOrder=order_data['marketPlaceNumberOrder'],
                marketPlaceID=order_data['marketPlaceID'],
                marketPlaceName=order_data['marketPlaceName'],
                marketPlaceDateCreated=order_data['marketPlaceDateCreated'],
                marketPlaceStore=order_data['marketPlaceStore'],
                idSeller=order_data['idSeller'],
                crossDocking=order_data['crossDocking'],
                billNumber=order_data['billNumber'],
                proofOfSale=order_data['proofOfSale'],
                originApp=order_data['originApp'],
                orderZapcommerce=order_data['orderZapcommerce'],
                orderCD=order_data['orderCD'],
                sellerCode=order_data['sellerCode'],
                totalShipping=order_data['totalShipping'],
                totalDiscount=order_data['totalDiscount'],
                idPaymentBrand=order_data['idPaymentBrand'],
                codeBank=order_data['codeBank'],
                nameBank=order_data['nameBank'],
                agency=order_data['agency'],
                checkingAccount=order_data['checkingAccount'],
                creditCardFlag=order_data['creditCardFlag'],
                numberOfInstallments=order_data['numberOfInstallments'],
                valueOfInstallment=order_data['valueOfInstallment'],
                rg_ie=order_data['rg_ie'],
                nameShipping=order_data['nameShipping'],
                deliveryShipping=order_data['deliveryShipping'],
                customerExternalId=order_data['customerExternalId'],
                paymentLink=order_data['paymentLink'],
                metaData=order_data['metaData'],
                usefulDay=order_data['usefulDay'],
                nameCarrying=order_data['nameCarrying'],
                trackingLink=order_data['trackingLink'],
                recurrentCodePlan=order_data['recurrentCodePlan'],
                recurrentSelectedTime=order_data['recurrentSelectedTime'],
                interestValue=order_data['interestValue'],
                descricaoDetalhada=order_data['descricaoDetalhada'],
                nameStatus=order_data['nameStatus'],
                orderType=order_data['orderType']
            )

            order.save()

             # Check if the order was saved successfully
            if order.pk:
                print("Order saved successfully. ID:", order.pk)
            else:
                print("Failed to save order.")


    else:
        print('Error:', response.status_code)
        print(response.json().get('message'))
        
def delete_orders():
    orders = Order.objects.all()

    orders.delete()