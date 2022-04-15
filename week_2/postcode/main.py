from postcode_service.postcode_manager import PostcodeManager

def postcode(postcode_string):
    return PostcodeManager(postcode_string).get_postcode()

if __name__ == "__main__":
    pc = postcode("B7 4BB")
    print(pc)
    print(pc.admin_district)