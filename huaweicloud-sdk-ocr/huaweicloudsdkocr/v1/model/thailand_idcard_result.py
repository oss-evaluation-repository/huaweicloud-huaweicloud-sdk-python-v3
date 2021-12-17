# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ThailandIdcardResult:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'side': 'str',
        'id_number': 'str',
        'name_th': 'str',
        'first_name_en': 'str',
        'last_name_en': 'str',
        'date_of_birth_th': 'str',
        'date_of_birth_en': 'str',
        'religion_th': 'str',
        'address_th': 'str',
        'date_of_issue_th': 'str',
        'date_of_issue_en': 'str',
        'date_of_expiry_th': 'str',
        'date_of_expiry_en': 'str',
        'serial_number': 'str',
        'card_number': 'str',
        'laser_number': 'str',
        'confidence': 'ThailandIdcardConfidence',
        'portrait_image': 'str',
        'portrait_location': 'list[list[int]]',
        'idcard_type': 'str'
    }

    attribute_map = {
        'side': 'side',
        'id_number': 'id_number',
        'name_th': 'name_th',
        'first_name_en': 'first_name_en',
        'last_name_en': 'last_name_en',
        'date_of_birth_th': 'date_of_birth_th',
        'date_of_birth_en': 'date_of_birth_en',
        'religion_th': 'religion_th',
        'address_th': 'address_th',
        'date_of_issue_th': 'date_of_issue_th',
        'date_of_issue_en': 'date_of_issue_en',
        'date_of_expiry_th': 'date_of_expiry_th',
        'date_of_expiry_en': 'date_of_expiry_en',
        'serial_number': 'serial_number',
        'card_number': 'card_number',
        'laser_number': 'laser_number',
        'confidence': 'confidence',
        'portrait_image': 'portrait_image',
        'portrait_location': 'portrait_location',
        'idcard_type': 'idcard_type'
    }

    def __init__(self, side=None, id_number=None, name_th=None, first_name_en=None, last_name_en=None, date_of_birth_th=None, date_of_birth_en=None, religion_th=None, address_th=None, date_of_issue_th=None, date_of_issue_en=None, date_of_expiry_th=None, date_of_expiry_en=None, serial_number=None, card_number=None, laser_number=None, confidence=None, portrait_image=None, portrait_location=None, idcard_type=None):
        """ThailandIdcardResult - a model defined in huaweicloud sdk"""
        
        

        self._side = None
        self._id_number = None
        self._name_th = None
        self._first_name_en = None
        self._last_name_en = None
        self._date_of_birth_th = None
        self._date_of_birth_en = None
        self._religion_th = None
        self._address_th = None
        self._date_of_issue_th = None
        self._date_of_issue_en = None
        self._date_of_expiry_th = None
        self._date_of_expiry_en = None
        self._serial_number = None
        self._card_number = None
        self._laser_number = None
        self._confidence = None
        self._portrait_image = None
        self._portrait_location = None
        self._idcard_type = None
        self.discriminator = None

        if side is not None:
            self.side = side
        if id_number is not None:
            self.id_number = id_number
        if name_th is not None:
            self.name_th = name_th
        if first_name_en is not None:
            self.first_name_en = first_name_en
        if last_name_en is not None:
            self.last_name_en = last_name_en
        if date_of_birth_th is not None:
            self.date_of_birth_th = date_of_birth_th
        if date_of_birth_en is not None:
            self.date_of_birth_en = date_of_birth_en
        if religion_th is not None:
            self.religion_th = religion_th
        if address_th is not None:
            self.address_th = address_th
        if date_of_issue_th is not None:
            self.date_of_issue_th = date_of_issue_th
        if date_of_issue_en is not None:
            self.date_of_issue_en = date_of_issue_en
        if date_of_expiry_th is not None:
            self.date_of_expiry_th = date_of_expiry_th
        if date_of_expiry_en is not None:
            self.date_of_expiry_en = date_of_expiry_en
        if serial_number is not None:
            self.serial_number = serial_number
        if card_number is not None:
            self.card_number = card_number
        if laser_number is not None:
            self.laser_number = laser_number
        if confidence is not None:
            self.confidence = confidence
        if portrait_image is not None:
            self.portrait_image = portrait_image
        if portrait_location is not None:
            self.portrait_location = portrait_location
        if idcard_type is not None:
            self.idcard_type = idcard_type

    @property
    def side(self):
        """Gets the side of this ThailandIdcardResult.

        标示正面还是反面，取值为front或back。 

        :return: The side of this ThailandIdcardResult.
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this ThailandIdcardResult.

        标示正面还是反面，取值为front或back。 

        :param side: The side of this ThailandIdcardResult.
        :type: str
        """
        self._side = side

    @property
    def id_number(self):
        """Gets the id_number of this ThailandIdcardResult.

        身份证号。 

        :return: The id_number of this ThailandIdcardResult.
        :rtype: str
        """
        return self._id_number

    @id_number.setter
    def id_number(self, id_number):
        """Sets the id_number of this ThailandIdcardResult.

        身份证号。 

        :param id_number: The id_number of this ThailandIdcardResult.
        :type: str
        """
        self._id_number = id_number

    @property
    def name_th(self):
        """Gets the name_th of this ThailandIdcardResult.

        泰文名字。 

        :return: The name_th of this ThailandIdcardResult.
        :rtype: str
        """
        return self._name_th

    @name_th.setter
    def name_th(self, name_th):
        """Sets the name_th of this ThailandIdcardResult.

        泰文名字。 

        :param name_th: The name_th of this ThailandIdcardResult.
        :type: str
        """
        self._name_th = name_th

    @property
    def first_name_en(self):
        """Gets the first_name_en of this ThailandIdcardResult.

        英文名字。 

        :return: The first_name_en of this ThailandIdcardResult.
        :rtype: str
        """
        return self._first_name_en

    @first_name_en.setter
    def first_name_en(self, first_name_en):
        """Sets the first_name_en of this ThailandIdcardResult.

        英文名字。 

        :param first_name_en: The first_name_en of this ThailandIdcardResult.
        :type: str
        """
        self._first_name_en = first_name_en

    @property
    def last_name_en(self):
        """Gets the last_name_en of this ThailandIdcardResult.

        英文姓氏。 

        :return: The last_name_en of this ThailandIdcardResult.
        :rtype: str
        """
        return self._last_name_en

    @last_name_en.setter
    def last_name_en(self, last_name_en):
        """Sets the last_name_en of this ThailandIdcardResult.

        英文姓氏。 

        :param last_name_en: The last_name_en of this ThailandIdcardResult.
        :type: str
        """
        self._last_name_en = last_name_en

    @property
    def date_of_birth_th(self):
        """Gets the date_of_birth_th of this ThailandIdcardResult.

        泰文出生日期。 

        :return: The date_of_birth_th of this ThailandIdcardResult.
        :rtype: str
        """
        return self._date_of_birth_th

    @date_of_birth_th.setter
    def date_of_birth_th(self, date_of_birth_th):
        """Sets the date_of_birth_th of this ThailandIdcardResult.

        泰文出生日期。 

        :param date_of_birth_th: The date_of_birth_th of this ThailandIdcardResult.
        :type: str
        """
        self._date_of_birth_th = date_of_birth_th

    @property
    def date_of_birth_en(self):
        """Gets the date_of_birth_en of this ThailandIdcardResult.

        英文出生日期。 

        :return: The date_of_birth_en of this ThailandIdcardResult.
        :rtype: str
        """
        return self._date_of_birth_en

    @date_of_birth_en.setter
    def date_of_birth_en(self, date_of_birth_en):
        """Sets the date_of_birth_en of this ThailandIdcardResult.

        英文出生日期。 

        :param date_of_birth_en: The date_of_birth_en of this ThailandIdcardResult.
        :type: str
        """
        self._date_of_birth_en = date_of_birth_en

    @property
    def religion_th(self):
        """Gets the religion_th of this ThailandIdcardResult.

        宗教。 

        :return: The religion_th of this ThailandIdcardResult.
        :rtype: str
        """
        return self._religion_th

    @religion_th.setter
    def religion_th(self, religion_th):
        """Sets the religion_th of this ThailandIdcardResult.

        宗教。 

        :param religion_th: The religion_th of this ThailandIdcardResult.
        :type: str
        """
        self._religion_th = religion_th

    @property
    def address_th(self):
        """Gets the address_th of this ThailandIdcardResult.

        地址。 

        :return: The address_th of this ThailandIdcardResult.
        :rtype: str
        """
        return self._address_th

    @address_th.setter
    def address_th(self, address_th):
        """Sets the address_th of this ThailandIdcardResult.

        地址。 

        :param address_th: The address_th of this ThailandIdcardResult.
        :type: str
        """
        self._address_th = address_th

    @property
    def date_of_issue_th(self):
        """Gets the date_of_issue_th of this ThailandIdcardResult.

        泰文签发日期。 

        :return: The date_of_issue_th of this ThailandIdcardResult.
        :rtype: str
        """
        return self._date_of_issue_th

    @date_of_issue_th.setter
    def date_of_issue_th(self, date_of_issue_th):
        """Sets the date_of_issue_th of this ThailandIdcardResult.

        泰文签发日期。 

        :param date_of_issue_th: The date_of_issue_th of this ThailandIdcardResult.
        :type: str
        """
        self._date_of_issue_th = date_of_issue_th

    @property
    def date_of_issue_en(self):
        """Gets the date_of_issue_en of this ThailandIdcardResult.

        英文签发日期。 

        :return: The date_of_issue_en of this ThailandIdcardResult.
        :rtype: str
        """
        return self._date_of_issue_en

    @date_of_issue_en.setter
    def date_of_issue_en(self, date_of_issue_en):
        """Sets the date_of_issue_en of this ThailandIdcardResult.

        英文签发日期。 

        :param date_of_issue_en: The date_of_issue_en of this ThailandIdcardResult.
        :type: str
        """
        self._date_of_issue_en = date_of_issue_en

    @property
    def date_of_expiry_th(self):
        """Gets the date_of_expiry_th of this ThailandIdcardResult.

        泰文有效期。 

        :return: The date_of_expiry_th of this ThailandIdcardResult.
        :rtype: str
        """
        return self._date_of_expiry_th

    @date_of_expiry_th.setter
    def date_of_expiry_th(self, date_of_expiry_th):
        """Sets the date_of_expiry_th of this ThailandIdcardResult.

        泰文有效期。 

        :param date_of_expiry_th: The date_of_expiry_th of this ThailandIdcardResult.
        :type: str
        """
        self._date_of_expiry_th = date_of_expiry_th

    @property
    def date_of_expiry_en(self):
        """Gets the date_of_expiry_en of this ThailandIdcardResult.

        英文有效期。 

        :return: The date_of_expiry_en of this ThailandIdcardResult.
        :rtype: str
        """
        return self._date_of_expiry_en

    @date_of_expiry_en.setter
    def date_of_expiry_en(self, date_of_expiry_en):
        """Sets the date_of_expiry_en of this ThailandIdcardResult.

        英文有效期。 

        :param date_of_expiry_en: The date_of_expiry_en of this ThailandIdcardResult.
        :type: str
        """
        self._date_of_expiry_en = date_of_expiry_en

    @property
    def serial_number(self):
        """Gets the serial_number of this ThailandIdcardResult.

        序列号。 

        :return: The serial_number of this ThailandIdcardResult.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this ThailandIdcardResult.

        序列号。 

        :param serial_number: The serial_number of this ThailandIdcardResult.
        :type: str
        """
        self._serial_number = serial_number

    @property
    def card_number(self):
        """Gets the card_number of this ThailandIdcardResult.

        身份证反面卡号。 

        :return: The card_number of this ThailandIdcardResult.
        :rtype: str
        """
        return self._card_number

    @card_number.setter
    def card_number(self, card_number):
        """Sets the card_number of this ThailandIdcardResult.

        身份证反面卡号。 

        :param card_number: The card_number of this ThailandIdcardResult.
        :type: str
        """
        self._card_number = card_number

    @property
    def laser_number(self):
        """Gets the laser_number of this ThailandIdcardResult.

        激光码。 

        :return: The laser_number of this ThailandIdcardResult.
        :rtype: str
        """
        return self._laser_number

    @laser_number.setter
    def laser_number(self, laser_number):
        """Sets the laser_number of this ThailandIdcardResult.

        激光码。 

        :param laser_number: The laser_number of this ThailandIdcardResult.
        :type: str
        """
        self._laser_number = laser_number

    @property
    def confidence(self):
        """Gets the confidence of this ThailandIdcardResult.


        :return: The confidence of this ThailandIdcardResult.
        :rtype: ThailandIdcardConfidence
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this ThailandIdcardResult.


        :param confidence: The confidence of this ThailandIdcardResult.
        :type: ThailandIdcardConfidence
        """
        self._confidence = confidence

    @property
    def portrait_image(self):
        """Gets the portrait_image of this ThailandIdcardResult.

        头像的base64编码。 当输入参数“return_portrait_image”为“true”时，才返回该参数。 

        :return: The portrait_image of this ThailandIdcardResult.
        :rtype: str
        """
        return self._portrait_image

    @portrait_image.setter
    def portrait_image(self, portrait_image):
        """Sets the portrait_image of this ThailandIdcardResult.

        头像的base64编码。 当输入参数“return_portrait_image”为“true”时，才返回该参数。 

        :param portrait_image: The portrait_image of this ThailandIdcardResult.
        :type: str
        """
        self._portrait_image = portrait_image

    @property
    def portrait_location(self):
        """Gets the portrait_location of this ThailandIdcardResult.

        头像在原图上的位置。 当输入参数“return_portrait_location”为“true”时，才返回该参数。以列表形式显示，包含头像区域四个顶点的二维坐标（x,y），坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向 

        :return: The portrait_location of this ThailandIdcardResult.
        :rtype: list[list[int]]
        """
        return self._portrait_location

    @portrait_location.setter
    def portrait_location(self, portrait_location):
        """Sets the portrait_location of this ThailandIdcardResult.

        头像在原图上的位置。 当输入参数“return_portrait_location”为“true”时，才返回该参数。以列表形式显示，包含头像区域四个顶点的二维坐标（x,y），坐标原点为图片左上角，x轴沿水平方向，y轴沿竖直方向 

        :param portrait_location: The portrait_location of this ThailandIdcardResult.
        :type: list[list[int]]
        """
        self._portrait_location = portrait_location

    @property
    def idcard_type(self):
        """Gets the idcard_type of this ThailandIdcardResult.

        身份证的类型。取值如下所示： - normal：身份证原件 - copy：复印的身份证 当输入参数“return_idcard_type”为“true”时，才返回该参数。 

        :return: The idcard_type of this ThailandIdcardResult.
        :rtype: str
        """
        return self._idcard_type

    @idcard_type.setter
    def idcard_type(self, idcard_type):
        """Sets the idcard_type of this ThailandIdcardResult.

        身份证的类型。取值如下所示： - normal：身份证原件 - copy：复印的身份证 当输入参数“return_idcard_type”为“true”时，才返回该参数。 

        :param idcard_type: The idcard_type of this ThailandIdcardResult.
        :type: str
        """
        self._idcard_type = idcard_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ThailandIdcardResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
