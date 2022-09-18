import get_pictures
import time
import random
from datetime import datetime
import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType
import sys
sys.path.insert(0, '../')
 
 #тест гитхаб
#login, password='login','password'
# vk_session = vk_api.VkApi(login, password)
# vk_session.auth()
token = ''
vk_session = vk_api.VkApi(token=token)
 
session_api = vk_session.get_api()
 
longpoll = VkLongPoll(vk_session)
phone = ["photo-106372220_457254777"]
 
def send_message(vk_session, id_type, id, message=None, attachment=None, keyboard=None):
    vk_session.method('messages.send', {id_type: id, 'message': message, 'random_id': random.randint(
        -2147483648, +2147483648), "attachment": attachment, 'keyboard': keyboard})
 
def main_loop():
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Сообщение пришло в: ' +
                  str(datetime.strftime(datetime.now(), "%H:%M:%S")))
            print('Текст сообщения: ' + str(event.text))
            print(event.user_id)
            response = event.text.lower()
            keyboard = VkKeyboard(one_time=False)
            

            if event.from_user and not event.from_me:
                if (response == "привет") or (response == "хай") or (response == "приве") or (response == "прив") or (response == "hi") or (response == "hello") or (response == "команды") or (response == "помоги") or (response == "добрый день") or (response == "ghbdtn") or (response == "помощь" )or (response == "help") or (response == "доброе утро") or (response == "добрый вечер") or (response == "что ты можешь?") or (response == "что ты можешь"):
                    keyboard.add_button('Меню', color=VkKeyboardColor.POSITIVE)
                    send_message(vk_session, 'user_id', event.user_id,
                                 message='Привет, нажми на кнопку, чтобы получить список команд', keyboard=keyboard.get_keyboard())
 
                elif response == "меню":
                    keyboard.add_openlink_button(
                        'Заказ справки с места обучения', link="https://student-spravki.bashedu.ru/application_form")
 
                    keyboard.add_line()  
                    keyboard.add_openlink_button(
                        'Заявления на соц стипендию и мат помощь', link="https://vk.com/docs-42498111")
 
                    keyboard.add_line()  
                    keyboard.add_button(
                        'контакты', color=VkKeyboardColor.POSITIVE)
                    

                    keyboard.add_line()  
                    keyboard.add_openlink_button(
                        'Обходной лист для отчисленных студентов', link="https://vk.com/wall-75465069_2969")
                        
                    keyboard.add_line()  
                    keyboard.add_openlink_button(
                        'Расписание', link="https://bashedu.ru/raspisanie-fakulteta-matematiki-i-informacionnykh-tekhnologiy")
                    
                    keyboard.add_line()
                    keyboard.add_openlink_button(
                        'Личный кабинет БашГУ', link="https://cabinet.bashedu.ru/")
                    keyboard.add_openlink_button(
                        'СДО', link="http://sdo.bashedu.ru/")
                    
                    
                    
                    keyboard.add_line()  
                    keyboard.add_openlink_button(
                        'Подслушано', link="https://vk.com/podslushanobashgu")
                    keyboard.add_openlink_button(
                        'Новости БашГУ', link="https://vk.com/public30836025")
                    
                   
                        
                    
                    keyboard.add_line()
                    keyboard.add_openlink_button(
                        'Профбюро ФМИИТ', link="https://vk.com/fmiit_bashedu")
                    keyboard.add_openlink_button(
                        'Профком', link="https://vk.com/clubprofbsu")
                    
                        
 
                    keyboard.add_line()
                    keyboard.add_button(
                        'время работы деканата', color=VkKeyboardColor.PRIMARY)
                     
                    keyboard.add_line()
                    keyboard.add_button(
                        'закрыть', color=VkKeyboardColor.NEGATIVE)
                   

                    send_message(vk_session, 'user_id', event.user_id,
                                 message='Пожалуйста', keyboard=keyboard.get_keyboard())
                elif response == 'пока':
                    send_message(vk_session, 'user_id', event.user_id,
                                 message='Пока')
                elif (response == 'время работы деканата') or (response == 'время') or (response == 'работа деканата') or (response == 'работа') or (response == 'деканат') or (response == 'время деканата') or (response == 'где находится деканат'):
                    vk_session.method("messages.send", {"user_id": event.user_id, "message": "Деканат", "attachment": "photo-204504130_457239068", "random_id": 0})
                elif response == 'контакты':
                    vk_session.method("messages.send", {"user_id": event.user_id, "message": "Контакты", "attachment": "photo-204504130_457239067", "random_id": 0})
                elif response == 'закрыть':
                    print('закрываем клаву')
                    send_message(vk_session, 'user_id', event.user_id,
                                 message='Закрыть', keyboard=keyboard.get_empty_keyboard())
                
                    
                else:
                    vk_session.method("messages.send",{"user_id":event.user_id,"message":"я тебя не понял","random_id":random.randint(1,1000)})
 
            print('-' * 30)
 
 
if __name__ == "__main__":
    while True:
        try:
            main_loop()
        except (KeyboardInterrupt, SystemExit):
            break
        except Exception as e:
            print(f"Ошибка вышла: {e}")
            print("Restart bot ...")
            continue
