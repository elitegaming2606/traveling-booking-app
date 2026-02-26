import requests

class PaymentGateway:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.paymentgateway.com/v1"

    def process_payment(self, amount, currency, payment_method):
        url = f"{self.base_url}/payments"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }
        data = {
            'amount': amount,
            'currency': currency,
            'payment_method': payment_method
        }
        response = requests.post(url, json=data, headers=headers)
        return response.json()

# Example usage
if __name__ == '__main__':
    payment_service = PaymentGateway(api_key='your_api_key_here')
    result = payment_service.process_payment(1000, 'USD', 'credit_card')
    print(result)