from dotenv import load_dotenv
load_dotenv(verbose=True)

from app.service.publish_terror_attacks_service import publish_terror_attacks



if __name__ == '__main__':
    publish_terror_attacks()
