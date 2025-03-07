from dataclasses import dataclass
from typing import List


@dataclass
class OfferJob:
    company_name: str
    job_title: str
    location: str
    teleworking: str
    job_description: str
    required_skills: str
    contract_type: str
    offer_date: str
    offer_link: str
    company_presentation: str
    answer_message: str
    answer_date: str
    status: str

    @staticmethod
    def from_list(data: List[str]) -> "OfferJob":
        return OfferJob(
            company_name=data[0],
            job_title=data[1],
            location=data[2],
            teleworking=data[3],
            job_description=data[4],
            required_skills=data[5],
            contract_type=data[5],
            offer_date=data[7],
            offer_link=data[8],
            company_presentation=data[9],
            answer_message=data[10],
            answer_date="",
            status=""
        )

    def to_list(self) -> List[str]:
        """Transformer le modèle en liste d'attributs"""
        return [
            self.company_name,
            self.location,
            self.teleworking,
            self.job_title,
            self.job_description,
            self.required_skills,
            self.contract_type,
            self.offer_date,
            self.offer_link,
            self.company_presentation,
            self.answer_message,
            self.answer_date,
            self.status
        ]

    def __str__(self):
        return (f"Job Offer: {self.job_title} at {self.company_name}\n"
                f"Contract: {self.contract_type}\n"
                f"Posted on: {self.offer_date}\n"
                f"More info: {self.offer_link if self.offer_link else 'N/A'}")


# Exemple d'utilisation
if __name__ == "__main__":
    offer = ["TechCorp", "Paris", "à distance", "Software Engineer", "Develop and maintain software solutions.",
             "Python\nDjango\nREST APIs", "CDI", "2024-03-05", "", "", "", "", ""]
    job = OfferJob.from_list(offer)
    print(job)
    print(job.to_list())
