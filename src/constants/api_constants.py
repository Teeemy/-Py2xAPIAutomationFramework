# APIconstants is a class which contain all the end point.. we keep all the urls
# staticmethod : # it means it can be called without the obj. directly by using class. it can be called

class APIConstants(object): # creating class which inherit frm obj

    @staticmethod
    def base_url(self):
        return "https://restful-booker.herokuapp.com"

    @staticmethod
    def url_create_booking():
        return "https://restful-booker.herokuapp.com/booking"

    @staticmethod
    def url_create_token():
        return "https://restful-booker.herokuapp.com/auth"
    # update,put,delete requires bookingid

    def url_patch_put_delete(booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)
