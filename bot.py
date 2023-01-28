import vk_api, vk
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id

vk_session = vk_api.VkApi(token='vk1.a.Uqyb6diWQfu0tSCNNAhUlNEKR-Sw_Chw5GKlm2kjeu5UUJObRyy_ZqTXcjdz_nLRKlQ-uO01oXgn13TPD0GovLuQ9P-_Uz4vF1S3hDMqiiNVOe_Wy0znx8btj-xx4atM75XhawfreMCoHwaIU-hudZA2o0vcybH9toQ99KFGMhpl7pxycOoRtGp4Btr39tcBn9tXCuMUv_1aoRwspstBzA')

from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
longpoll = VkBotLongPoll(vk_session, 217010440)
vk = vk_session.get_api()
from vk_api.longpoll import VkLongPoll, VkEventType

keyboard = VkKeyboard(one_time=True)
keyboard.add_button('Привет', color=VkKeyboardColor.NEGATIVE)
keyboard.add_button('Клавиатура', color=VkKeyboardColor.POSITIVE)
keyboard.add_line()
keyboard.add_location_button()
keyboard.add_line()
keyboard.add_vkpay_button(hash="action=transfer-to-group&group_id=217010440")

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if 'Ку' in str(event) or 'Привет' in str(event) or 'Хай' in str(event) or 'Хелло' in str(event) or 'Хеллоу' in str(event):
            if event.from_chat:
                vk.messages.send(
                    key = ('ea508b7b39ea8e29e8cfd2b327f826230146527e'),
                    server = ('https://lp.vk.com/wh217010440'),
                    ts=('1'),
                    random_id = get_random_id(),
                    message='Привет!',
                    chat_id = event.chat_id
                )