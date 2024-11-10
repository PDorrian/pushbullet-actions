from pushbullet import Pushbullet

def lambda_handler(event, _):
    action = event['action']
    pushbullet_key = event['pushbullet_key']
    pb = Pushbullet(pushbullet_key)

    if action == 'send_sms':
        phone_number = event['phone_number']
        pb.send_sms([phone_number], event['message'])
