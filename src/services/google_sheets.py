import gspread
import os
from dotenv import load_dotenv
from google.oauth2.service_account import Credentials
from src.services.models import OfferJob

load_dotenv()


class GoogleSheetOfferJobManager:
    def __init__(self):
        # charger le compte de service
        self.service_account_file = os.getenv("VERTEXAI_KEY_NAME")
        self.scopes = ["https://www.googleapis.com/auth/spreadsheets"]
        self.spreadsheet_id = "1HTN_iJuK1gbIgdDr-iGTen8SNQJq4BUz21nHGb8u5I8"

        creds = Credentials.from_service_account_file(self.service_account_file, scopes=self.scopes)
        self.client = gspread.authorize(creds)
        self.sheet = self.client.open_by_key(self.spreadsheet_id).sheet1

    def add_offer(self, offer: OfferJob):
        """Ajoute une offre d'emploi dans la liste"""
        data = offer.to_list()
        self.sheet.append_row(data)


if __name__ == "__main__":
    offer = ["TechCorp", "Paris", "à distance", "Software Engineer", "Develop and maintain software solutions.",
             "Python\nDjango\nREST APIs", "CDI", "2024-03-05", "", "", "", "", ""]
    manager = GoogleSheetOfferJobManager()
    job = OfferJob.from_list(offer)

    manager.add_offer(job)
